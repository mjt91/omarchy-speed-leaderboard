# Omarchy Speed Leaderboard

A public archive of how fast Omarchy installs: the milestones in its journey from minutes to seconds, and the fastest installs people have achieved.

## Language

**Omarchy**:
The Arch-based Linux distribution by DHH, maintained under the `omacom` GitHub organization. The subject of this site; not something this project builds or ships.

**Run**:
A single installation attempt whose duration is being claimed.
_Avoid_: attempt, entry, submission (a Submission is the paperwork for a Run, not the Run itself)

**Installer-Reported Time**:
The elapsed duration the Omarchy installer itself displays when installation finishes, formatted `{m}m {s}s` at whole-second resolution (so a 52-second Run reads `0m 52s`). The sole timing authority for this site: this project never defines its own start and stop points, it reads the number Omarchy already produced.
_Avoid_: wall clock, install time, elapsed time, duration

**Completion Screen**:
The installer's final screen, shown before the reboot prompt. Its entire payload is one centred line, `Installed Omarchy in {duration}`, rendered by `omarchy-install-dashboard`. It carries no version, hardware, hostname or date.
_Avoid_: finish screen, done screen, install-done

**Proof Screenshot**:
An image of a Completion Screen, submitted as the evidence for a Run. The existing community practice (people posting these at DHH, who reposts them) that this site formalises.
_Avoid_: proof, evidence, screenshot

**Submission**:
A claimed Run plus its Proof Screenshot, offered for inclusion.

**Record**:
The single fastest Installer-Reported Time ever recorded, across every Omarchy version and every machine. Unclassed: there is one Record, not one per version and not one per hardware category. DHH's own phrasing is "Omarchy Quattro Install World Record", so "world record" is the domain's language and is used freely here.
_Avoid_: best time, high score, PB

**Milestone**:
A notable moment in Omarchy's install-speed history, whether or not anyone raced for it. Release-driven engineering achievements ("Omarchy 3.0's offline ISO brought a full install to two minutes") are Milestones; a person beating a previous best is not, unless the site chooses to mark it as one.

**Baseline**:
A sourced install time for a non-Omarchy operating system, shown for contrast. Baselines exist only to convey why Omarchy's numbers are remarkable; they are never ranked against Runs and never appear on the leaderboard.
_Avoid_: comparison, competitor
