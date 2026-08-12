# NOTES — teacher's scratchpad

> Preferences, working notes, and anything to remember when designing lessons.

## User preferences (standing)
- **English only.** All lessons, records, and explanations in English.
- **Videos: YouTube streaming only** via videos.txt links — never download.
- **Concise** — the user prefers tight bullet-point summaries; no fluff.
- **Worked numeric examples over prose** — every abstract rule gets at least one concrete
  numeric check before moving on.
- **Session pattern:** 4-5 weekday mornings (~60-75 min, reliable slot; evenings volatile) +
  one weekend block (~2-4h); ~12-14h/wk total, ~60/40 EE/SE. Weekly 30-45 min agent session.
- **Commit+push after every agent session** (weekly cadence, DEC-010).
- **Curriculum tree is read-only:** never write into `mit-ocw-curriculum/`; extract zips into
  `teach-workspace/work/<course>/` (e.g. `work/6.01SC/`).
- Quiz options must be **equal word count** per question (no formatting clues).

## Workspace contract (enforced by `tools/verify_workspace.py`)
- Lessons: `lessons/NNNN-<kebab-name>.html`, contiguous from 0001, each linking
  `../assets/style.css`, naming a Primary source, linking `../MISSION.md`, and containing a
  `<section class="quiz">` with `<li class="q">` + `<ul class="options"><li data-answer="true|false">`.
  Explanations go in `<p class="explain">` (revealed after answering).
- Learning records: `learning-records/NNNN-<kebab-name>.md`, contiguous from 0001.
- Lesson numbers are assigned at authoring time as `max(existing) + 1`; study order lives in
  LESSON-MAP.md.

## Current state (2026-08-12)
- Phase 0 scaffold done (merged from two concurrent sessions — see git history). Week 1 in
  progress: Python diagnostic (0002) + primer (0001), 6.01SC Unit 1 state machines (0003).
  6.01SC Unit 2 (signals & systems, chap05) queued next per LESSON-MAP.md.
- Python baseline: **rusty** — needs the 6.0001-primer before 6.0002 (DEC-015).
- Baby (b. May 2026) — sleep volatility; wk 6 is buffer; **defer, don't quit**.

## Teaching style notes
- Ground every lesson in the mission (BESS/grid/machines + data work) — make the EE payoff
  visible early (state machines → battery controller logic, etc.).
- Small lessons, one tangible win each. Knowledge first, then interactive practice.
- Lead lessons with retrieval checks; close with a quiz + primary source + follow-up prompt.
- Interleave EE/SE practice across the week, not within a single lesson.
