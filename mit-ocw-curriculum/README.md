# MIT OpenCourseWare — Software Engineering & Electrical Engineering Curriculum

Free, self-study degree-equivalent paths built entirely from MIT OpenCourseWare.
All materials (lecture notes, assignments, exams, solutions, code) are downloaded locally
for offline study. Lecture **videos are NOT downloaded** (too large) — each course folder has a
`videos.txt` playlist (archive.org / YouTube) you can stream, or batch-download with yt-dlp:

    yt-dlp -a <course>/videos.txt -o '<course>/videos/%(title)s.%(ext)s'

## The two tracks

- `software-engineering/` — 10 courses: CS core + software construction + systems + algorithms (≈ MIT CS degree content minus general education)
- `electrical-engineering/` — 9 courses: circuits → signals → EM → microelectronics → power systems/machines/power electronics

**19 courses, 710 material files, ~313 MB** downloaded locally (2026-08-11).

Each course folder: `lecture-notes/`, `assignments/` (+ solutions), `exams/` (+ solutions),
`readings/`, `software/`, `README.md`, `syllabus.txt`, `videos.txt`, `manifest.json`.

## Videos (YouTube, not downloaded)

Lecture videos are NOT stored locally (too large). Each `videos.txt` lists the official
MIT OCW YouTube playlists/links for that course. Stream them, or batch-download to disk:

    yt-dlp --batch-file <course>/videos.txt -o '<course>/videos/%(playlist_title)s/%(title)s.%(ext)s'

Courses whose lectures have no confirmed YouTube playlist still carry the archive.org
direct-mp4 links (same lectures, from the OCW download page) as backup in `videos.txt`.

## Recommended weekly rhythm

- ~10-15 h/week per active course; 2 courses in parallel max (one theory + one hands-on).
- For each course: (1) watch/read lecture, (2) do the assignment without looking at solutions,
  (3) only then check `assignments/solutions`, (4) before moving on, sit a past exam timed.
- Keep a progress repo (like the OSSU trackers) — public accountability beats willpower.

## Curriculum map

### Software Engineering (do in order)

| # | Course | Focus | Prereq |
|---|--------|-------|--------|
| 1 | 6.0001 Intro to CS & Programming (Python) | programming fundamentals | none |
| 2 | 6.0002 Computational Thinking & Data Science | modeling, optimization, ML basics | 6.0001 |
| 3 | 6.042J Mathematics for CS | discrete math, proofs, probability | 6.0001 |
| 4 | 6.006 Introduction to Algorithms | data structures + algorithms | 6.042J |
| 5 | 6.005 Software Construction | design, testing, concurrency in Java | 6.006 |
| 6 | 6.033 Computer System Engineering | OS, networks, distributed principles | 6.005 |
| 7 | 6.046J Design & Analysis of Algorithms | advanced algorithms, NP-completeness | 6.006 |
| 8 | 6.824 Distributed Systems | real distributed systems (labs!) | 6.033 |
| 9 | 6.045J Automata, Computability, Complexity | theory of computation | 6.042J |
| 10 | 6.851 Advanced Data Structures | research-level DS | 6.006 |

### Electrical Engineering (do in order)

| # | Course | Focus | Prereq |
|---|--------|-------|--------|
| 1 | 6.01SC Intro to EECS I | circuits + signals + systems, Python/lab | none |
| 2 | 6.002 Circuits & Electronics | circuit analysis, op-amps, MOSFETs | 6.01 / calculus |
| 3 | 6.003 Signals & Systems | LTI systems, Fourier, Laplace, z | 6.002 |
| 4 | 6.007 Electromagnetic Energy | fields, motors, optics | 6.002, physics |
| 5 | 6.012 Microelectronic Devices & Circuits | semiconductor devices, ICs | 6.002 |
| 6 | 6.061 Introduction to Electric Power Systems | power flow, transformers, grids | 6.002 |
| 7 | 6.685 Electric Machines | motors/generators, drives | 6.061 |
| 8 | 6.622 Power Electronics | converters, PWM, applications | 6.061 |
| 9 | 6.071J Electronics, Signals & Measurement | lab instrumentation, practical EE | 6.01 |

## What this does NOT include

- Accredited credential (OCW grants no degree — see research/2026-08-11_opencourseware-degrees.md)
- Graded feedback (do self-grading via solutions; consider OSSU Discord for peer review)
- Lecture videos (stream via videos.txt)
- Some courses' old 2006-2013 term versions remain the canonical OCW editions

Last updated: 2026-08-11
