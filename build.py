#!/usr/bin/env python3
"""Render index.html from data.json.

Deliberately dependency-free: the whole site is one data file, this script and
a vendored stylesheet. See docs/adr/0003 for why there is no backend.
"""

import html
import json
import pathlib

ROOT = pathlib.Path(__file__).parent
DATA = ROOT / "data.json"
LOGO = ROOT / "assets" / "logo.txt"
OUT = ROOT / "index.html"


def esc(value):
    return html.escape(str(value), quote=True)


def link(url, label):
    return f'<a href="{esc(url)}" rel="noopener">{esc(label)}</a>'


def gh_user(username):
    """Link a who-field to its GitHub profile when it looks like one. Anything
    that doesn't match GitHub's username rules (alnum + hyphen, 1-39 chars)
    falls back to plain text — labels like 'Anonymous' or version strings
    stay unlinked rather than 404."""
    u = (username or "").strip()
    if not u or not all(c.isalnum() or c == "-" for c in u) or not 1 <= len(u) <= 39:
        return esc(username)
    return f'<a href="https://github.com/{esc(u)}" rel="noopener">{esc(u)}</a>'


def stated(run, field):
    """Not every source gives every field. A visible gap is honest; a plausible
    guess about someone else's hardware is not."""
    value = (run.get(field) or "").strip()
    return value or None


def render_logo():
    """The same logo.txt the installer prints above the completion time (MIT,
    from omacom/omarchy). Using the real one keeps the site honest about what
    it is looking at."""
    if not LOGO.exists():
        return ""
    art = esc(LOGO.read_text().rstrip("\n"))
    return f'<pre class="logo" role="img" aria-label="Omarchy">{art}</pre>'


def render_record(run, meta):
    """The headline. One number, sourced, with whatever the source said about the
    machine that produced it — which is sometimes nothing."""
    machine = stated(run, "machine")
    hardware = ", ".join(p for p in (stated(run, "specs"), stated(run, "drive")) if p)
    who = f"<strong>{gh_user(run['who'])}</strong>"
    if machine and hardware:
        line = f"{who} on a <strong>{esc(machine)}</strong> &mdash; {esc(hardware)}"
    elif machine:
        line = f"{who} on a <strong>{esc(machine)}</strong>"
    elif hardware:
        line = f"{who} &mdash; {esc(hardware)}"
    else:
        line = f'{who} &mdash; <span class="muted">no hardware stated</span>'

    version = stated(run, "version")
    version_bit = f"Omarchy {esc(version)}" if version else '<span class="muted">version not stated</span>'

    return f"""
    <div class="record">
      <div class="record__label">Current world record</div>
      <div class="record__time">{esc(run['time'])}</div>
      <p class="record__meta">
        {line}<br>
        {version_bit} &middot; {esc(run['date'])} &middot; {link(run['source'], run['source_label'])}
      </p>
    </div>
    <p class="muted small">{esc(run['note'])}</p>
"""


def render_milestones(milestones):
    items = []
    for m in milestones:
        items.append(f"""      <li>
        <div class="timeline__when">{esc(m['date'])} &middot; Omarchy {esc(m['version'])}</div>
        <div class="timeline__head">{esc(m['headline'])}</div>
        <p class="timeline__body">{esc(m['body'])}</p>
        <p class="small muted">{link(m['source'], m['source_label'])}</p>
      </li>""")
    return '<ul class="timeline">\n' + "\n".join(items) + "\n    </ul>"


def render_runs(runs):
    rows = []
    for r in sorted(runs, key=lambda r: r["seconds"]):
        origin = "Observed in the wild" if r["origin"] == "observed" else "Submitted"
        version = esc(stated(r, "version") or "—")
        drive = esc(stated(r, "drive") or "Drive not stated")
        parts = [p for p in (stated(r, "machine"), stated(r, "specs")) if p]
        hardware = f'<br><span class="muted small">{esc(" · ".join(parts))}</span>' if parts else ""
        rows.append(f"""        <tr>
          <td class="time">{esc(r['time'])}</td>
          <td>{gh_user(r['who'])}</td>
          <td>{version}</td>
          <td>{drive}{hardware}</td>
          <td>{esc(r['date'])}</td>
          <td><span class="tag">{esc(origin)}</span><br><span class="small">{link(r['source'], r['source_label'])}</span></td>
        </tr>""")
    return """      <table>
        <thead><tr><th>Time</th><th>Who</th><th>Version</th><th>Drive &amp; machine</th><th>Date</th><th>Source</th></tr></thead>
        <tbody>
""" + "\n".join(rows) + """
        </tbody>
      </table>"""


def render_baselines(baselines):
    rows = []
    for b in baselines:
        rows.append(f"""        <tr>
          <td>{esc(b['os'])}</td>
          <td class="time">{esc(b['time'])}</td>
          <td class="muted">{esc(b['note'])} {link(b['source'], b['source_label'])}</td>
        </tr>""")
    return """      <table>
        <thead><tr><th>System</th><th>Typical install</th><th>Notes</th></tr></thead>
        <tbody>
""" + "\n".join(rows) + """
        </tbody>
      </table>"""


def build():
    data = json.loads(DATA.read_text())
    meta = data["meta"]
    record = min(data["runs"], key=lambda r: r["seconds"])

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(meta['title'])}</title>
<meta name="description" content="{esc(meta['tagline'])}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap">
<link rel="stylesheet" href="vendor/modest-ui.min.css">
<link rel="stylesheet" href="assets/theme.css">
</head>
<body class="mdst-ui">
<div class="page">

  <header>
{render_logo()}
    <h1>{esc(meta['title'])}</h1>
    <p class="subtitle">{esc(meta['tagline'])}</p>
    <p class="unaffiliated">An unofficial fan project. Not affiliated with, endorsed by, or run by
    DHH, Basecamp, 37signals or the Omarchy project. The real Omarchy is at
    {link('https://omarchy.org/', 'omarchy.org')}.</p>
  </header>

  <main>
{render_record(record, meta)}

    <h2>How it got here</h2>
    <p class="lede">Omarchy went from a five-minute install to under a minute in roughly a year. Most of that
    came from one decision: making the installer work offline, which took the network out of the equation and
    left the disk as the thing that decides your number.</p>
    {render_milestones(data['milestones'])}

    <h2>Recorded runs</h2>
    <p class="lede">One unclassed board. Faster hardware wins, and that is fine &mdash; the specs sit next to
    every time the source gave them, so you can read a number for what it is.</p>
    <div class="table-wrap">
{render_runs(data['runs'])}
    </div>

    <div class="notice">
      <h3>About the times on this page</h3>
      <p>Every time here is the number Omarchy's own installer printed on its completion screen
      &mdash; <span class="time">Installed Omarchy in {esc(record['time'])}</span> &mdash; not a stopwatch held by us or anyone else.</p>
      <p><strong>These times are taken on trust.</strong> That screen shows one line of text and nothing else:
      no version, no hardware, no date. A screenshot of it proves nothing, and we are not going to pretend
      otherwise. Versions and specs are self-reported. Runs marked <span class="tag">Observed in the wild</span>
      were collected from public posts by people who never agreed to any of this.</p>
      <p class="small">Got a faster one? {link(meta['submit_url'], 'Open an issue')} with your completion screen and your drive.</p>
    </div>

    <h2>For scale</h2>
    <p class="lede">Why any of this is worth a page. These are typical reported ranges rather than controlled
    measurements &mdash; the point is the order of magnitude, not the decimal.</p>
    <div class="table-wrap">
{render_baselines(data['baselines'])}
    </div>
  </main>

  <footer class="small muted">
    <p>An unofficial fan project. Not affiliated with, endorsed by, or run by DHH, Basecamp, 37signals or the
    Omarchy project. Omarchy is {link('https://omarchy.org/', 'omarchy.org')}.</p>
    <p>Corrections and submissions: {link(meta['repo'], 'github.com/mjt91/omarchy-speed-leaderboard')} &middot;
    Last updated {esc(meta['updated'])}</p>
  </footer>

</div>
</body>
</html>
"""
    OUT.write_text(page)
    print(f"wrote {OUT.relative_to(ROOT)} ({len(page):,} bytes) "
          f"— record {record['time']}, {len(data['runs'])} runs, {len(data['milestones'])} milestones")


if __name__ == "__main__":
    build()
