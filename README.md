# Omarchy Speed Leaderboard

A record of how fast [Omarchy](https://omarchy.org/) installs: the milestones that took it from a
five-minute install to under a minute, and the fastest runs anyone has posted.

DHH called 50 seconds the "Omarchy Quattro Install World Record". This site keeps the book on it.

**Unofficial.** Not affiliated with, endorsed by, or run by DHH, Basecamp, 37signals or the Omarchy project.

## Submitting a time

Use the [Submit a run](https://github.com/mjt91/omarchy-speed-leaderboard/issues/new?template=run-submission.yml)
issue form. It asks for the time exactly as the completion screen printed it, a screenshot of that
screen, and the drive you installed to — the one spec that actually explains a fast number.

Times here are taken on trust. That screen carries no version, hardware or date, so a screenshot
proves nothing and this site does not pretend otherwise — see
[docs/adr/0002](docs/adr/0002-trust-based-verification.md).

## Working on the site

Everything lives in `data.json`. `build.py` renders it to `index.html`.

```sh
python3 build.py   # no dependencies, stdlib only
```

Open `index.html` directly, or `python3 -m http.server` for a local server.

- `data.json` — runs, milestones, baselines. The only file that changes when a record falls.
- `build.py` — the renderer.
- `assets/theme.css` — Omarchy's Tokyo Night palette and JetBrains Mono, over modest-ui.
- `assets/logo.txt` — Omarchy's own `logo.txt` (MIT), the one its installer prints.
- `vendor/` — vendored [modest-ui](https://modest-ui.com/) (npm: `mdst-ui`), MIT.
- `index.html` — generated. Rebuild rather than editing it by hand.

## Decisions

- [CONTEXT.md](CONTEXT.md) — the vocabulary this project uses, deliberately.
- [ADR 0001](docs/adr/0001-one-unclassed-all-time-record.md) — one unclassed, all-time record.
- [ADR 0002](docs/adr/0002-trust-based-verification.md) — screenshots are trusted, not verified.
- [ADR 0003](docs/adr/0003-github-issues-as-the-submission-backend.md) — GitHub Issues as the backend.
