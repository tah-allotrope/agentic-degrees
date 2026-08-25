# NOTES — gap-ee teacher's scratchpad

> Preferences, working notes, and anything to remember when designing lessons.

## User preferences (standing)
- **English only.** All lessons, records, and explanations in English.
- **Concise** — tight bullet-point summaries; no fluff.
- **Worked numeric examples over prose** — every abstract rule gets at least one concrete
  numeric check before moving on.
- Quiz options should be roughly equal word count per question (no formatting clues).

## Workspace contract (enforced by `tools/verify_workspace.py`, run as
`python teach-workspace/tools/verify_workspace.py teach-workspace/gap-ee`)
- Lessons: `gap-ee/lessons/NNNN-<kebab-name>.html`, contiguous from 0001, each linking
  `../assets/style.css`, naming a Primary source, linking `../MISSION.md`, and containing a
  `<section class="quiz">` with `<li class="q">` + `<ul class="options"><li data-answer="true|false">`.
  Explanations go in `<p class="explain">` (revealed after answering). Each lesson also has a
  companion `.md` for terminal/pane viewing.
- Learning records: `learning-records/NNNN-<kebab-name>.md`, contiguous from 0001.
- The verifier checks whatever workspace path you pass it — always pass
  `teach-workspace/gap-ee` explicitly.

## Hard rules inherited from the plan
- `ee-heat` (`C:\Users\tukum\Downloads\ee-heat`) is a separate git repo — read-only for this
  course. Never `git add`/`git commit` inside it; never edit its files.
- All practice REopt work lives in `capstone/reopt-practice/`.
- Coal is modelled as `fuel_type: "natural_gas"` with BOTH cost and emissions overridden —
  do not "fix" this to a literal coal type (none exists).
- `heat_pump_model` is used for COP only — its cost/LCOH output is unusable.
- Money: USD unless labelled VND; FX 26,250 VND/USD; 1 MMBtu = 293.071 kWh.

## Current state (2026-08-25)
- All 5 plan phases complete: 11 lessons + 2 learning records + capstone run, verifier clean.
- Capstone outcome: physics/dispatch confirmed (COP 3.11 end-to-end, TES rides the peak);
  NPV −$388k at default costs → investment case open on supplier data. Full log in
  capstone/reopt-practice/schema-notes.md (incl. two REopt v0.61.0 upstream bugs worked around).
- No deferrals under ASM-003: the track was executed in one sitting on 2026-08-25.
