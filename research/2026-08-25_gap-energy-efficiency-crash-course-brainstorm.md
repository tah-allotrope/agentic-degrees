---
title: "GAP Energy-Efficiency-as-a-Service Crash Course"
date: "2026-08-25"
type: "brainstorm"
depth: "standard"
source_request: "my work with gap at folder ee-heat necessitate a short course on the creation of energy efficiency crash course with combination with materials here in order to be a qualified energy efficiency as a service engineer for gap"
slug: "gap-energy-efficiency-crash-course"
---

# Brainstorm: GAP Energy-Efficiency-as-a-Service Crash Course

## Problem & Why Now

Tung (tah@allotropevc.com) owns the **energy efficiency + clean heat** workstream on
Allotrope Partners' Gap Inc. engagement (`ee-heat/activeContext.md`) — steam system
optimization, industrial heat pumps, and electric boilers for Gap's Vietnam/Indonesia
supplier base (solar/BESS/DPPA is a separate teammate's workstream). The technical
toolchain (MEASUR, REopt.jl, `heat_pump_model`, EnergyPlus, IHDA/FIED) is already
installed, localized to Vietnam, and has produced a real first finding — there is no
single breakeven COP for an industrial heat pump against coal, because Vietnam's
peak/off-peak tariff spread is 2.86x.

Separately, `agentic-degrees` is Tung's self-directed learning platform: a MIT OCW-based
dual-track EE + SE curriculum (`curriculum.json`, `teach-workspace/`) currently running
Phase 1 of a BESS/grid-EE fluency mission (Aug 17 – Oct 11, 12-14h/wk). Its lesson
format (paired `.html`/`.md`, `quiz.js`-driven retrieval questions, weekly
`learning-records/`) is a proven, working pattern for turning source material into
verified competency.

The request is to point that machinery at the GAP domain: build a short, intensive
course — reusing the teach-workspace lesson/quiz/learning-record pattern — that takes
Tung from "EE/SE fundamentals, no thermal/industrial-EE background" to "can
independently run the real GAP toolchain and reproduce a defensible technical finding,"
without waiting on a formal external credential.

## Current vs Desired State

- **Current state:**
  - `ee-heat/` (separate repo, `C:\Users\tukum\Downloads\ee-heat\`) holds a real,
    working GAP client engagement: `activeContext.md` (priority order + tool ranking +
    the VN breakeven-COP finding), `tools/README.md` (per-tool usage + localization
    caveats), `tools/measur/VN-settings-card.md`, `tools/reopt/{vn_context.json,
    make_vn_scenario.py, run_scenario.jl, garment_factory_process_heat.json,
    crosscheck_pysam.py}`, `tools/heat-pump-model/`, `tools/energyplus/`,
    `tools/reference/{Industrial-Heat-Demand-Analysis, foundational-industry-energy-data}`,
    and `research/2026-08-14_nrel-building-energy-tools.md`. No teaching/lesson
    structure exists there — it's project work product, not study material.
  - `agentic-degrees/teach-workspace/` has a working lesson pipeline (`MISSION.md`,
    `LESSON-MAP.md`, `lessons/000N-*.{html,md}`, `learning-records/`, shared
    `assets/{quiz.js,style.css}`, `tools/verify_workspace.py`) but zero thermal,
    industrial-EE, or techno-economic content — its EE track (6.01SC/6.002) is circuits
    and signals, not heat.
  - `curriculum.json` indexes MIT OCW courses only (schema: `[code, category, order,
    slug, ocw-dir-name, ""]`), tied one-to-one to downloaded OCW material in
    `mit-ocw-curriculum/`. There is no OCW course backing GAP-domain content, so this
    track cannot be expressed as a `curriculum.json` entry the way the existing tracks
    are.
  - Phase-1 BESS/grid-EE mission is live and unaffected by this request.

- **Desired state:** A new, separately-budgeted 2-week track inside `teach-workspace/`
  (own mission doc + lesson map, own lesson namespace) that takes Tung through a
  thermo/heat-transfer primer, steam systems, TEA/LCOH fundamentals, and hands-on
  lessons on all five ranked GAP tools, gated by a capstone that independently
  reproduces and extends the real Vietnam garment-factory finding (sizing the thermal
  storage that `activeContext.md` says the breakeven-COP finding calls for but hasn't
  built yet) — run as a practice copy, not committed into `ee-heat`.

- **Key repo surfaces:**
  - `agentic-degrees/teach-workspace/` — lesson/quiz/learning-record machinery to reuse.
  - `agentic-degrees/curriculum.json`, `mit-ocw-curriculum/` — OCW-only index; out of
    scope for this track (see DEC-015).
  - `ee-heat/activeContext.md`, `ee-heat/tools/README.md`, `ee-heat/tools/measur/`,
    `ee-heat/tools/reopt/`, `ee-heat/tools/heat-pump-model/`, `ee-heat/tools/energyplus/`,
    `ee-heat/tools/reference/` — the real domain material and toolchain the course is
    built on top of, referenced by path rather than copied (DEC-014).

## Resolved Decisions

- **DEC-001:** The trigger is both near-term GAP deliverable pressure and long-term
  self-sufficiency, weighted equally — not a formal-credential requirement from GAP.
- **DEC-002:** "Done" means independently reproducing a real GAP deliverable
  end-to-end (extend the Vietnam garment-factory scenario), not just passing knowledge
  checks.
- **DEC-003:** The course lives inside the existing `teach-workspace` system, reusing
  its lesson/quiz/learning-record format rather than being a standalone artifact.
- **DEC-004:** Runs in parallel with the Phase-1 BESS/grid-EE mission on a **separate**
  hours budget — does not touch that mission's schedule or gates.
- **DEC-005:** Needs a thermodynamics / heat-transfer / refrigeration-cycle primer
  before the tool-specific lessons — no prior thermal-engineering background assumed.
- **DEC-006:** Capstone extends the existing Vietnam garment-factory REopt scenario
  (`tools/reopt/garment_factory_process_heat.json`) — reproduce the breakeven-COP
  finding, then push it further by sizing the `HotThermalStorage` the finding implies
  but that hasn't been modeled yet.
- **DEC-007:** Technical competency only — no client-memo-writing/consulting-craft
  component; that's a separate skill GAP account work already exercises.
- **DEC-008:** Pace is 2 weeks, intensive.
- **DEC-009:** New lessons get their own namespace (own mission + lesson-map doc, own
  lesson-number sequence) rather than continuing the BESS/grid-EE track's global
  numbering in the shared `LESSON-MAP.md`.
- **DEC-010:** 15-20h/wk dedicated to this track for the 2 weeks (on top of the
  separate BESS-mission budget).
- **DEC-011:** All five ranked tools (MEASUR, REopt, `heat_pump_model`, EnergyPlus,
  IHDA/FIED) get hands-on lessons, not just the top-2 (MEASUR/REopt) that
  `activeContext.md`'s own fit ranking would otherwise justify prioritizing.
- **DEC-012:** Domain source material is free/public only — consistent with the
  existing `MISSION.md` "no paid tools" rule. DOE/AMO, ORNL/MEASUR docs, NREL/REopt
  docs, and the material already sitting in `ee-heat/tools/reference` and
  `ee-heat/research/` are treated as sufficient.
- **DEC-013:** Capstone work is a **practice copy**, kept out of the `ee-heat` client
  repo's git history — only promoted into `ee-heat` manually later if the result is
  genuinely deliverable-quality. Concretely: fork the scenario files under the new
  `teach-workspace/gap-ee/` track (or a scratch location), never edit
  `ee-heat/tools/reopt/*` in place for this course.
- **DEC-014:** Lessons reference `ee-heat`'s real files **by path**, not by copying
  content into `teach-workspace` — same convention the existing MIT OCW lessons
  already use for `mit-ocw-curriculum/` chapter PDFs. Keeps one source of truth; a
  lesson can go stale if `activeContext.md`/`vn_context.json` change, which is an
  accepted tradeoff for avoiding drift the other way.
- **DEC-015 (repo-derived):** `curriculum.json` is not touched — its schema is
  OCW-download-pipeline-specific (`ocw-dir-name` column) and this track has no OCW
  course backing it. The new track gets its own mission/lesson-map docs instead of a
  `curriculum.json` row.
- **DEC-016 (repo-derived):** Assessment format matches the existing lessons exactly —
  paired `.html`/`.md` lesson, `quiz.js`-driven retrieval-practice questions, one
  `learning-records/` entry per lesson (or per week) — no lighter-weight substitute,
  since the 2-week timeline doesn't strain that format.
- **DEC-017 (repo-derived):** Primary reading spine, in the order lessons will need
  it: `ee-heat/activeContext.md` → `ee-heat/tools/README.md` →
  `ee-heat/tools/measur/VN-settings-card.md` → `ee-heat/tools/reopt/vn_context.json` +
  `make_vn_scenario.py` + `run_scenario.jl` → `ee-heat/tools/heat-pump-model/` →
  `ee-heat/tools/energyplus/` → `ee-heat/tools/reference/{Industrial-Heat-Demand-Analysis,
  foundational-industry-energy-data}` → `ee-heat/research/2026-08-14_nrel-building-energy-tools.md`,
  supplemented by free DOE/ORNL/ASHRAE-adjacent fundamentals where the thermo primer
  needs source material not already present in `ee-heat`.

## Assumptions & Constraints

- **ASM-001:** No hard external GAP deadline falls inside the 2-week sprint window
  (see Open Questions Q-001) — the course is capability-building for the next work
  cycle, not racing a specific milestone.
- **ASM-002:** The new track lives at `teach-workspace/gap-ee/`, mirroring the existing
  top-level layout (`MISSION.md`, `LESSON-MAP.md`, `lessons/`, `learning-records/`) and
  reusing the shared `teach-workspace/assets/{quiz.js,style.css}` rather than
  duplicating them (see Open Questions Q-002).
- **CON-001:** Combined weekly study load during the sprint is high — 15-20h/wk for
  this track plus the existing 12-14h/wk BESS-mission budget, against `MISSION.md`'s
  own stated constraints (infant at home, morning-only reliable slot). This is a
  2-week sprint, not the whole Phase-1 duration, but it has no built-in buffer week the
  way Phase 1 does.
- **CON-002:** MEASUR stores its settings in an internal DB and cannot be scripted —
  the VN localization in `VN-settings-card.md` must be re-entered by hand each time a
  fresh MEASUR install or profile is used for a lesson.
- **CON-003:** `heat_pump_model`'s cost outputs are known-bad (negative capital cost,
  garbled units per `activeContext.md`) — any lesson using it must scope it to COP/
  refrigerant-physics verification only, never cost/LCOH output.

## Approaches Considered

- **Chosen:** New namespaced track inside `teach-workspace/`, referencing `ee-heat`
  material by path, all five tools hands-on, capped by a practice-copy capstone that
  extends the real garment-factory scenario — see DEC-001 through DEC-017.
- **ALT-001:** Fold GAP content into the existing global lesson sequence
  (`teach-workspace/lessons/0008...`) — rejected (DEC-009): mixes two missions with
  different gates and timelines into one `LESSON-MAP.md`.
- **ALT-002:** Prioritize only MEASUR + REopt (the top-2 by `activeContext.md`'s own
  fit ranking), treat the other three as reference-only — considered and offered as
  the recommended option, but explicitly rejected in favor of all-five hands-on
  (DEC-011).
- **ALT-003:** Commit capstone work directly into `ee-heat/tools/reopt/` as real
  project progress — rejected (DEC-013): keeps training iteration separate from the
  client engagement's git history; can still be promoted manually if the result turns
  out deliverable-quality.
- **ALT-004:** Copy/excerpt `ee-heat` content into `teach-workspace` for a fully
  self-contained course — rejected (DEC-014) in favor of path references, matching the
  existing OCW-lesson convention and avoiding a second copy that can drift.

## Out of Scope

- Formal/external EE certification (AEE CEM, ASHRAE, etc.) — not what "qualified"
  means here per DEC-001/DEC-002.
- Client-facing memo or deliverable-writing craft — DEC-007.
- Modifying `curriculum.json` or the OCW download pipeline — DEC-015.
- Editing anything under `ee-heat/tools/reopt/*` (or any other `ee-heat` project file)
  in place — DEC-013/DEC-014; the course only reads from `ee-heat`, never writes to it.
- Solar, BESS, solar+storage, off-site DPPA content — explicitly a teammate's
  workstream per `ee-heat/activeContext.md`.
- Re-litigating or slowing the Phase-1 BESS/grid-EE mission — DEC-004.

## Open Questions

1. **Q-001:** Is there an actual GAP deliverable deadline (in `Workplan.xlsx`, the
   CSA, or a recent check-in) that falls inside or near the 2-week sprint window and
   should size the capstone target more precisely?
   - **Recommended default:** Assume no hard deadline inside the 2 weeks; treat the
     capstone as capability-building toward the next GAP work cycle. `/plan` should
     flag this as a binding assumption a human can override once a real date is
     confirmed.
   - **Why this matters:** A real near-term deadline would change pacing, tool
     priority order (MEASUR/REopt first, others deferred), and possibly bring back
     ALT-002/ALT-003.

2. **Q-002:** Confirm `teach-workspace/gap-ee/` as the folder name/convention for the
   new track (mission doc, lesson map, lessons, learning-records), mirroring the
   existing top-level `teach-workspace/` layout.
   - **Recommended default:** `teach-workspace/gap-ee/{MISSION.md, LESSON-MAP.md,
     lessons/, learning-records/}`, reusing shared `../assets/`.
   - **Why this matters:** Determines every file path `/plan` and the implementation
     phase will write to.

3. **Q-003:** Is the 15-20h/wk (this track) + 12-14h/wk (BESS mission) ≈ 27-34h/wk
   combined load for 2 weeks actually sustainable given `MISSION.md`'s own stated
   constraints (infant at home, morning-only reliable slot, no built-in buffer inside
   a 2-week sprint)?
   - **Recommended default:** Proceed as chosen since it's bounded to 2 weeks, but if
     the sprint stalls, defer GAP-track lessons rather than cutting BESS-mission
     hours, and log a re-entry plan the same way `MISSION.md` already handles a
     stalled unit.
   - **Why this matters:** Changes whether `/plan` should build in an explicit
     lower-load fallback path from the start rather than treating it as a later
     recovery step.

## Suggested Next Step

Run `/plan gap-energy-efficiency-crash-course` to turn this into a multi-phase
implementation plan — expected to cover: scaffolding `teach-workspace/gap-ee/`
(mission doc, lesson map, shared-asset wiring); drafting the ~10-12 lesson sequence
(thermo/heat-transfer primer → refrigeration cycle/COP → steam systems → MEASUR
hands-on → TEA/LCOH fundamentals → REopt hands-on → TOU/breakeven-COP → heat-pump-model
cross-check → EnergyPlus orientation → IHDA/FIED methodology → capstone); and the
capstone build (fork the garment-factory scenario as a practice copy, size
`HotThermalStorage`, verify against `activeContext.md`'s published numbers).
