#!/usr/bin/env python3
"""build_explorer.py — the character explorer, as a self-contained page.

    python3 tools/build_explorer.py        # writes data/explorer.html

Generated from `data/taoteching.sqlite`, so it is never a second source of truth.
Everything it shows is already in the database; what it adds is the ability to
*look*, which a CSV cannot give. Clicking a component asks the reverse question —
"what else is built from this part?" — and that question is the point of having
decomposition data at all.

Self-contained by requirement: one HTML file, no external requests beyond Google
Fonts, so it can be opened from disk, published, or handed to anyone.
"""

import argparse
import json
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.corpus import ROOT  # noqa: E402

DB_PATH = ROOT / "data" / "taoteching.sqlite"
OUT = ROOT / "data" / "explorer.html"


def payload(conn):
    conn.row_factory = sqlite3.Row
    q = conn.execute

    chars = {}
    for r in q("""
        SELECT c.char, c.pinyin, c.gloss, c.gloss_source, c.our_render,
               c.lock_status, c.tier, c.centrality, c.total, c.chapters,
               c.chapter_count, c.is_function_word, c.glossary_entry,
               s.headword, s.radical, s.kind, s.fanqie, s.definition_zh,
               s.definition_en
          FROM character c LEFT JOIN shuowen s ON s.char = c.char
      ORDER BY c.total DESC"""):
        chars[r["char"]] = {
            "c": r["char"], "p": r["pinyin"], "g": r["gloss"],
            "gs": r["gloss_source"], "r": r["our_render"],
            "lock": 1 if r["lock_status"] == "locked" else 0, "tier": r["tier"],
            "cent": r["centrality"], "n": r["total"],
            "chs": [int(x) for x in (r["chapters"] or "").split(",") if x],
            "fw": r["is_function_word"], "entry": r["glossary_entry"],
            "hw": r["headword"], "rad": r["radical"], "kind": r["kind"],
            "fq": r["fanqie"], "def": r["definition_zh"],
            "defen": r["definition_en"],
            "sem": [], "pho": [],
        }
    for r in q("SELECT char, component, role FROM component ORDER BY seq"):
        if r["char"] in chars:
            chars[r["char"]]["sem" if r["role"] == "semantic" else "pho"].append(
                r["component"])

    glyphs = {r["char"]: [r["pinyin"], r["gloss"]]
              for r in q("SELECT char, pinyin, gloss FROM glyph")}

    # reverse index: component -> characters built from it
    built = {}
    for r in q("SELECT component, char, role FROM component"):
        built.setdefault(r["component"], []).append([r["char"], r["role"][0]])

    lines = {}
    for r in q("""
        SELECT l.chapter, l.seq, l.chinese, l.pinyin,
               (SELECT group_concat(v.english, ' ') FROM alignment a
                  JOIN verse_line v ON v.id = a.verse_line_id
                 WHERE a.line_id = l.id) AS eng,
               (SELECT max(a.method) FROM alignment a WHERE a.line_id = l.id) AS m
          FROM line l ORDER BY l.chapter, l.seq"""):
        lines[f"{r['chapter']}.{r['seq']}"] = [
            r["chinese"], r["pinyin"], r["eng"] or "",
            1 if r["m"] in ("authored", "exact-count") else 0]

    # One entry per LINE, not per token, with the count on it. Keyed per token,
    # a character occurring three times in one line — 聖人無常心，以百姓心為心
    # at 49.1 — produced that line three times over in the occurrence list.
    # The count is kept rather than dropped so the heat map still totals
    # occurrences, which is what it should measure, not lines touched.
    where = {}
    for r in q("""SELECT char, chapter, line_seq, count(*) AS n FROM token
                   GROUP BY char, chapter, line_seq
                   ORDER BY chapter, line_seq"""):
        where.setdefault(r["char"], []).append(
            [f"{r['chapter']}.{r['line_seq']}", r["n"]])

    # han_chars rides along so the Guodian view can compare a character's share
    # against the share of the book Guodian actually carries. Without a baseline
    # "7 of its 12 uses are attested" means nothing.
    chapters = {r["n"]: [r["hsg_title_zh"], r["hsg_title_pinyin"],
                         r["hsg_title_en"], r["guodian_attested"], r["han_chars"]]
                for r in q("SELECT n, hsg_title_zh, hsg_title_pinyin,"
                           " hsg_title_en, guodian_attested, han_chars"
                           " FROM chapter")}

    return {"chars": list(chars.values()), "glyphs": glyphs, "built": built,
            "lines": lines, "where": where, "chapters": chapters}


TEMPLATE = r"""<meta charset="utf-8">
<title>The Laozi Character Atlas</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,300;0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
:root{
  --paper:#E9E9E4; --card:#F4F4F0; --sunk:#DEDED8;
  --ink:#16171A; --ink-2:#4A4D53; --ink-3:#787C83;
  --rule:#CFCFC8;
  --sem:#B03A2E;         /* vermilion — the brush a scholar annotates with */
  --sem-rgb:176,58,46;   /* same colour, mixable — the heat map scales its alpha */
  --sem-soft:#F0DCD8;
  --pho:#5B6B7A;         /* slate — quieter, because sound carries no meaning */
  --pho-soft:#DCE2E7;
  --lock:#8A6D1F;
  --shadow:0 1px 2px rgba(20,20,24,.06),0 8px 24px -12px rgba(20,20,24,.18);
  --serif:"Spectral",Georgia,"Times New Roman",serif;
  --mono:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Menlo,monospace;
  --han:"Songti SC","Song Ti","SimSun","Noto Serif CJK SC","Noto Serif TC",
        "Hiragino Mincho ProN","Yu Mincho",serif;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --paper:#141518; --card:#1C1E22; --sunk:#0F1013;
    --ink:#E8E6E1; --ink-2:#B0B2B7; --ink-3:#83868C;
    --rule:#2B2E33;
    --sem:#E07E6C; --sem-rgb:224,126,108; --sem-soft:#3A2724;
    --pho:#93A9BC; --pho-soft:#232B33;
    --lock:#D6B25C;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px -14px rgba(0,0,0,.7);
  }
}
:root[data-theme="dark"]{
  --paper:#141518; --card:#1C1E22; --sunk:#0F1013;
  --ink:#E8E6E1; --ink-2:#B0B2B7; --ink-3:#83868C;
  --rule:#2B2E33;
  --sem:#E07E6C; --sem-rgb:224,126,108; --sem-soft:#3A2724;
  --pho:#93A9BC; --pho-soft:#232B33;
  --lock:#D6B25C;
  --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 28px -14px rgba(0,0,0,.7);
}
*{box-sizing:border-box}
body{
  margin:0;background:var(--paper);color:var(--ink);
  font-family:var(--serif);font-size:16px;line-height:1.55;
  -webkit-font-smoothing:antialiased;
}
h1,h2,h3{text-wrap:balance;margin:0;font-weight:500;letter-spacing:-.012em}
a{color:inherit}
.lab{
  font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;
  text-transform:uppercase;color:var(--ink-3);
}
.wrap{max-width:1400px;margin:0 auto;padding:0 24px 72px}

/* ---------- masthead ---------- */
header{border-bottom:1px solid var(--rule);margin-bottom:22px}
.mast{display:flex;gap:24px;align-items:flex-end;flex-wrap:wrap;
      padding:34px 0 18px}
.mast h1{font-size:clamp(28px,3.4vw,42px);line-height:1.06;font-weight:600}
.mast h1 .zh{font-family:var(--han);font-weight:500}
.mast p{margin:6px 0 0;color:var(--ink-2);max-width:60ch;font-size:15px}
.counts{margin-left:auto;display:flex;gap:22px;text-align:right}
.counts div span{display:block;font-family:var(--mono);font-size:19px;
                 color:var(--ink);font-variant-numeric:tabular-nums}

/* ---------- controls ---------- */
.controls{display:flex;gap:10px;flex-wrap:wrap;align-items:center;
          padding:0 0 18px}
input[type=search]{
  font-family:var(--serif);font-size:15px;color:var(--ink);
  background:var(--card);border:1px solid var(--rule);border-radius:2px;
  padding:8px 12px;min-width:260px;
}
input[type=search]:focus-visible,button:focus-visible,
.cell:focus-visible,.part:focus-visible{outline:2px solid var(--sem);
  outline-offset:2px}
button{
  font-family:var(--mono);font-size:11px;letter-spacing:.06em;
  text-transform:uppercase;color:var(--ink-2);cursor:pointer;
  background:transparent;border:1px solid var(--rule);border-radius:2px;
  padding:7px 11px;
}
/* Heat cells are buttons too, and these two rules would otherwise repaint their
   fill and erase the Guodian outline. Excluded explicitly rather than by
   scoping, so .more and the inline controls keep the shared button look. */
button:hover:not(.hc){color:var(--ink);border-color:var(--ink-3)}
button[aria-pressed="true"]:not(.hc){background:var(--ink);color:var(--paper);
  border-color:var(--ink)}
.spacer{flex:1}

/* ---------- two-column reading room ---------- */
.room{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,420px);gap:26px;
      align-items:start}
@media(max-width:980px){.room{grid-template-columns:1fr}}

/* ---------- the specimen index ---------- */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(58px,1fr));
      gap:1px;background:var(--rule);border:1px solid var(--rule)}
.cell{
  background:var(--card);border:0;padding:9px 4px 7px;cursor:pointer;
  display:flex;flex-direction:column;align-items:center;gap:2px;
  position:relative;transition:background .12s;
}
.cell:hover{background:var(--sunk)}
.cell[aria-current="true"]{background:var(--ink)}
.cell[aria-current="true"] .gl,
.cell[aria-current="true"] .py{color:var(--paper)}
.gl{font-family:var(--han);font-size:25px;line-height:1.15;color:var(--ink)}
.py{font-family:var(--mono);font-size:9px;color:var(--ink-3);
    max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cell.locked::after{content:"";position:absolute;top:5px;right:5px;
  width:4px;height:4px;border-radius:50%;background:var(--lock)}
.empty{padding:40px 8px;color:var(--ink-3);font-style:italic}

/* ---------- the anatomy card ---------- */
.card{background:var(--card);border:1px solid var(--rule);box-shadow:var(--shadow);
      position:sticky;top:16px;max-height:calc(100vh - 32px);overflow:auto}
.card-in{padding:22px}
.hero{display:flex;gap:18px;align-items:flex-start;
      border-bottom:1px solid var(--rule);padding-bottom:16px;margin-bottom:16px}
.hero .big{font-family:var(--han);font-size:76px;line-height:.92;color:var(--ink)}
.hero .meta{min-width:0}
.hero .meta .pin{font-family:var(--mono);font-size:14px;color:var(--sem)}
.hero .meta .gloss{font-size:19px;line-height:1.25;margin-top:2px}
.hero .meta .render{color:var(--ink-2);font-size:14px;margin-top:5px;
                    font-style:italic}
.tags{display:flex;gap:6px;flex-wrap:wrap;margin-top:9px}
.tag{font-family:var(--mono);font-size:9.5px;letter-spacing:.07em;
  text-transform:uppercase;padding:2px 6px;border:1px solid var(--rule);
  border-radius:2px;color:var(--ink-3)}
.tag.lock{color:var(--lock);border-color:var(--lock)}

section.blk{margin-top:20px}
section.blk > .lab{display:block;margin-bottom:8px;
  border-bottom:1px solid var(--rule);padding-bottom:5px}

/* parts */
.parts{display:flex;flex-wrap:wrap;gap:8px;align-items:stretch}
.part{
  display:flex;gap:9px;align-items:center;cursor:pointer;text-align:left;
  border:1px solid var(--rule);border-radius:2px;padding:7px 10px 7px 8px;
  background:transparent;flex:1 1 168px;min-width:0;
}
.part:hover{border-color:var(--ink-3)}
.part .pg{font-family:var(--han);font-size:27px;line-height:1;flex:none}
.part .pt{min-width:0}
.part .pt b{display:block;font-family:var(--mono);font-size:10.5px;
  font-weight:500;letter-spacing:.02em}
.part .pt span{display:block;font-size:13px;line-height:1.3;color:var(--ink-2);
  overflow:hidden;text-overflow:ellipsis}
.part.sem{background:var(--sem-soft);border-color:transparent}
.part.sem .pg,.part.sem .pt b{color:var(--sem)}
.part.pho{background:var(--pho-soft);border-color:transparent}
.part.pho .pg,.part.pho .pt b{color:var(--pho)}
.legend{font-size:13px;color:var(--ink-2);margin:9px 0 0;line-height:1.45}
.legend em{color:var(--sem);font-style:normal}
.legend strong{color:var(--pho);font-weight:400}

.swz{font-family:var(--han);font-size:16px;line-height:1.7;color:var(--ink);
     background:var(--sunk);padding:11px 13px;border-left:2px solid var(--sem)}
.swen{font-size:14px;color:var(--ink-2);margin:8px 0 0;line-height:1.5;
      font-style:italic}
.note{font-size:12.5px;color:var(--ink-3);margin-top:7px;line-height:1.45}

/* The book is 81 chapters, so the map is 9×9 and always complete. Showing only
   the chapters a character reaches hides the more telling half — where it does
   not go. Absence has a shape, and it is only visible against a constant frame. */
.heat{display:grid;grid-template-columns:repeat(9,1fr);gap:3px;margin-top:2px}
.hc{
  aspect-ratio:1;border:1px solid transparent;border-radius:2px;padding:0;
  background:var(--sunk);cursor:pointer;
  font-family:var(--mono);font-size:9.5px;font-variant-numeric:tabular-nums;
  color:var(--ink-3);display:flex;align-items:center;justify-content:center;
  transition:transform .1s;
}
.hc:hover{transform:scale(1.14)}
/* A chapter the character never reaches is not a control. It stayed a button so
   its tooltip still names the chapter, but nothing about it should promise a
   click that does nothing. */
.hc.void{cursor:default}
.hc.void:hover{transform:none}
.hc.gd{border-color:var(--pho)}
.hc.faded{opacity:.22}
.hc[aria-pressed="true"]{outline:2px solid var(--ink);outline-offset:1px;
  color:var(--ink)}
.hc:focus-visible{outline:2px solid var(--sem);outline-offset:1px}
.hkey{display:flex;align-items:center;gap:7px;margin-top:10px;flex-wrap:wrap}
.hramp{display:flex;gap:2px}
.hramp i{width:15px;height:11px;border-radius:1px;display:block}
.hkey .lab{white-space:nowrap}


.occ{display:flex;flex-direction:column;gap:12px}
.oc{border-top:1px solid var(--rule);padding-top:10px}
.oc:first-child{border-top:0;padding-top:0}
.oc .ref{font-family:var(--mono);font-size:10px;color:var(--ink-3);
  letter-spacing:.05em;display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
.oc .times{color:var(--sem);letter-spacing:.03em}
.oc .zh{font-family:var(--han);font-size:17px;line-height:1.6;margin-top:3px}
.oc .zh mark{background:var(--sem-soft);color:var(--sem);
  border-radius:2px;padding:0 1px}
.oc .py2{font-family:var(--mono);font-size:11px;color:var(--ink-3);
  margin-top:2px;line-height:1.45}
.oc .en{font-size:14.5px;color:var(--ink-2);margin-top:5px;line-height:1.45}
.oc .approx{font-family:var(--mono);font-size:9.5px;color:var(--ink-3);
  letter-spacing:.05em}
.more{margin-top:10px}

footer{border-top:1px solid var(--rule);margin-top:40px;padding-top:18px;
  color:var(--ink-3);font-size:13px;line-height:1.6;max-width:78ch}
footer b{color:var(--ink-2);font-weight:500}
footer .zh{font-family:var(--han)}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>

<div class="wrap">
<header>
  <div class="mast">
    <div>
      <h1>Inside the characters of the <span class="zh">道德經</span></h1>
      <p>Every character in the Tao Te Ching, taken apart into the pieces it is
      built from — with what each piece means, where the character appears, and
      how this translation renders it. No Chinese required.</p>
    </div>
    <div class="counts">
      <div><span id="k-ch">—</span><div class="lab">characters</div></div>
      <div><span id="k-oc">—</span><div class="lab">occurrences</div></div>
      <div><span id="k-pt">—</span><div class="lab">parts</div></div>
    </div>
  </div>
</header>

<div class="controls">
  <input type="search" id="q" placeholder="Search a character, sound, or meaning"
         aria-label="Search characters">
  <button id="f-lock" aria-pressed="false">Settled terms</button>
  <button id="f-real" aria-pressed="true">Hide grammar</button>
  <button id="s-freq" aria-pressed="true">By frequency</button>
  <button id="s-cent" aria-pressed="false">By reach</button>
  <span class="spacer"></span>
  <button id="clear" hidden>Clear filter</button>
</div>

<div class="room">
  <div>
    <div class="lab" id="status" style="padding-bottom:8px"></div>
    <div class="grid" id="grid"></div>
  </div>
  <aside class="card"><div class="card-in" id="card"></div></aside>
</div>

<footer>
  <p><b>How to read this.</b> A Chinese character is usually built from parts, and
  the parts do two different jobs. A <em style="color:var(--sem);font-style:normal">semantic</em>
  part carries meaning. A <strong style="color:var(--pho);font-weight:400">phonetic</strong>
  part was borrowed for its sound alone and means nothing here — which is why the
  two are coloured differently and never merged.</p>
  <p><b>Where the analysis comes from.</b> <span class="zh">說文解字</span>
  (<i>Shuōwén Jiězì</i>), c. 100 CE — the earliest systematic account of how
  Chinese characters are built. It states each character's parts in its own
  words, so the semantic/phonetic split is the source's, not ours. A modern
  radical is a filing system; this is an analysis.</p>
  <p><b>What is ours, and what is not.</b> The Chinese is public domain by age.
  The English glosses, the translation, and the settled renderings are by Shalom
  Ormsby and are dedicated <b>CC0</b> — no rights reserved. <span class="zh">說文</span>'s
  definitions are never machine-rendered: an English line appears only where a
  glossary entry has researched the character and translated it by hand. Component
  glosses cover the common parts and the rest are marked as gaps, not guessed.</p>
</footer>
</div>

<script id="data" type="application/json">__DATA__</script>
<script>
const D = JSON.parse(document.getElementById('data').textContent);
const CH = D.chars, G = D.glyphs, BUILT = D.built, LN = D.lines,
      WH = D.where, CHAP = D.chapters;
const byChar = Object.fromEntries(CH.map(c => [c.c, c]));

const el = id => document.getElementById(id);
const grid = el('grid'), card = el('card'), status = el('status');
let sel = null, filter = {q:'', lock:false, real:true, comp:null}, sort = 'freq';
let occLimit = 6, chapFilter = null, gdOn = false;

el('k-ch').textContent = CH.length;
el('k-oc').textContent = CH.reduce((a,c)=>a+c.n,0).toLocaleString();
el('k-pt').textContent = Object.keys(BUILT).length;

function esc(s){ return (s||'').replace(/[&<>"]/g, m =>
  ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[m])); }

function visible(){
  let out = CH.slice();
  if (filter.comp) {
    const set = new Set((BUILT[filter.comp]||[]).map(x=>x[0]));
    out = out.filter(c => set.has(c.c));
  }
  if (filter.lock) out = out.filter(c => c.lock);
  if (filter.real) out = out.filter(c => !c.fw);
  const q = filter.q.trim().toLowerCase();
  if (q) out = out.filter(c =>
    c.c.includes(q) ||
    (c.p||'').toLowerCase().includes(q) ||
    (c.g||'').toLowerCase().includes(q) ||
    (c.r||'').toLowerCase().includes(q));
  out.sort(sort === 'cent' ? (a,b)=>b.cent-a.cent : (a,b)=>b.n-a.n);
  return out;
}

function draw(){
  const list = visible();
  grid.innerHTML = '';
  if (!list.length){
    grid.innerHTML = '<p class="empty" style="grid-column:1/-1">' +
      'Nothing matches. Try a different word, or clear the filter.</p>';
  }
  const frag = document.createDocumentFragment();
  for (const c of list){
    const b = document.createElement('button');
    b.className = 'cell' + (c.lock ? ' locked' : '');
    b.type = 'button';
    b.setAttribute('aria-current', sel === c.c ? 'true' : 'false');
    b.title = `${c.c} ${c.p||''} — ${c.g||'not yet glossed'} · ${c.n}×`;
    b.innerHTML = `<span class="gl">${esc(c.c)}</span>` +
                  `<span class="py">${esc(c.p||'')}</span>`;
    b.onclick = () => { sel = c.c; occLimit = 6; chapFilter = null;
                        draw(); show(c.c); };
    frag.appendChild(b);
  }
  grid.appendChild(frag);

  let s = `${list.length} of ${CH.length} characters`;
  if (filter.comp){
    const g = G[filter.comp] || [];
    s += ` built from ${filter.comp}` + (g[1] ? ` (${g[1]})` : '');
  }
  status.textContent = s;
  el('clear').hidden = !filter.comp;
}

function partBtn(ch, role){
  const g = G[ch] || [null,null];
  const known = !!g[1];
  const meaning = role === 'sem'
    ? (g[1] || 'not yet glossed')
    : 'sound only — carries no meaning here';
  return `<button class="part ${role}" type="button" data-comp="${esc(ch)}"
      title="Show every character built from ${esc(ch)}">
      <span class="pg">${esc(ch)}</span>
      <span class="pt"><b>${esc(g[0] || '?')}</b>
      <span${known||role==='pho'?'':' style="opacity:.7;font-style:italic"'}>${esc(meaning)}</span></span>
    </button>`;
}

function show(chr){
  const c = byChar[chr];
  if (!c){ card.innerHTML = ''; return; }
  const tags = [];
  if (c.lock) tags.push('<span class="tag lock">settled rendering</span>');
  if (c.tier) tags.push(`<span class="tag">${esc(c.tier)}</span>`);
  if (c.kind) tags.push(`<span class="tag">${esc(c.kind.replace(/-/g,' '))}</span>`);
  if (c.rad) tags.push(`<span class="tag">filed under ${esc(c.rad)}</span>`);

  let h = `<div class="hero">
      <div class="big">${esc(c.c)}</div>
      <div class="meta">
        <div class="pin">${esc(c.p||'')}</div>
        <div class="gloss">${esc(c.g || 'not yet glossed')}</div>
        ${c.r && c.r !== c.g ? `<div class="render">rendered “${esc(c.r)}”</div>`:''}
        <div class="tags">${tags.join('')}</div>
      </div>
    </div>`;

  if (c.sem.length || c.pho.length){
    h += `<section class="blk"><span class="lab">Built from</span>
      <div class="parts">
        ${c.sem.map(x => partBtn(x,'sem')).join('')}
        ${c.pho.map(x => partBtn(x,'pho')).join('')}
      </div>`;
    if (c.pho.length && c.sem.length)
      h += `<p class="legend"><em>Vermilion</em> parts carry meaning.
            <strong>Slate</strong> parts were borrowed for sound alone.</p>`;
    else if (c.pho.length)
      h += `<p class="legend"><strong>Slate</strong> parts were borrowed for
            sound alone and mean nothing here.</p>`;
    h += `</section>`;
  } else if (c.kind === 'pictograph'){
    h += `<section class="blk"><span class="lab">Built from</span>
      <p class="legend">Nothing — this one is a picture, not an assembly.</p>
      </section>`;
  }

  if (c.def){
    h += `<section class="blk"><span class="lab">說文解字 · c. 100 CE</span>
      <div class="swz">${esc(c.def)}</div>`;
    // The English is hand-made, from the character's glossary entry; where no
    // entry has translated it yet, the Chinese stands alone.
    if (c.defen) h += `<p class="swen">${esc(c.defen)}</p>`;
    const facts = (c.hw && c.hw !== c.c
        ? `Filed under the older graph ${esc(c.hw)}. ` : '') +
      (c.fq ? `Middle Chinese spelling ${esc(c.fq)}.` : '');
    if (facts) h += `<p class="note">${facts.trim()}</p>`;
    h += `</section>`;
  }

  const occ = WH[c.c] || [];              // [[ "49.1", 3 ], …] — one per line
  const per = new Array(82).fill(0);
  for (const [k, n] of occ) per[+k.split('.')[0]] += n;
  const peak = Math.max(1, ...per);

  // Scaled against this character's own peak, not the book's. The question the
  // map answers is where *this* character concentrates; a global scale would
  // flatten every term that is not 道 into an even wash. The legend states the
  // peak so the shading is never mistaken for an absolute count.
  const shade = n => n === 0 ? 0 : 0.18 + 0.82 * (n / peak);

  // The Guodian view is a second variable, and it is only worth showing in
  // interaction with the first: does this character live in the part of the book
  // the oldest witness carries, or only outside it? Off by default — a persistent
  // outline on chapters where the character never appears is noise in exactly the
  // cases where it is least informative.
  let gdChars = 0, allChars = 0, gdUses = 0;
  for (let n = 1; n <= 81; n++){
    const meta = CHAP[n] || [], size = meta[4] || 0;
    allChars += size;
    if (meta[3]){ gdChars += size; gdUses += per[n]; }
  }
  const gdShare = allChars ? Math.round(100 * gdChars / allChars) : 0;
  const useShare = c.n ? Math.round(100 * gdUses / c.n) : 0;

  h += `<section class="blk">
    <span class="lab" style="display:flex;justify-content:space-between;
      align-items:center;gap:10px">Where it appears
      <button id="gdtog" type="button" aria-pressed="${gdOn}"
        title="Guodian, c. 300 BCE \u2014 the oldest surviving copy of this text. A witness is a copy that testifies to what the text said at some point; it is not a source the text came from."
        style="padding:3px 8px;font-size:9.5px">Oldest witness</button></span>
    <p class="legend" style="margin:0 0 10px">${c.n}&times;
      across ${c.chs.length} of 81 chapters${
        peak > 1 ? `, most often in chapter ${per.indexOf(peak)} (${peak}&times;)` : ''}</p>
    <div class="heat">`;
  for (let n = 1; n <= 81; n++){
    const k = per[n], a = shade(k), gd = CHAP[n] && CHAP[n][3];
    const strong = a > .55;
    const title = `Chapter ${n}${CHAP[n]&&CHAP[n][2] ? ' \u2014 '+CHAP[n][2] : ''}` +
      ` \u00b7 ${k === 0 ? 'does not appear' : k + (k===1?' time':' times')}` +
      (gdOn ? (gd ? ' \u00b7 in Guodian, c. 300 BCE'
                  : ' \u00b7 not in Guodian') : '');
    const cls = 'hc' + (k ? '' : ' void') +
      (gdOn && gd ? ' gd' : '') + (gdOn && !gd ? ' faded' : '');
    h += `<button class="${cls}" type="button" data-ch="${n}"
      ${k ? '' : 'tabindex="-1" aria-disabled="true"'}
      aria-pressed="${chapFilter === n}"
      style="background:${k ? `rgba(var(--sem-rgb),${a.toFixed(3)})` : 'var(--sunk)'};${
        strong ? 'color:#fff;' : ''}"
      title="${esc(title)}">${n}</button>`;
  }
  h += `</div>
    <div class="hkey">
      <span class="lab">none</span>
      <span class="hramp">${[0,.25,.5,.75,1].map(t =>
        `<i style="background:${t ? `rgba(var(--sem-rgb),${(0.18+0.82*t).toFixed(2)})`
          : 'var(--sunk)'}"></i>`).join('')}</span>
      <span class="lab">${peak}&times; in one chapter</span>
    </div>`;
  if (!gdOn)
    h += `<p class="legend" style="font-size:12.5px;margin-top:8px">
      All 81 chapters are shown, so the gaps count too. Deeper red means more
      uses of ${esc(c.c)} there. Click a chapter to read only its lines.</p>`;
  else
    h += `<p class="legend" style="font-size:12.5px;margin-top:8px">
      Faded chapters are missing from <b>Guodian</b> (c. 300 BCE) &mdash; bamboo
      slips dug up in 1993, the oldest surviving copy of this text. It is a
      <i>witness</i>, not a source: it testifies to what the text said, but the
      later text does not descend from it. It carries 31 of the 81 chapters and
      ${gdShare}% of the book&rsquo;s characters.
      <b>${gdUses} of ${esc(c.c)}&rsquo;s ${c.n} uses &mdash; ${useShare}% &mdash;
      fall inside it.</b>
      ${c.n < 10
        ? `Too few uses to read anything into that. With ${c.n}, a split this far
           from ${gdShare}% is ordinary chance.`
        : useShare === 0
        ? `Absent from the oldest witness entirely &mdash; across ${c.n} uses that
           is unlikely to be chance, and worth asking whether ${esc(c.c)} belongs
           to a later layer.`
        : Math.abs(useShare - gdShare) < 10
        ? `Within range of the ${gdShare}% an even spread would give, so this says
           nothing either way.`
        : useShare < gdShare
        ? `Below the ${gdShare}% an even spread would give: it leans toward the
           chapters the oldest witness lacks.`
        : `Above the ${gdShare}% an even spread would give: it leans toward the
           oldest stratum.`}
      Weak evidence at best. Guodian is a selection, not an earlier edition, and
      absence from it is not proof of lateness &mdash; see
      <code>sources/PROVENANCE.md</code>.</p>`;
  h += `    </section>`;

  const shown = chapFilter
    ? occ.filter(e => +e[0].split('.')[0] === chapFilter) : occ;
  const nLines = shown.length;
  h += `<section class="blk"><span class="lab">In the text</span>`;
  if (chapFilter)
    h += `<p class="legend" style="margin:0 0 9px">Chapter ${chapFilter} only —
      <button id="allch" type="button" style="padding:2px 7px">show all
      ${occ.length} lines</button></p>`;
  h += `<div class="occ">`;
  for (const [key, times] of shown.slice(0, occLimit)){
    const L = LN[key]; if (!L) continue;
    const [ch, seq] = key.split('.');
    const zh = esc(L[0]).replace(new RegExp(esc(c.c),'g'), m=>`<mark>${m}</mark>`);
    h += `<div class="oc">
      <div class="ref">CH ${ch} · LINE ${seq}${
        times > 1 ? `<span class="times">${times}× in this line</span>` : ''}</div>
      <div class="zh">${zh}</div>
      <div class="py2">${esc(L[1]||'')}</div>
      <div class="en">${esc(L[2] || '—')}</div>
      ${L[3] ? '' : '<div class="approx">line pairing approximate</div>'}
    </div>`;
  }
  h += `</div>`;
  if (nLines > occLimit)
    h += `<button class="more" id="more" type="button">Show more
          (${nLines - occLimit} more line${nLines - occLimit === 1 ? '' : 's'})</button>`;
  h += `</section>`;

  if (c.entry)
    h += `<section class="blk"><span class="lab">Full entry</span>
      <p class="legend">This character has a written glossary entry:
      <code style="font-family:var(--mono);font-size:12.5px">${esc(c.entry)}</code></p>
      </section>`;

  card.innerHTML = h;
  card.querySelectorAll('[data-comp]').forEach(b => b.onclick = () => {
    filter.comp = b.dataset.comp; filter.q = ''; el('q').value = '';
    filter.real = false; el('f-real').setAttribute('aria-pressed','false');
    draw(); window.scrollTo({top:0, behavior:'smooth'});
  });
  card.querySelectorAll('[data-ch]').forEach(b => b.onclick = () => {
    const n = +b.dataset.ch;
    // A chapter the character never reaches has nothing to filter to.
    if (!per[n]) return;
    chapFilter = chapFilter === n ? null : n;
    occLimit = 6;
    show(chr);
  });
  const g = el('gdtog');
  if (g) g.onclick = () => { gdOn = !gdOn; show(chr); };
  const a = el('allch');
  if (a) a.onclick = () => { chapFilter = null; occLimit = 6; show(chr); };
  const m = el('more');
  if (m) m.onclick = () => { occLimit += 12; show(chr); };
}

el('q').oninput = e => { filter.q = e.target.value; draw(); };
function toggle(id, key){
  el(id).onclick = () => {
    filter[key] = !filter[key];
    el(id).setAttribute('aria-pressed', String(filter[key]));
    draw();
  };
}
toggle('f-lock','lock'); toggle('f-real','real');
el('s-freq').onclick = () => { sort='freq';
  el('s-freq').setAttribute('aria-pressed','true');
  el('s-cent').setAttribute('aria-pressed','false'); draw(); };
el('s-cent').onclick = () => { sort='cent';
  el('s-cent').setAttribute('aria-pressed','true');
  el('s-freq').setAttribute('aria-pressed','false'); draw(); };
el('clear').onclick = () => { filter.comp=null; draw(); };

sel = '道';
draw();
show('道');
</script>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--db", default=str(DB_PATH))
    ap.add_argument("-o", "--out", default=str(OUT))
    args = ap.parse_args()

    db = Path(args.db)
    if not db.exists():
        print(f"  no database at {db} — run: python3 tools/build_db.py")
        return 2

    conn = sqlite3.connect(db)
    data = payload(conn)
    conn.close()

    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    # </script> inside a JSON island would close the block early.
    blob = blob.replace("</", "<\\/")
    html = TEMPLATE.replace("__DATA__", blob)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")

    unglossed = sum(1 for c in data["chars"] if not c["g"])
    print(f"  characters          {len(data['chars'])}")
    print(f"  distinct parts      {len(data['built'])}")
    print(f"  lines               {len(data['lines'])}")
    print(f"  without a gloss     {unglossed}")
    print(f"  page size           {len(html) / 1024:.0f} KB")
    print(f"\n  → {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
