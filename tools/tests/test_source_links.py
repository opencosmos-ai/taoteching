import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from http.client import BadStatusLine
from io import BytesIO, StringIO
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError, URLError

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import check_source_links as links


class SourceLinks(unittest.TestCase):
    def test_collects_resolved_links_from_each_surface(self):
        data = {
            "sources": {"records": [{"scan": "https://example.test/édition#page-1",
                                     "editions": [{"url": "https://example.test/edition"}]}]},
            "chapter_sources": {"1": {"readings": [{"url": "https://example.test/reading"}]}},
            "entries": [{"refs": [{"url": "https://example.test/%C3%A9dition#page-2"},
                                  {"url": "https://example.test/citation"},
                                  {"url": "sources/local.md"}],
                         "url": "https://example.test/ignored"}],
        }
        self.assertEqual(links.source_urls(data), [
            "https://example.test/%C3%A9dition", "https://example.test/citation",
            "https://example.test/edition", "https://example.test/reading",
        ])

    @patch.object(links, "urlopen")
    def test_probe_outcomes(self, urlopen):
        url = "https://example.test/source"
        response = urlopen.return_value.__enter__.return_value
        response.getcode.return_value = 200
        self.assertEqual(links.probe(url), "")
        request = urlopen.call_args.args[0]
        self.assertEqual(request.get_header("User-agent"), links.USER_AGENT)
        self.assertEqual(urlopen.call_args.kwargs["timeout"], 10)
        for code, expected in ((403, None), (429, None), (404, "HTTP 404"), (503, "HTTP 503")):
            with self.subTest(code=code):
                urlopen.side_effect = HTTPError(url, code, "test", None, BytesIO())
                self.assertEqual(links.probe(url), expected)
        urlopen.side_effect = URLError("timed out")
        self.assertIsNone(links.probe(url))
        urlopen.side_effect = BadStatusLine("invalid response")
        self.assertIsNone(links.probe(url))

    def test_history_ignores_inconclusive_checks_and_drops_recovered_or_removed_urls(self):
        url = "https://example.test/source"
        pending = links.failure_history({}, {url: "HTTP 404"})
        body, opened = links.issue_body(pending)
        self.assertFalse(opened)
        self.assertNotIn(url, body)
        restored = links.issue_history({"body": body})
        self.assertEqual(links.failure_history(restored, {url: None}), pending)
        confirmed = links.failure_history(restored, {url: "HTTP 410"})
        body, opened = links.issue_body(confirmed)
        self.assertTrue(opened)
        self.assertIn(f"<{url}> (HTTP 410)", body)
        self.assertEqual(links.failure_history(confirmed, {url: ""}), {})
        self.assertEqual(links.failure_history(confirmed, {}), {})

    def test_two_runs_create_one_issue_from_artifact_history(self):
        with tempfile.TemporaryDirectory() as tmp:
            export, history = Path(tmp) / "export.json", Path(tmp) / "history.json"
            url = "https://example.test/source"
            export.write_text(json.dumps({"sources": {"url": url}, "chapter_sources": {}, "entries": []}))
            args = ["check_source_links.py", "--export", str(export), "--history", str(history)]
            environment = {"GH_TOKEN": "test", "GITHUB_REPOSITORY": "example/project"}
            with (patch.object(sys, "argv", args), patch.dict(os.environ, environment),
                  patch.object(links, "find_issue", return_value=None),
                  patch.object(links, "probe", return_value="HTTP 404"),
                  patch.object(links, "github_request") as github_request,
                  redirect_stdout(StringIO())):
                links.main()
                self.assertEqual(json.loads(history.read_text())[url]["failures"], 1)
                github_request.assert_not_called()
                links.main()
                self.assertEqual(json.loads(history.read_text())[url]["failures"], 2)
                self.assertEqual(github_request.call_args.args[2], "POST")
                github_request.assert_called_once()

    @patch.object(links, "github_request")
    def test_updates_and_reopens_one_issue(self, github_request):
        base = "https://api.github.com/repos/example/project/issues"
        url = "https://example.test/source"
        self.assertIsNone(links.publish(base, "token", None, {}))
        github_request.assert_not_called()

        pending = {url: {"failures": 1, "reason": "HTTP 404"}}
        links.publish(base, "token", None, pending)
        github_request.assert_not_called()

        confirmed = links.failure_history(pending, {url: "HTTP 404"})
        body, _ = links.issue_body(confirmed)
        links.publish(base, "token", None, confirmed)
        github_request.assert_called_once_with(base, "token", "POST", {"title": links.TITLE, "body": body})

        issue = {"number": 42, "body": body, "state": "closed"}
        github_request.reset_mock()
        links.publish(base, "token", issue, confirmed)
        github_request.assert_called_once_with(f"{base}/42", "token", "PATCH", {"body": body, "state": "open"})

        issue.update(body=body, state="open")
        github_request.reset_mock()
        links.publish(base, "token", issue, {})
        body, _ = links.issue_body({})
        github_request.assert_called_once_with(f"{base}/42", "token", "PATCH", {"body": body, "state": "closed"})
