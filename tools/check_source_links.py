#!/usr/bin/env python3
"""Check the external URLs in the published source records and update one issue."""

import argparse
import base64
import json
import os
from concurrent.futures import ThreadPoolExecutor
from http.client import HTTPException
from pathlib import Path
from urllib.error import HTTPError
from urllib.parse import quote, urldefrag, urlsplit
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent.parent
TITLE = "Source link report"
HISTORY = "<!-- source-link-history\n"
USER_AGENT = "opencosmos-ai/taoteching source link check (https://github.com/opencosmos-ai/taoteching)"
URL_SYNTAX = "%:/?&=#+!$'()*+,;@~-._[]"


def source_urls(export):
    """Yield unique web URLs from resolved bibliography and citation data."""
    def collect(value):
        if isinstance(value, dict):
            for key, item in value.items():
                if key in ("url", "scan") and isinstance(item, str):
                    parts = urlsplit(item)
                    if parts.scheme in ("http", "https") and parts.netloc:
                        yield quote(urldefrag(item).url, safe=URL_SYNTAX)
                else:
                    yield from collect(item)
        elif isinstance(value, list):
            for item in value:
                yield from collect(item)

    evidence = [export["sources"], export["chapter_sources"],
                [entry["refs"] for entry in export["entries"]]]
    return sorted(set(collect(evidence)))


def probe(url):
    """Return an HTTP failure reason, an empty success, or None if inconclusive."""
    try:
        request = Request(url, headers={"User-Agent": USER_AGENT})
        with urlopen(request, timeout=10) as response:
            status = response.getcode()
    except HTTPError as exc:
        status = exc.code
        exc.close()
    except (HTTPException, OSError):
        return None
    if status is None or status in (403, 429):
        return None
    return "" if 200 <= status < 300 else f"HTTP {status}"


def failure_history(previous, observations):
    """Keep streaks only for current URLs; inconclusive probes preserve them."""
    current = {}
    for url, result in observations.items():
        prior = previous.get(url)
        if result is None and prior:
            current[url] = prior
        elif result:
            failures = min(2, 1 + (prior["failures"] if prior else 0))
            current[url] = {"failures": failures, "reason": result}
    return current


def issue_body(history):
    confirmed = [url for url, result in sorted(history.items()) if result["failures"] == 2]
    lines = ["This report is generated from the Open Tao Te Ching source registry.", ""]
    if confirmed:
        lines += ["These URLs failed two consecutive conclusive checks.", ""]
        for url in confirmed:
            lines.append(f'- <{url}> ({history[url]["reason"]})')
    else:
        lines.append("No links have two consecutive conclusive failures.")
    serialized = base64.b64encode(json.dumps(history, sort_keys=True).encode()).decode()
    lines += ["", HISTORY + serialized, "-->\n"]
    return "\n".join(lines), bool(confirmed)


def issue_history(issue):
    if not issue:
        return {}
    encoded = issue["body"].split(HISTORY, 1)[1].split("\n-->", 1)[0]
    return json.loads(base64.b64decode(encoded, validate=True))


def github_request(url, token, method="GET", payload=None):
    headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json",
               "Authorization": f"Bearer {token}"}
    data = json.dumps(payload).encode() if payload is not None else None
    if data is not None:
        headers["Content-Type"] = "application/json"
    with urlopen(Request(url, data=data, headers=headers, method=method), timeout=20) as response:
        return json.load(response)


def find_issue(base, token):
    page = 1
    while True:
        url = f"{base}?state=all&creator=github-actions%5Bbot%5D&per_page=100&page={page}"
        issues = github_request(url, token)
        for issue in issues:
            if "pull_request" not in issue and HISTORY in (issue.get("body") or ""):
                return issue
        if len(issues) < 100:
            return None
        page += 1


def publish(base, token, issue, history):
    body, has_failures = issue_body(history)
    state = "open" if has_failures else "closed"
    if not issue:
        if has_failures:
            github_request(base, token, "POST", {"title": TITLE, "body": body})
    elif issue["body"] != body or issue["state"] != state:
        github_request(f'{base}/{issue["number"]}', token, "PATCH", {"body": body, "state": state})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export", type=Path, default=ROOT / "data" / "atlas-export.json")
    parser.add_argument("--history", type=Path, required=True)
    args = parser.parse_args()
    urls = source_urls(json.loads(args.export.read_text(encoding="utf-8")))
    token = os.environ["GH_TOKEN"]
    base = f'https://api.github.com/repos/{os.environ["GITHUB_REPOSITORY"]}/issues'
    issue = find_issue(base, token)
    previous = issue_history(issue)
    if not issue and args.history.is_file():
        previous = json.loads(args.history.read_text(encoding="utf-8"))
    with ThreadPoolExecutor(max_workers=6) as pool:
        observations = dict(zip(urls, pool.map(probe, urls)))
    history = failure_history(previous, observations)
    publish(base, token, issue, history)
    args.history.parent.mkdir(parents=True, exist_ok=True)
    args.history.write_text(json.dumps(history, sort_keys=True) + "\n", encoding="utf-8")
    repeated = sum(v["failures"] == 2 for v in history.values())
    print(f"Checked {len(urls)} source URLs. {repeated} have repeated failures.")


if __name__ == "__main__":
    main()
