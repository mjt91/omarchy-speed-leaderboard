# GitHub Issues is the submission backend; the site is static

A Submission is a GitHub issue on this repo with a Proof Screenshot attached, triaged with the standard labels and, once accepted, hand-copied into a JSON data file that the static site renders. There are no user accounts, no database, no server.

## Considered Options

GitHub OAuth and full email/password accounts were both rejected. At a realistic volume of a few submissions a month, either would mean a backend, a session store, moderation tooling and a personal-data surface, for a fun project. GitHub supplies identity, image hosting, spam control, an audit trail and a moderation queue at no cost.

## Consequences

Submitters need a GitHub account — near-universal for an Arch-derivative audience, but a real barrier for anyone else. Accepted entries are copied by hand, which is fine at ten entries and would not be at a thousand; that is the signal to revisit this. The site stays deployable to GitHub Pages from the same repo that holds its submission queue.
