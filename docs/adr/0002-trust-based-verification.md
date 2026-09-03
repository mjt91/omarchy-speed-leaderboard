# Proof Screenshots are trusted, not verified

A Proof Screenshot cannot establish anything. The Completion Screen rendered by `omarchy-install-dashboard` contains exactly one line — `Installed Omarchy in {duration}` — with no version, hostname, hardware, date or any other anchor, so it is forgeable in seconds by typing the string into a terminal. We accept submissions on trust anyway, and say so plainly on the site.

## Considered Options

Requiring uncut video is the only mechanism that would actually establish a time, and was rejected: it is a heavy ask for a site with no traffic, and would reduce the submission rate to roughly zero. Optional corroborating artifacts (`omarchy-disk-speedtest` output, an `omarchy-version` string) earning a "corroborated" badge were considered and dropped to keep the project simple.

## Consequences

Automated screenshot validation is pointless as fraud protection — OCR can confirm the string's format, and would pass a forgery perfectly — so it is not built. The Omarchy version of a Run is self-reported, because the screen does not carry it. The site's credibility rests on stating its own limits rather than on the evidence.
