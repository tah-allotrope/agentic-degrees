---
title: "GAP Energy-Efficiency-as-a-Service Crash Course"
date: "2026-08-25"
status: "draft"
request: "bsaed on brainstorm"
plan_type: "multi-phase"
research_inputs:
  - "research/2026-08-25_gap-energy-efficiency-crash-course-brainstorm.md"
---

# Plan: GAP Energy-Efficiency-as-a-Service Crash Course

## Objective
Build a self-contained, 2-week, 11-lesson crash-course track inside this repo's
`teach-workspace/` — reusing its existing lesson/quiz/learning-record machinery —
that takes the learner from "EE/SE fundamentals, no thermal-engineering background"
to "can independently operate the real Gap Inc. clean-heat toolchain (MEASUR, REopt.jl,
`heat_pump_model`, EnergyPlus, IHDA/FIED) and reproduce a defensible technical finding,"
gated by a capstone that extends a real Gap Inc. finding (industrial heat-pump +
thermal-storage sizing) as an isolated practice exercise, never touching the live
client repository.

## Context Snapshot
- **Current state:** `teach-workspace/` (this repo, `agentic-degrees`) has a working,
  verifier-enforced lesson pipeline — paired `lessons/NNNN-slug.{html,md}` files, a
  shared vanilla-JS quiz engine (`assets/quiz.js`), `learning-records/`, and
  `tools/verify_workspace.py` — but zero thermal, industrial-EE, steam-system, or
  techno-economic content; its existing EE content (6.01SC/6.002) is circuits and
  signals. A separate local repository, `ee-heat` (`C:\Users\tukum\Downloads\ee-heat`,
  its own independent git repo, not a subdirectory of this one), holds the real,
  currently-active Gap Inc. energy-efficiency/clean-heat engagement: an installed and
  Vietnam-localized toolchain (MEASUR v1.8.3, REopt.jl, `heat_pump_model`,
  EnergyPlus v26.1.0, and two US-methodology reference repos) plus a real finding
  already produced and documented in `ee-heat/activeContext.md` and
  `ee-heat/tools/README.md`: Vietnam's peak/off-peak electricity tariff spread (2.86x)
  means there is no single breakeven COP for an industrial heat pump against a
  coal-fired steam boiler — it ranges from 1.88 (off-peak) to 5.37 (peak) — so the
  design answer is "heat pump plus thermal storage," a thermal-storage sizing exercise
  that has **not yet been built** in `ee-heat`'s REopt scenario.
- **Desired state:** A new `teach-workspace/gap-ee/` track exists, structurally
  identical to `teach-workspace/` itself (own `MISSION.md`, `GLOSSARY.md`,
  `RESOURCES.md`, `NOTES.md`, `PROGRESS.md`, `LESSON-MAP.md`, `assets/`, `lessons/`,
  `learning-records/`), passing `python teach-workspace/tools/verify_workspace.py
  teach-workspace/gap-ee` with zero problems, containing 11 lessons (numbered
  0001–0011, contiguous) that move from thermodynamics fundamentals through
  hands-on use of all five ranked `ee-heat` tools to a capstone that independently
  reproduces `ee-heat/activeContext.md`'s breakeven-COP finding and extends it by
  sizing an `ASHPWaterHeater` + `HotThermalStorage` pair in REopt.jl — done entirely
  inside a practice copy under `teach-workspace/gap-ee/capstone/reopt-practice/`, with
  the live `ee-heat` repository never modified.
- **Key repo surfaces:**
  - `agentic-degrees/teach-workspace/` (existing lesson/quiz/verify machinery to
    reuse, read-only reference for format).
  - `agentic-degrees/teach-workspace/gap-ee/` (everything this plan creates).
  - `agentic-degrees/curriculum.json`, `agentic-degrees/mit-ocw-curriculum/`
    (untouched — OCW-index-only, out of scope).
  - `ee-heat/activeContext.md`, `ee-heat/tools/README.md`,
    `ee-heat/tools/measur/VN-settings-card.md`, `ee-heat/tools/reopt/{vn_context.json,
    make_vn_scenario.py, run_scenario.jl, Project.toml, Manifest.toml,
    garment_factory_process_heat.json}`, `ee-heat/tools/heat-pump-model/`,
    `ee-heat/tools/energyplus/`, `ee-heat/tools/reference/` — read as reference
    material and, for REopt, copied once into a practice directory; never edited in
    place.
- **Out of scope:** Editing `curriculum.json` or `mit-ocw-curriculum/`; any file under
  `ee-heat/gap/` or `ee-heat/data/` (both are confidential client material per
  `ee-heat/.gitignore` and are not needed for this course); writing to, committing
  in, or running `git add`/`git commit` inside the `ee-heat` repository at any point;
  client-facing memo/deliverable-writing craft; solar, BESS, or DPPA content; changes
  to the existing BESS/grid-EE Phase-1 mission's schedule, hours budget, or files.

## Environment & Conventions
- **Stack:** Static HTML/Markdown lesson pairs + a dependency-free vanilla-JS quiz
  engine (no build step, no package manager for `teach-workspace/` itself). Python
  3.11 (standard library only) runs `teach-workspace/tools/verify_workspace.py`. For
  the capstone: Julia 1.10.10 with `REopt`, `JuMP`, `HiGHS`, `JSON` (already installed
  in the user's global Julia package depot — confirmed via `julia --version` →
  `julia version 1.10.10`, and `ee-heat/tools/reopt/Project.toml` lists exactly these
  four `[deps]`), plus Python (`ee-heat/tools/.venv/Scripts/python.exe`) for
  `make_vn_scenario.py`.
- **Setup:** No install needed for `teach-workspace/gap-ee/` itself (static content).
  For the capstone's REopt practice copy: after copying the files (Phase 3, Task
  03-05), run `julia --project=. -e "using Pkg; Pkg.instantiate()"` from inside
  `teach-workspace/gap-ee/capstone/reopt-practice/` once.
- **Build / Run:** No build step for lessons. To view a lesson locally, open its
  `.html` file directly in a browser (`file://` URL) — this is how existing lessons
  in `teach-workspace/lessons/` are already viewed; there is no dev server in this
  repo.
- **Test:** Full-suite structural check (run after every phase that adds files):
  ```
  python teach-workspace/tools/verify_workspace.py teach-workspace/gap-ee
  ```
  Expected clean-pass output format: `OK: <N> lessons, <M> records, 0 problems`. There
  is no single-lesson-only invocation — the script always scans the whole workspace
  argument you pass it, so passing `teach-workspace/gap-ee` scopes it to only this
  track (it does **not** also re-check `teach-workspace/`'s own BESS-mission lessons,
  since numbering/required-file checks are relative to the workspace argument).
- **Conventions & traps:**
  - Lesson files: `teach-workspace/gap-ee/lessons/NNNN-kebab-slug.html` (+ a
    companion `.md` for terminal/pane viewing, matching existing lessons 0004–0007),
    numbers contiguous from `0001`, zero-padded to 4 digits.
  - Every lesson `.html` MUST contain, verbatim: `href="../assets/style.css"` (style
    link), `href="../MISSION.md"` (mission link — resolves to
    `teach-workspace/gap-ee/MISSION.md`), the literal text `Primary source`, and a
    `<section class="quiz">` block.
  - Quiz markup contract (enforced by `assets/quiz.js`, not by the verifier, but
    required for the quiz to function): `<section class="quiz"><ol><li class="q">`
    wrapping a `<p class="qtext">`, a `<ul class="options">` of
    `<li data-answer="true">`/`<li data-answer="false">` entries, and a
    `<p class="explain">` revealed on click. Match this exactly — see
    `teach-workspace/lessons/0006-dicts-and-comprehensions-review.html` lines 89–195
    for a working reference block.
  - Money: all `ee-heat` cost figures are USD unless labelled VND/IDR; VND figures
    convert via `vn_context.json`'s `fx.vnd_per_usd = 26250`. Energy unit conversion
    used throughout: 1 MMBtu = 293.071 kWh.
  - Timezone: if `PROGRESS.md`'s hour table uses dated weeks (optional — see Phase 5),
    follow the existing `teach-workspace/PROGRESS.md` convention of `Asia/Ho_Chi_Minh`
    (UTC+7), Monday→Sunday weeks.
  - `ee-heat` is a **separate git repository** with its own `.gitignore` that excludes
    `gap/` and `data/` entirely (confidential client material) and
    `tools/reopt/results_*.json`, `tools/energyplus/`, `tools/.venv/`,
    `tools/heat-pump-model/heat_pump_model/`, `tools/reference/` (regenerable/
    reinstallable). Never run `git add`, `git commit`, or any write-intent git command
    inside `ee-heat` as part of this plan.
  - `ee-heat/tools/heat-pump-model/heat_pump_model/` is itself a **separate nested git
    clone** (`NatLabRockies/heat_pump_model`) with its own `.git`. Running its Jupyter
    notebooks may modify tracked notebook-output cells inside that nested repo — this
    is expected and harmless (it is a reference tool clone, not Gap deliverable
    work), but never commit inside it either.
- **Repo map (this repo, `agentic-degrees`):**
  ```
  agentic-degrees/
    curriculum.json                  # OCW course index only — do not touch
    research/                        # brainstorm briefs (this plan's source brief lives here)
    plans/                           # this plan file
    teach-workspace/
      MISSION.md, GLOSSARY.md, RESOURCES.md, NOTES.md, PROGRESS.md, LESSON-MAP.md
      assets/{style.css,quiz.js}     # shared engine — copy into gap-ee/assets/, do not modify
      lessons/000N-*.{html,md}       # existing BESS/grid-EE track — do not touch
      learning-records/000N-*.md     # existing BESS/grid-EE track — do not touch
      tools/verify_workspace.py      # the structural checker this plan must keep passing
      gap-ee/                        # <-- everything this plan creates lives here
  ```
- **Repo map (external, read-mostly dependency, `ee-heat`):**
  ```
  ee-heat/                                    # separate git repo, sibling to agentic-degrees
    activeContext.md                          # priority order, tool ranking, VN findings
    tools/README.md                           # per-tool usage, localization, caveats
    tools/measur/VN-settings-card.md          # MEASUR VN localization values
    tools/reopt/{vn_context.json, make_vn_scenario.py, run_scenario.jl,
                 Project.toml, Manifest.toml, garment_factory_process_heat.json}
    tools/heat-pump-model/{make_vn_inputs.py, vn_*_model_inputs.yml, heat_pump_model/}
    tools/energyplus/{EnergyPlus-26.1.0-.../energyplus.exe, weather/*.epw}
    tools/reference/{Industrial-Heat-Demand-Analysis/, foundational-industry-energy-data/}
    gap/, data/                               # CONFIDENTIAL — out of scope, never read or write
  ```

## Research Inputs
From `research/2026-08-25_gap-energy-efficiency-crash-course-brainstorm.md`:
- The course must live inside `teach-workspace/`'s existing lesson/quiz/
  learning-record machinery, in its **own namespace** (`gap-ee/`), on a hours budget
  fully separate from the existing BESS/grid-EE Phase-1 mission — never touching that
  mission's files, schedule, or `curriculum.json`.
- "Done" is defined as independently reproducing a real Gap deliverable end-to-end
  (the Vietnam garment-factory REopt scenario), not just passing quizzes — the
  capstone is the actual gate, at 2 weeks / 15–20h per week.
- All five ranked `ee-heat` tools (MEASUR, REopt, `heat_pump_model`, EnergyPlus,
  IHDA/FIED) get hands-on lessons, not just the top two the tool-fit ranking would
  otherwise justify prioritizing.
- The capstone must be a **practice copy**, isolated from `ee-heat`'s real git
  history, extending the scenario with the `HotThermalStorage` sizing that
  `activeContext.md` explicitly flags as the next step but says has not been built.
- Lessons reference `ee-heat` material **by path**, matching how existing lessons
  already reference `mit-ocw-curriculum/` PDFs as plain-text paths rather than copies
  or hyperlinks — do not duplicate `ee-heat` content into this repo.
- No client-memo-writing skill in scope; free/public sourcing only for any
  supplementary thermo/heat-transfer material beyond what already sits in `ee-heat`.

## Assumptions and Constraints
- **ASM-001:** No hard external Gap Inc. deliverable deadline is confirmed to fall
  inside this 2-week sprint window. **BINDING DEFAULT:** treat the course as
  capability-building toward the next Gap work cycle; do not compress or reorder the
  lesson sequence below to chase an unconfirmed date. If a real deadline surfaces
  later, re-sequence Phase 3/4 to front-load MEASUR + REopt (the top-2 tools by
  `activeContext.md`'s own fit ranking) and treat `heat_pump_model`/EnergyPlus/
  IHDA-FIED lessons (gap-0008–0010) as deferrable.
- **ASM-002:** The exact input field names REopt.jl's `HotThermalStorage` technology
  requires are not documented anywhere in `ee-heat` (only its existence is named, in
  `ee-heat/tools/README.md`'s "Relevant inputs" list). **BINDING DEFAULT:** discover
  them via Julia reflection at the start of Phase 4 (Task 04-01) before writing any
  JSON — never guess field names. The reflection commands and fallback are specified
  in Phase 4.
- **ASM-003:** The combined weekly study load during the sprint (15–20h/wk for this
  track, on top of the existing, separately-budgeted 12–14h/wk BESS/grid-EE mission)
  has no built-in buffer week the way the 8-week BESS mission does. **BINDING
  DEFAULT:** if a week's lessons are not finished, defer the remaining `gap-ee`
  lessons to the following week rather than cutting BESS-mission hours or skipping
  the capstone's verification step; log the deferral as a bullet under
  `teach-workspace/gap-ee/NOTES.md`'s "Current state" section (see Phase 5).
- **ASM-004:** `teach-workspace/gap-ee/` is the confirmed folder name and layout
  (mirrors `teach-workspace/` itself: `MISSION.md`, `GLOSSARY.md`, `RESOURCES.md`,
  `NOTES.md`, `PROGRESS.md`, `LESSON-MAP.md`, `assets/`, `lessons/`,
  `learning-records/`).
- **CON-001:** MEASUR (v1.8.3, installed at
  `%LOCALAPPDATA%\Programs\MEASUR\MEASUR.exe`) is a Windows GUI application with no
  CLI and no scriptable settings — every MEASUR-related task and verification step in
  this plan is manual (screenshots/screen-reading), not shell-automatable.
- **CON-002:** `heat_pump_model`'s cost outputs are known-bad (negative capital cost,
  garbled units — documented in `ee-heat/tools/README.md` §3). Any lesson or capstone
  step using it must use it **only** for COP / refrigerant-physics verification,
  never for its cost or LCOH output.
- **CON-003:** REopt has no native coal fuel type. Coal must always be modelled by
  declaring `fuel_type: "natural_gas"` on `ExistingBoiler` and overriding **both**
  `fuel_cost_per_mmbtu` and `emissions_factor_lb_CO2_per_mmbtu` — this is already done
  correctly in the existing `garment_factory_process_heat.json`; do not "fix" it to a
  literal coal type (none exists) when copying it in Phase 3.
- **DEC-001–DEC-017:** All resolved decisions from the brainstorm brief (course
  trigger, success definition, teach-workspace integration, parallel/separate
  scheduling, thermo-primer inclusion, capstone site choice, technical-only scope,
  2-week/15–20h pace, separate lesson namespace, all-5-tools coverage, free/public
  sourcing, practice-copy isolation, path-reference-not-copy convention, and the
  four repo-derived decisions on `curriculum.json`, assessment format, reading spine,
  and folder layout) are treated as fixed inputs to this plan and are not
  re-litigated here — see the brief for full rationale.

## Specification

**Breakeven COP formula** (used in gap-0007's lesson content and to sanity-check the
capstone's REopt result in Phase 4). A heat pump "breaks even" against the coal
boiler when its delivered-heat cost equals coal's delivered-heat cost:

```
COP_breakeven = (P_elec × 293.071) / (P_coal / η_boiler)
```

Symbol annotations:
- `P_elec` — grid electricity price, USD per kWh, for the tariff period being
  evaluated (peak / normal / off-peak).
- `293.071` — kWh per MMBtu (unit-conversion constant; 1 MMBtu = 293.071 kWh).
- `P_coal` — delivered coal fuel price, USD per MMBtu (as-fired, before boiler
  losses).
- `η_boiler` — existing coal boiler thermal efficiency, as a fraction (e.g. `0.75`
  for 75%).
- `P_coal / η_boiler` — coal's **delivered heat** cost, USD per MMBtu of useful heat
  (accounts for boiler losses).
- `COP_breakeven` — the coefficient of performance a heat pump must exceed, at this
  electricity price, to deliver heat more cheaply than the coal boiler.

**Verification of this formula against `ee-heat`'s published numbers** (all values
from `ee-heat/tools/reopt/vn_context.json` and `ee-heat/tools/README.md`, checked
2026-08-18): with `P_coal = $5.30/MMBtu`, `η_boiler = 0.75` (so
`P_coal/η_boiler = $7.067/MMBtu`):

| Tariff period | `P_elec` (USD/kWh) | `COP_breakeven` computed | Published value |
|---|---|---|---|
| Off-peak (00:00–06:00) | 0.04533 | (0.04533 × 293.071) / 7.067 = **1.879** | 1.88 |
| Normal | 0.06983 | (0.06983 × 293.071) / 7.067 = **2.895** | 2.90 |
| Peak (Mon–Sat 17:30–22:30) | 0.12945 | (0.12945 × 293.071) / 7.067 = **5.369** | 5.37 |

All three reproduce the published table to within rounding — this formula is the
gap-0007 lesson's core worked example and the capstone's first sanity check in Phase
4.

## Phase Summary
| Phase | Goal | Dependencies | Primary outputs |
|---|---|---|---|
| PHASE-01 | Scaffold the `gap-ee` workspace (required files, shared assets) | None | `teach-workspace/gap-ee/{MISSION,GLOSSARY,RESOURCES,NOTES,PROGRESS,LESSON-MAP}.md`, `assets/{style.css,quiz.js}`, verifier passing with 0 lessons |
| PHASE-02 | Author Week-1 lessons: thermo/refrigeration/steam fundamentals + MEASUR | PHASE-01 | `lessons/0001`–`0005` (.html + .md), verifier passing |
| PHASE-03 | Author Week-2 tool lessons: REopt, breakeven-COP, `heat_pump_model`, EnergyPlus, IHDA/FIED; create the REopt practice copy | PHASE-02 | `lessons/0006`–`0010`, `capstone/reopt-practice/` (baseline-verified copy), verifier passing |
| PHASE-04 | Capstone: extend the practice copy with `ASHPWaterHeater` + `HotThermalStorage`, run, verify, author `lessons/0011` | PHASE-03 | `lessons/0011`, extended scenario + results in `capstone/reopt-practice/`, 2 learning records |
| PHASE-05 | Tracking, final verification, handoff | PHASE-04 | `PROGRESS.md` filled in, final verifier pass, commit in `agentic-degrees` only |

## Detailed Phases

### PHASE-01 - Scaffold the `gap-ee` Workspace
**Goal**
Create the required-file skeleton for a new, independently-verifiable teach-workspace
track at `teach-workspace/gap-ee/`, so `tools/verify_workspace.py` passes against it
before any lesson content is authored.

**Tasks**
- [ ] TASK-01-01: Create `teach-workspace/gap-ee/MISSION.md` following the
  `MISSION-FORMAT` template (`# Mission: {Topic}` / `## Why` / `## Success looks
  like` / `## Constraints` / `## Out of scope`). Content must state: Why — become
  independently able to run the Gap Inc. clean-heat toolchain (MEASUR, REopt,
  `heat_pump_model`, EnergyPlus, IHDA/FIED) and defend a technical finding without
  deferring to a consultant, on the active Gap Inc. engagement. Success looks like —
  list the 5 concrete tool-competencies plus "independently reproduce and extend the
  Vietnam garment-factory breakeven-COP + thermal-storage finding." Constraints — 2
  weeks, 15–20h/wk, runs parallel to and fully separate from the existing BESS/
  grid-EE mission's budget, English only, free/public sources only. Out of scope —
  client memo writing, solar/BESS/DPPA, any edit to the live `ee-heat` repository.
- [ ] TASK-01-02: Create `teach-workspace/gap-ee/GLOSSARY.md` following the
  `GLOSSARY-FORMAT` template — header `# Gap Energy Efficiency Glossary`, one
  sentence description, then `## Terms` (empty list to start, or seeded with terms
  the learner already demonstrably knows — leave empty; terms get added lesson by
  lesson per the format's own rule of only adding a term once understood).
- [ ] TASK-01-03: Create `teach-workspace/gap-ee/RESOURCES.md` following the
  `RESOURCES-FORMAT` template, with a `## Knowledge` section seeded with the primary
  sources this plan already identifies: `ee-heat/activeContext.md`,
  `ee-heat/tools/README.md`, `ee-heat/tools/measur/VN-settings-card.md`, the DOE/ORNL
  AMO Steam System / Process Heating source material MEASUR's modules are built on
  (cite by name, no fabricated URLs — the executor should locate the actual current
  DOE AMO steam-system sourcebook URL at authoring time and annotate it per the
  format's rules), and REopt.jl's own documentation. Include a `## Gaps` section
  noting that `HotThermalStorage`'s exact input schema is not documented anywhere
  local (ties to ASM-002).
- [ ] TASK-01-04: Create `teach-workspace/gap-ee/NOTES.md` as a scratchpad, seeded
  with: the verifier contract (copy the bullet list from this repo's
  `teach-workspace/NOTES.md` "Workspace contract" section, adjusted to say
  `gap-ee/lessons/`), the standing preference "English only, worked numeric examples
  over prose, concise", and a "Current state" section dated today noting "Phase-01
  scaffold complete, lessons not yet authored."
- [ ] TASK-01-05: Create `teach-workspace/gap-ee/PROGRESS.md` with an `## Hours`
  table (2 rows, Week 1 and Week 2, columns Dates / Domain h / Tool h / Total h,
  dates left blank to fill in during execution) and a `## Lessons` checklist listing
  all 11 planned lesson slugs (from `LESSON-MAP.md`, Task 01-06) as unchecked boxes.
- [ ] TASK-01-06: Create `teach-workspace/gap-ee/LESSON-MAP.md` with a table of all
  11 lessons in study order:
  | # | Day | Slug | Primary tool/source | Focus |
  |---|---|---|---|---|
  | 0001 | 1 | thermo-and-heat-transfer-primer | free DOE/public thermo reference | conduction, convection, sensible vs. latent heat, why °C/bar(g)/kJ units matter |
  | 0002 | 1–2 | refrigeration-cycle-and-cop | free public refrigeration-cycle reference | vapor-compression cycle, COP definition, ideal vs. actual COP |
  | 0003 | 2–3 | steam-systems-fundamentals | DOE AMO steam-system reference | boiler efficiency, blowdown, condensate return, flash steam, header balance |
  | 0004 | 3–4 | measur-hands-on-steam-and-waste-heat | MEASUR v1.8.3 + `ee-heat/tools/measur/VN-settings-card.md` | localize MEASUR to Vietnam, run Steam System Modeler + Waste Heat Recovery on the placeholder garment-plant defaults |
  | 0005 | 5 | tea-lcoh-fundamentals | free public TEA/LCOH reference | discounting, payback, levelized cost of heat, why sizing against an unoptimized load overstates equipment |
  | 0006 | 6–7 | reopt-hands-on-scenario-building | `ee-heat/tools/reopt/` (read) → practice copy | `ProcessHeatLoad`/`ExistingBoiler`/`ElectricHeater` inputs, run the existing baseline scenario in a practice copy, reproduce the published NPV/emissions numbers |
  | 0007 | 7 | tou-tariffs-and-breakeven-cop | `ee-heat/tools/reopt/vn_context.json` | reproduce the breakeven-COP table by hand using this plan's `## Specification` formula |
  | 0008 | 8 | heat-pump-model-cross-check | `ee-heat/tools/heat-pump-model/` | run the CoolProp-based model, verify the corroborated COP 3.11 dye-house finding, understand why its cost output is unusable |
  | 0009 | 9 | energyplus-envelope-hvac-orientation | `ee-heat/tools/energyplus/` | run `1ZoneUncontrolled.idf` against the Ho Chi Minh weather file; understand why this tool is standby (envelope/HVAC only, not dye-house steam) |
  | 0010 | 9–10 | ihda-fied-methodology | `ee-heat/tools/reference/` | temperature-range-by-end-use methodology; why the US EPA/EIA numbers can't be reused but the method can |
  | 0011 | 11–14 | capstone-thermal-storage-sizing | practice copy of `ee-heat/tools/reopt/` | add `ASHPWaterHeater` (COP 3.11) + `HotThermalStorage` to the practice scenario, run, verify against the breakeven-COP table |
- [ ] TASK-01-07: Copy `teach-workspace/assets/style.css` to
  `teach-workspace/gap-ee/assets/style.css` and `teach-workspace/assets/quiz.js` to
  `teach-workspace/gap-ee/assets/quiz.js` byte-for-byte (do not modify either file —
  `gap-ee`'s lessons reuse the identical shared engine).

**File Changes**
- `teach-workspace/gap-ee/MISSION.md` (create): per TASK-01-01.
- `teach-workspace/gap-ee/GLOSSARY.md` (create): per TASK-01-02.
- `teach-workspace/gap-ee/RESOURCES.md` (create): per TASK-01-03.
- `teach-workspace/gap-ee/NOTES.md` (create): per TASK-01-04.
- `teach-workspace/gap-ee/PROGRESS.md` (create): per TASK-01-05.
- `teach-workspace/gap-ee/LESSON-MAP.md` (create): per TASK-01-06.
- `teach-workspace/gap-ee/assets/style.css` (create): byte-identical copy of
  `teach-workspace/assets/style.css`.
- `teach-workspace/gap-ee/assets/quiz.js` (create): byte-identical copy of
  `teach-workspace/assets/quiz.js`.

**Function Signatures**
None — no code interfaces change in this phase.

**Test Specs**
- `python teach-workspace/tools/verify_workspace.py teach-workspace/gap-ee` →
  stdout exactly `OK: 0 lessons, 0 records, 0 problems`, exit code `0`.
- Edge case: if `teach-workspace/gap-ee/lessons/` and `learning-records/` don't exist
  yet, the verifier's `scan_numbered` returns `[]` for both (confirmed by reading
  `teach-workspace/tools/verify_workspace.py` lines 43–52 — `Path.is_dir()` guard) —
  this is expected and not a failure; do not pre-create empty `lessons/` or
  `learning-records/` directories.

**Dependencies**
None.

**Exit Criteria**
- [ ] All 8 files/dirs in File Changes exist.
- [ ] The verify command above prints `OK: 0 lessons, 0 records, 0 problems`.

**Phase Risks**
- **RISK-01-01:** Copying `assets/*` with a text-mode copy tool could alter line
  endings and change the files' byte content (harmless functionally, but breaks the
  "byte-identical" intent). Mitigation: use a binary-safe copy command
  (`cp teach-workspace/assets/style.css teach-workspace/gap-ee/assets/style.css` in a
  POSIX-compatible shell, or `Copy-Item` in PowerShell — both preserve bytes;
  avoid any tool that does text transcoding).

### PHASE-02 - Week-1 Lessons: Thermo, Refrigeration Cycle, Steam Systems, MEASUR, TEA/LCOH
**Goal**
Author and verify lessons 0001–0005: the foundational domain knowledge (thermo,
refrigeration cycle/COP, steam systems, TEA/LCOH) plus the first hands-on tool lesson
(MEASUR), giving the learner everything needed to read `ee-heat/activeContext.md`'s
findings with full technical understanding before touching REopt in Phase 3.

**Tasks**
- [ ] TASK-02-01: Author `teach-workspace/gap-ee/lessons/0001-thermo-and-heat-transfer-primer.{html,md}`.
  Cover: conduction/convection/radiation basics, sensible vs. latent heat (why steam
  carries far more energy per kg than hot water — this is *why* steam systems exist),
  the °C / bar(g) / kJ unit system MEASUR uses (tie explicitly to
  `ee-heat/tools/measur/VN-settings-card.md`'s "Set units to Metric" instruction).
  Include at least 1 worked numeric example (e.g., energy to raise 1000 kg water from
  20°C to boiling vs. the latent heat to then vaporize it, using specific heat
  4.186 kJ/kg·°C and latent heat of vaporization ≈2257 kJ/kg). Follow the format
  contract: `../assets/style.css` link, `../MISSION.md` link, `Primary source` text
  citing the specific free public source used (locate and cite an actual current DOE
  or equivalent public reference at authoring time — do not fabricate a URL), and a
  `<section class="quiz">` with at least 5 questions matching the exact markup in
  `teach-workspace/lessons/0006-dicts-and-comprehensions-review.html` lines 89–195.
- [ ] TASK-02-02: Author `teach-workspace/gap-ee/lessons/0002-refrigeration-cycle-and-cop.{html,md}`.
  Cover: the 4-stage vapor-compression cycle (evaporator, compressor, condenser,
  expansion valve), COP definition (`COP = Q_heat_delivered / W_electrical_input`),
  ideal vs. actual COP (second-law efficiency), and explicitly connect to
  `ee-heat/tools/heat-pump-model/`'s finding: ideal COP 6.22 vs. actual COP 3.11 at
  50% second-law efficiency on the 45°C→95°C dye-house case. At least 1 worked
  numeric example computing actual COP from ideal COP and a stated second-law
  efficiency. Same format contract as Task 02-01.
- [ ] TASK-02-03: Author `teach-workspace/gap-ee/lessons/0003-steam-systems-fundamentals.{html,md}`.
  Cover: boiler efficiency (fuel in vs. steam energy out), blowdown, condensate
  return (why returning hot condensate instead of dumping it saves both fuel and
  water-treatment cost), flash steam recovery, header balance. Ground every concept
  in the exact `ee-heat/tools/measur/VN-settings-card.md` "What to look for first"
  ordering (condensate return rate → blowdown rate/heat recovery → flash steam
  recovery → stack losses/excess air → distribution insulation) — this ordering
  *is* the lesson's structure. Same format contract.
- [ ] TASK-02-04: Author `teach-workspace/gap-ee/lessons/0004-measur-hands-on-steam-and-waste-heat.{html,md}`.
  This is a **manual, hands-on** lesson (MEASUR is a GUI app, per CON-001): walk
  through (a) launching MEASUR v1.8.3 at
  `%LOCALAPPDATA%\Programs\MEASUR\MEASUR.exe`, (b) entering every value from
  `ee-heat/tools/measur/VN-settings-card.md` into Settings → Default Settings
  (Metric units; electricity $0.06983/kWh normal, $0.04533/kWh off-peak,
  $0.12945/kWh peak; boiler fuel $5.02/GJ; grid emissions 0.1831 kg CO2/MJ; coal
  emissions 92.1 kg CO2/GJ), (c) running the Steam System Modeler and Waste Heat
  Recovery modules against the "Typical Vietnamese garment/textile plant defaults"
  table in the same file (steam header ≤10 bar(g), dye-house/HTHW loop 60–95°C,
  boiler efficiency 75%, 16h/day 5–6 days/week). Include a short checklist the
  learner ticks off by hand (not a `<section class="quiz">` multiple-choice quiz for
  the manual-entry part — see Test Specs) but still include a
  `<section class="quiz">` with at least 5 conceptual questions about what each
  MEASUR module computes and why. Same format contract otherwise.
- [ ] TASK-02-05: Author `teach-workspace/gap-ee/lessons/0005-tea-lcoh-fundamentals.{html,md}`.
  Cover: discounting and NPV, simple payback, levelized cost of heat (LCOH) as
  "total lifecycle cost of a heat source ÷ total lifetime heat delivered," and the
  MEASUR-then-REopt sequencing rule from `ee-heat/activeContext.md` ("MEASUR first,
  REopt second... sizing a heat pump against an unoptimized steam load over-sizes
  the equipment and produces a wrong LCOH"). At least 1 worked numeric LCOH example
  using two candidate systems with different capital cost/lifetime/annual output.
  Same format contract.
- [ ] TASK-02-06: Run the Phase-1 verify command (see Test Specs) and fix any
  reported problems before moving to Phase 3.

**File Changes**
- `teach-workspace/gap-ee/lessons/0001-thermo-and-heat-transfer-primer.html` (create)
- `teach-workspace/gap-ee/lessons/0001-thermo-and-heat-transfer-primer.md` (create)
- `teach-workspace/gap-ee/lessons/0002-refrigeration-cycle-and-cop.html` (create)
- `teach-workspace/gap-ee/lessons/0002-refrigeration-cycle-and-cop.md` (create)
- `teach-workspace/gap-ee/lessons/0003-steam-systems-fundamentals.html` (create)
- `teach-workspace/gap-ee/lessons/0003-steam-systems-fundamentals.md` (create)
- `teach-workspace/gap-ee/lessons/0004-measur-hands-on-steam-and-waste-heat.html` (create)
- `teach-workspace/gap-ee/lessons/0004-measur-hands-on-steam-and-waste-heat.md` (create)
- `teach-workspace/gap-ee/lessons/0005-tea-lcoh-fundamentals.html` (create)
- `teach-workspace/gap-ee/lessons/0005-tea-lcoh-fundamentals.md` (create)
- `teach-workspace/gap-ee/PROGRESS.md` (modify): check off lessons 0001–0005 in the
  `## Lessons` checklist as each is authored; fill in Week-1 hour actuals if tracked.

**Function Signatures**
None — no code interfaces change in this phase.

**Test Specs**
- `python teach-workspace/tools/verify_workspace.py teach-workspace/gap-ee` →
  stdout `OK: 5 lessons, 0 records, 0 problems`, exit code `0`.
- Worked example (0001): 1000 kg water, 20°C → 100°C, then fully vaporized at
  100°C → sensible heat = `1000 kg × 4.186 kJ/kg·°C × 80°C = 334,880 kJ`; latent
  heat = `1000 kg × 2257 kJ/kg = 2,257,000 kJ` → vaporizing costs **~6.7×** more
  energy than heating to boiling — this ratio is the number the lesson's worked
  example must reproduce.
- Worked example (0002): ideal COP 6.22 × second-law efficiency 0.5 = actual COP
  **3.11** — must match `ee-heat/tools/README.md`'s stated result exactly (this is
  the same run the learner will later reproduce hands-on in Phase 3's gap-0008).
- Edge case: if a MEASUR module (Task 02-04) will not accept the `natural_gas`
  workaround fuel type cleanly, the lesson must say so explicitly and point back to
  `ee-heat/tools/measur/VN-settings-card.md`'s "Fuel type" section rather than
  silently picking a different value.

**Dependencies**
- PHASE-01 (workspace scaffold, shared assets).

**Exit Criteria**
- [ ] 5 lessons authored (10 files: 5 `.html` + 5 `.md`).
- [ ] Verify command passes with `5 lessons, 0 records, 0 problems`.
- [ ] Each lesson's worked numeric example matches the Test Specs values above.

**Phase Risks**
- **RISK-02-01:** MEASUR's one-click installer stores settings in an internal
  per-user database (CON-001) — if a second Windows user account or a fresh profile
  runs this lesson, the VN localization must be re-entered from scratch. Mitigation:
  lesson 0004 states this explicitly and links back to
  `ee-heat/tools/measur/VN-settings-card.md` as the re-entry source of truth every
  time, rather than assuming settings persist.
- **RISK-02-02:** Free/public source citations for 0001/0002/0003/0005 (thermo,
  refrigeration cycle, steam systems, TEA/LCOH) are not pre-selected by this plan —
  the executor must locate real, current, free sources at authoring time rather than
  reuse a URL that may be stale. Mitigation: `RESOURCES.md` (Phase 1) is the place to
  record and vet each source before it's cited in a lesson's `Primary source` line.

### PHASE-03 - Week-2 Lessons: REopt, Breakeven COP, `heat_pump_model`, EnergyPlus, IHDA/FIED
**Goal**
Author and verify lessons 0006–0010, and — as part of authoring 0006 — create the
isolated REopt practice copy that both 0006 and the Phase-4 capstone (0011) run
against, so the live `ee-heat` repository is never modified.

**Tasks**
- [ ] TASK-03-01: Create the practice copy directory and populate it:
  ```
  mkdir -p teach-workspace/gap-ee/capstone/reopt-practice
  cp "/c/Users/tukum/Downloads/ee-heat/tools/reopt/Project.toml" \
     "/c/Users/tukum/Downloads/ee-heat/tools/reopt/Manifest.toml" \
     "/c/Users/tukum/Downloads/ee-heat/tools/reopt/vn_context.json" \
     "/c/Users/tukum/Downloads/ee-heat/tools/reopt/make_vn_scenario.py" \
     "/c/Users/tukum/Downloads/ee-heat/tools/reopt/run_scenario.jl" \
     "/c/Users/tukum/Downloads/ee-heat/tools/reopt/garment_factory_process_heat.json" \
     teach-workspace/gap-ee/capstone/reopt-practice/
  ```
  Adjust the source path if `ee-heat` is checked out somewhere other than
  `C:\Users\tukum\Downloads\ee-heat` on the executing machine (see ASM-004's sibling
  assumption). All subsequent Julia/Python commands in this phase and Phase 4 run
  from inside `teach-workspace/gap-ee/capstone/reopt-practice/`, never from inside
  `ee-heat/tools/reopt/`.
- [ ] TASK-03-02: Instantiate the Julia environment once:
  ```
  cd teach-workspace/gap-ee/capstone/reopt-practice
  julia --project=. -e "using Pkg; Pkg.instantiate()"
  ```
  Then reproduce the existing baseline result:
  ```
  julia --project=. run_scenario.jl garment_factory_process_heat.json
  ```
  Expected stdout includes `Electric heater size (mmbtu/hr): 0.0` (or the line is
  absent because `ElectricHeater` was not built) and
  `CO2 emissions, optimal (t/yr)  : 13740.0` (± rounding), matching
  `ee-heat/activeContext.md`'s published "13,740 tCO2/yr, reproducing a hand
  calculation exactly (5,829 t boiler + 7,911 t grid)."
- [ ] TASK-03-03: Author `teach-workspace/gap-ee/lessons/0006-reopt-hands-on-scenario-building.{html,md}`.
  Walk through the scenario's JSON structure field by field
  (`Site`/`ElectricLoad`/`ElectricTariff`/`ElectricUtility`/`ProcessHeatLoad`/
  `ExistingBoiler`/`ElectricHeater`/`Financial`), the coal-as-`natural_gas` workaround
  (CON-003), and have the learner run TASK-03-02's two commands themselves inside
  the practice copy, confirming their own output matches the expected values in
  Test Specs below. Same format contract as Phase 2 lessons.
- [ ] TASK-03-04: Author `teach-workspace/gap-ee/lessons/0007-tou-tariffs-and-breakeven-cop.{html,md}`.
  Present this plan's `## Specification` breakeven-COP formula, then have the
  learner reproduce the 3-row table (off-peak 1.88 / normal 2.90 / peak 5.37) by
  hand from `vn_context.json`'s raw VND rates and FX rate — not by reading the
  precomputed USD rates in `VN-settings-card.md` — as the worked example. Same
  format contract.
- [ ] TASK-03-05: Author `teach-workspace/gap-ee/lessons/0008-heat-pump-model-cross-check.{html,md}`.
  Have the learner run, **inside `ee-heat/tools/heat-pump-model/` directly** (this
  is a read/verify-only operation on already-committed, idempotent generator output
  — see Environment & Conventions' gotcha — not a scenario edit, so the DEC-013
  practice-copy rule does not apply here):
  ```
  cd /c/Users/tukum/Downloads/ee-heat/tools/heat-pump-model
  /c/Users/tukum/Downloads/ee-heat/tools/.venv/Scripts/python.exe make_vn_inputs.py
  ```
  then confirm (via `git -C /c/Users/tukum/Downloads/ee-heat status --short` from
  outside `ee-heat`, or `cd`ing in only to check status, never to commit) that this
  produces **no diff** in `ee-heat` — if it does, stop and investigate before
  proceeding; do not commit inside `ee-heat` regardless. Then launch
  `tools/.venv/Scripts/python.exe -m jupyterlab` and open `test_heat_pump.ipynb`,
  running the dye-house case (45°C source → 95°C sink) and confirming ideal COP
  6.22 / actual COP 3.11 on R1234ze(Z). The lesson must explicitly teach CON-002
  (cost output is unusable; use this tool for COP only). Same format contract.
- [ ] TASK-03-06: Author `teach-workspace/gap-ee/lessons/0009-energyplus-envelope-hvac-orientation.{html,md}`.
  Have the learner run, from inside `ee-heat/tools/energyplus/` (this entire
  directory is gitignored by `ee-heat`, so any output here is automatically outside
  the client repo's tracked history):
  ```
  cd /c/Users/tukum/Downloads/ee-heat/tools/energyplus
  ./EnergyPlus-26.1.0-6f2e40d102-Windows-x86_64/energyplus.exe \
    -w weather/VNM_SVN_Ho.Chi.Minh-Tan.Son.Nhat.Intl.AP.489000_TMYx.2011-2025.epw \
    -d out \
    -r EnergyPlus-26.1.0-6f2e40d102-Windows-x86_64/ExampleFiles/1ZoneUncontrolled.idf
  ```
  and confirm `out/eplusout.eio` contains a `Site:Location` line naming
  `Ho.Chi.Minh-Tan.Son.Nhat.Intl.AP`. The lesson must teach *why* this tool is
  ranked standby for this scope (envelope/HVAC only — does not model dye-house
  steam) rather than treating the successful run as evidence it's useful here. Same
  format contract.
- [ ] TASK-03-07: Author `teach-workspace/gap-ee/lessons/0010-ihda-fied-methodology.{html,md}`.
  Read-only lesson (no code run required): walk through
  `ee-heat/tools/reference/Industrial-Heat-Demand-Analysis/Enduse_Calc.py`'s approach
  to assigning temperature ranges by end-use and industry, and
  `foundational-industry-energy-data/`'s unit-level characterization structure.
  Teach the explicit rule from `ee-heat/tools/README.md` §5: take the *method*, never
  the US EPA/EIA *numbers*, since no Vietnamese or Indonesian equivalent dataset
  exists. Same format contract.
- [ ] TASK-03-08: Run the Phase-3 verify command (see Test Specs) and fix any
  reported problems before moving to Phase 4.

**File Changes**
- `teach-workspace/gap-ee/capstone/reopt-practice/{Project.toml,Manifest.toml,
  vn_context.json,make_vn_scenario.py,run_scenario.jl,
  garment_factory_process_heat.json}` (create): copied verbatim from
  `ee-heat/tools/reopt/` per TASK-03-01.
- `teach-workspace/gap-ee/lessons/0006-reopt-hands-on-scenario-building.{html,md}` (create)
- `teach-workspace/gap-ee/lessons/0007-tou-tariffs-and-breakeven-cop.{html,md}` (create)
- `teach-workspace/gap-ee/lessons/0008-heat-pump-model-cross-check.{html,md}` (create)
- `teach-workspace/gap-ee/lessons/0009-energyplus-envelope-hvac-orientation.{html,md}` (create)
- `teach-workspace/gap-ee/lessons/0010-ihda-fied-methodology.{html,md}` (create)
- `teach-workspace/gap-ee/PROGRESS.md` (modify): check off lessons 0006–0010.

**Function Signatures**
None — no code interfaces change in this phase.

**Test Specs**
- `julia --project=. run_scenario.jl garment_factory_process_heat.json` (run from
  `teach-workspace/gap-ee/capstone/reopt-practice/`) → stdout contains
  `CO2 emissions, optimal (t/yr)  : 13740.0` (± 1.0 for rounding) and NPV `$0` (or a
  value REopt itself reports — `ee-heat/activeContext.md` states "REopt declined to
  build the electric boiler (0 MMBtu/hr, NPV $0)").
- Hand-computed breakeven table (0007): off-peak `1.88`, normal `2.90`, peak `5.37`
  — must match this plan's `## Specification` table exactly (already
  cross-verified above).
- `heat_pump_model` run (0008): ideal COP `6.22`, actual COP `3.11` on `R1234ze(Z)`.
- EnergyPlus run (0009): `out/eplusout.eio` (or `out/eplusout.err`, whichever the
  installed version emits `Site:Location` into) contains the string
  `Ho.Chi.Minh-Tan.Son.Nhat.Intl.AP`.
- `python teach-workspace/tools/verify_workspace.py teach-workspace/gap-ee` →
  stdout `OK: 10 lessons, 0 records, 0 problems`.
- Edge case: `git -C /c/Users/tukum/Downloads/ee-heat status --short` after TASK-03-05
  and TASK-03-06 → must show no changes to any *tracked* `ee-heat` file (gitignored
  paths like `tools/reopt/results_*.json` and everything under `tools/energyplus/`
  may freely appear as untracked — that is expected and fine).

**Dependencies**
- PHASE-02 (learner needs the thermo/refrigeration/steam/TEA foundation before the
  tool-specific lessons make sense).

**Exit Criteria**
- [ ] `teach-workspace/gap-ee/capstone/reopt-practice/` exists, is Julia-instantiated,
  and reproduces the published baseline numbers.
- [ ] 5 more lessons authored (10 files), verify command passes with
  `10 lessons, 0 records, 0 problems`.
- [ ] `ee-heat`'s tracked git state is unchanged (per the edge-case check above).

**Phase Risks**
- **RISK-03-01:** `ee-heat`'s absolute path may differ if this plan is executed on a
  machine other than the one it was authored on. Mitigation: every command in this
  phase that references `ee-heat` states the assumed absolute path explicitly (see
  ASM-004) — if it differs, substitute the real path everywhere `ee-heat` appears
  before running any command.
- **RISK-03-02:** Julia package resolution can fail if the practice copy's
  `Manifest.toml` pins a package version no longer available. Mitigation: if
  `Pkg.instantiate()` fails, fall back to `ee-heat/tools/reopt/install.jl`'s pattern
  (`Pkg.add(["REopt","JuMP","HiGHS"]); Pkg.instantiate()`) inside the practice copy
  instead of the pinned Manifest, and note the version drift in
  `teach-workspace/gap-ee/NOTES.md`.

### PHASE-04 - Capstone: Heat Pump + Thermal Storage Sizing
**Goal**
Extend the practice copy from Phase 3 with an `ASHPWaterHeater` technology (COP 3.11,
the corroborated dye-house finding) and a `HotThermalStorage` technology, run it, and
verify the result is directionally consistent with `ee-heat/activeContext.md`'s
published breakeven-COP reasoning — independently reproducing and extending the real
finding, entirely inside the isolated practice copy.

**Tasks**
- [ ] TASK-04-01: Discover `HotThermalStorage`'s real input field names (ASM-002) —
  do not guess. From `teach-workspace/gap-ee/capstone/reopt-practice/`, run:
  ```
  julia --project=. -e "using REopt; println(fieldnames(REopt.HotThermalStorage))"
  ```
  If that errors (the exact struct name may differ from the JSON key), fall back to:
  ```
  julia --project=. -e "using REopt; println(filter(n -> occursin(\"HotThermal\", string(n)), names(REopt, all=true)))"
  ```
  to find the real symbol, then re-run `fieldnames(...)` on whatever name that
  reveals. Do the same discovery pass for `REopt.ASHPWaterHeater` (its JSON-level
  fields `cop` and `can_serve_process_heat` are already confirmed by
  `ee-heat/tools/README.md`'s "Relevant inputs" list, but its full field set is not
  — confirm it the same way). Write the discovered field names and types to a new
  file, `teach-workspace/gap-ee/capstone/reopt-practice/schema-notes.md`, before
  writing any JSON.
- [ ] TASK-04-02: Create
  `teach-workspace/gap-ee/capstone/reopt-practice/make_vn_scenario_hp_storage.py` as
  a copy of `make_vn_scenario.py` (from the practice copy, not from `ee-heat`),
  modified to: (a) remove the placeholder `"ElectricHeater": {"cop": 1.0, ...}`
  block (a straight resistance heater, which the Phase-3 baseline run already showed
  REopt declines to build), (b) add an `"ASHPWaterHeater"` block with `"cop": 3.11`
  (the corroborated `heat_pump_model` finding from Phase 2/0008) and
  `"can_serve_process_heat": true`, using TASK-04-01's discovered field names for any
  other required fields (e.g. an installed-cost field, by analogy to
  `ElectricHeater`'s `installed_cost_per_mmbtu_per_hour: 110000.0` — confirm the
  exact `ASHPWaterHeater` field name from `schema-notes.md` rather than assuming it's
  identical to `ElectricHeater`'s), and (c) add a `"HotThermalStorage"` block using
  the field names discovered in TASK-04-01, sized to let REopt optimize its own
  capacity (do not hardcode a capacity — the whole point of the exercise is that
  REopt sizes it) unless TASK-04-01's discovery shows the technology requires an
  explicit bound to be considered at all, in which case set a generous bound (large
  enough not to constrain the optimizer) and note the chosen bound's rationale in
  `schema-notes.md`.
- [ ] TASK-04-03: Run the new generator and the new scenario:
  ```
  cd teach-workspace/gap-ee/capstone/reopt-practice
  julia --project=. -e "using Pkg" # no-op sanity check env is still instantiated
  /c/Users/tukum/Downloads/ee-heat/tools/.venv/Scripts/python.exe make_vn_scenario_hp_storage.py
  julia --project=. run_scenario.jl garment_factory_process_heat_hp_storage.json
  ```
  (Adjust `make_vn_scenario_hp_storage.py`'s output filename accordingly if it still
  writes `garment_factory_process_heat.json` by default — rename the output write
  target inside the script so the original baseline file from Phase 3 is never
  overwritten.)
- [ ] TASK-04-04: Compare the new run's results against the Phase-3 baseline and the
  breakeven-COP table from `## Specification`. Record the comparison — does REopt
  now choose to build a nonzero `ASHPWaterHeater` size? Does total optimal-case CO2
  emissions drop below the baseline's 13,740 tCO2/yr? Does the `HotThermalStorage`
  get sized to a nonzero capacity? — in a new learning record (Task 04-06).
- [ ] TASK-04-05: Author `teach-workspace/gap-ee/lessons/0011-capstone-thermal-storage-sizing.{html,md}`.
  This lesson documents the whole capstone: the schema-discovery process, the exact
  JSON diff from the baseline scenario, the run output, and the comparison against
  the breakeven-COP table — written as the technical narrative, not a
  multiple-choice-only lesson (still include a `<section class="quiz">` with at
  least 5 questions testing understanding of the result). Same format contract as
  all prior lessons.
- [ ] TASK-04-06: Write two learning records:
  `teach-workspace/gap-ee/learning-records/0001-<slug>.md` capturing the strongest
  non-obvious insight from Weeks 1–2 (e.g., the MEASUR-before-REopt sequencing
  rationale, or why `heat_pump_model`'s cost output must never be trusted), and
  `teach-workspace/gap-ee/learning-records/0002-<slug>.md` capturing the capstone's
  result (whether the heat-pump-plus-storage design was confirmed and by how much),
  following the `LEARNING-RECORD-FORMAT` template (title + 1–3 sentences; add
  `Evidence`/`Implications` sections only if they add real value).
- [ ] TASK-04-07: Run the Phase-4 verify command (see Test Specs) and fix any
  reported problems.

**File Changes**
- `teach-workspace/gap-ee/capstone/reopt-practice/schema-notes.md` (create): per
  TASK-04-01.
- `teach-workspace/gap-ee/capstone/reopt-practice/make_vn_scenario_hp_storage.py` (create): per TASK-04-02.
- `teach-workspace/gap-ee/capstone/reopt-practice/garment_factory_process_heat_hp_storage.json` (create): generated output of the script above, per TASK-04-03.
- `teach-workspace/gap-ee/capstone/reopt-practice/results_garment_factory_process_heat_hp_storage.json` (create): generated by `run_scenario.jl`, per TASK-04-03.
- `teach-workspace/gap-ee/lessons/0011-capstone-thermal-storage-sizing.{html,md}` (create): per TASK-04-05.
- `teach-workspace/gap-ee/learning-records/0001-<slug>.md` (create): per TASK-04-06.
- `teach-workspace/gap-ee/learning-records/0002-<slug>.md` (create): per TASK-04-06.
- `teach-workspace/gap-ee/PROGRESS.md` (modify): check off lesson 0011 and the
  capstone milestone.

**Function Signatures**
None — no code interfaces change in this phase (all changes are data/content: JSON
scenario files and Markdown/HTML lessons).

**Test Specs**
- `julia --project=. -e "println(fieldnames(REopt.HotThermalStorage))"` (or the
  fallback `names(REopt, all=true)` filter) → prints a non-empty list of field
  symbols; this list must be written into `schema-notes.md` before TASK-04-02
  proceeds — treat an empty or errored discovery as a blocker, not something to
  route around by guessing.
- `julia --project=. run_scenario.jl garment_factory_process_heat_hp_storage.json`
  → stdout's `CO2 emissions, optimal (t/yr)` line is **less than** `13740.0` (the
  Phase-3 baseline), and either an `ASHPWaterHeater` results block appears with a
  nonzero size, or the printed output/`results_*.json` documents specifically why
  it does not (e.g. a binding constraint discovered in `schema-notes.md`) — a silent
  zero-size result with no explanation is a failure of this task, not an acceptable
  outcome.
- `python teach-workspace/tools/verify_workspace.py teach-workspace/gap-ee` →
  stdout `OK: 11 lessons, 2 records, 0 problems`.

**Dependencies**
- PHASE-03 (practice copy must exist and reproduce the baseline first).

**Exit Criteria**
- [ ] `schema-notes.md` documents real, reflection-derived field names for both
  `ASHPWaterHeater` and `HotThermalStorage` — no guessed field names anywhere in
  `make_vn_scenario_hp_storage.py`.
- [ ] The new scenario runs to completion (`OPTIMAL` or equivalent solve status) and
  its emissions figure is compared explicitly against the 13,740 tCO2/yr baseline.
- [ ] Lesson 0011 and both learning records exist and the verify command passes with
  `11 lessons, 2 records, 0 problems`.
- [ ] `git -C /c/Users/tukum/Downloads/ee-heat status --short` still shows no changes
  to any tracked `ee-heat` file.

**Phase Risks**
- **RISK-04-01:** REopt.jl may reject an `ASHPWaterHeater` + `HotThermalStorage`
  combination outright (e.g. a required field this plan didn't anticipate) rather
  than solving with a small/zero result. Mitigation: TASK-04-01's schema discovery
  step exists precisely to catch this before a run is attempted; if the solve still
  errors, capture the exact Julia error text in `schema-notes.md` and treat the
  missing/malformed field it names as the next thing to fix, rather than abandoning
  `ASHPWaterHeater` for a re-purposed `ElectricHeater` block.
- **RISK-04-02:** The result could show REopt still declines to build any heat-pump
  capacity even after adding storage (e.g. if capital cost assumptions are
  unfavorable). This is a **valid, informative capstone outcome**, not a failure —
  the lesson (TASK-04-05) and learning record (TASK-04-06) must document it
  honestly either way; do not adjust inputs post-hoc to force a "heat pump wins"
  narrative.

### PHASE-05 - Tracking, Final Verification, and Handoff
**Goal**
Close out the sprint's record-keeping, run a final full verification pass, and
commit the new track in `agentic-degrees` only (never in `ee-heat`).

**Tasks**
- [ ] TASK-05-01: Fill in `teach-workspace/gap-ee/PROGRESS.md`'s `## Hours` table
  with actual dates and hours spent per week (source: whatever time-tracking the
  learner actually used during execution — this plan does not prescribe a specific
  tracking mechanism beyond the table's existence).
- [ ] TASK-05-02: If ASM-003's deferral condition was triggered at any point during
  execution, add a dated bullet to `teach-workspace/gap-ee/NOTES.md`'s "Current
  state" section describing what was deferred and the re-entry plan, mirroring how
  `teach-workspace/PROGRESS.md`'s existing "Deferrals" table works for the
  BESS/grid-EE mission.
- [ ] TASK-05-03: Run the full verifier one final time:
  ```
  python teach-workspace/tools/verify_workspace.py teach-workspace/gap-ee
  ```
  and separately confirm the existing BESS/grid-EE track is untouched:
  ```
  python teach-workspace/tools/verify_workspace.py teach-workspace
  ```
  (this second command must report the same lesson/record counts it reported before
  this plan started — if it changed, something in Phases 1–4 leaked outside
  `gap-ee/`, and that must be fixed before proceeding).
- [ ] TASK-05-04: Stage and commit the new track, in `agentic-degrees` only:
  ```
  git -C /c/Users/tukum/Downloads/agentic-degrees add teach-workspace/gap-ee research/2026-08-25_gap-energy-efficiency-crash-course-brainstorm.md plans/2026-08-25-gap-energy-efficiency-crash-course-plan.md
  git -C /c/Users/tukum/Downloads/agentic-degrees commit -m "teach: gap-ee track — 11-lesson EE-as-a-Service crash course + capstone"
  ```
  Do not run any `git add`/`git commit` inside `/c/Users/tukum/Downloads/ee-heat` at
  any point in this task or any prior phase.

**File Changes**
- `teach-workspace/gap-ee/PROGRESS.md` (modify): per TASK-05-01/05-02.
- `teach-workspace/gap-ee/NOTES.md` (modify): per TASK-05-02, only if triggered.

**Function Signatures**
None — no code interfaces change in this phase.

**Test Specs**
- `python teach-workspace/tools/verify_workspace.py teach-workspace/gap-ee` →
  `OK: 11 lessons, 2 records, 0 problems`.
- `python teach-workspace/tools/verify_workspace.py teach-workspace` → lesson/record
  counts identical to the counts before this plan's execution began (7 lessons — per
  this plan's Context Snapshot, lessons 0001–0007 already existed in
  `teach-workspace/lessons/` at planning time — and however many learning records
  existed at that time; the executor should note the actual pre-execution counts
  before Phase 1 and diff against them here rather than trust a hardcoded number).
- `git -C /c/Users/tukum/Downloads/ee-heat status --short` → no output (clean, or
  only gitignored/untracked artifacts from Phases 3–4's read/verify runs).

**Dependencies**
- PHASE-04.

**Exit Criteria**
- [ ] Both verify commands pass as specified.
- [ ] `ee-heat`'s git state confirmed unaffected.
- [ ] A single commit in `agentic-degrees` contains the new `gap-ee/` track.

**Phase Risks**
- **RISK-05-01:** Committing `teach-workspace/gap-ee/capstone/reopt-practice/` could
  accidentally include the copied `Manifest.toml`/`Project.toml` plus large
  generated `results_*.json` files in the commit, bloating repo history.
  Mitigation: before TASK-05-04, check file sizes
  (`du -sh teach-workspace/gap-ee/capstone/reopt-practice/*`); if
  `results_*.json` files are large (the existing
  `ee-heat/tools/reopt/results_garment_factory_process_heat.json` is ~4.4 MB), add a
  `teach-workspace/gap-ee/capstone/reopt-practice/.gitignore` entry for
  `results_*.json` before committing, matching `ee-heat`'s own convention of not
  tracking generated REopt results.

## Gotchas
- `verify_workspace.py`'s required-file and lesson checks are **relative to
  whatever workspace path you pass it** — always pass `teach-workspace/gap-ee`
  explicitly; running it with no argument checks `teach-workspace` (the *other*
  track) instead and will report `gap-ee`'s files as entirely missing.
- The word "Primary source" must appear verbatim (case-sensitive, exact phrase) in
  every lesson `.html` file — the checker does a plain substring match
  (`"Primary source" not in text`), not a regex, so e.g. "primary source"
  (lowercase) would fail it.
- REopt's `ElectricLoad` technology takes `doe_reference_name`; `ProcessHeatLoad`
  takes `industrial_reference_name` — using the wrong key name fails the whole
  scenario with `NaN` results rather than a clear error (documented in
  `ee-heat/tools/README.md` §2, "Five US-default traps," item 5). Both accept the
  same `FlatLoad_*` string values, which makes the wrong-key mistake easy to make
  silently.
- `renewable_energy_fraction_series` must be an 8760-length array, not a scalar —
  REopt's type signature accepts `Union{Real,Array}` but a scalar fails at runtime
  with "Unable to convert renewable_energy_fraction_series." The existing
  `make_vn_scenario.py` already handles this correctly
  (`[grid["renewable_energy_fraction"]] * 8760`) — preserve that pattern in
  TASK-04-02's modified copy.
- Coal has no native REopt fuel type — always `fuel_type: "natural_gas"` with both
  `fuel_cost_per_mmbtu` and `emissions_factor_lb_CO2_per_mmbtu` overridden (CON-003).
  Leaving REopt's natural-gas defaults in place understates coal's emissions by
  ~45% (`ee-heat/tools/README.md` §2, item 1).
- `heat_pump_model`'s cost/LCOH output is unusable (negative capital cost, garbled
  units) — every lesson and the capstone must use it for COP only (CON-002); never
  let a cost number from this tool flow into the capstone's economics.
- REopt's built-in load profiles are 2017 calendar-year profiles — `TARIFF_YEAR`
  must stay `2017` in any copy of `make_vn_scenario.py` (including TASK-04-02's),
  or the Mon–Sat peak window lands on the wrong days of the week.
- `ee-heat/tools/reopt/vn_context.json`'s FX rate (26,250 VND/USD) is explicitly
  flagged as a "sensitive input — a 5% FX move shifts every USD-denominated tariff
  result by 5%" — if this plan is executed much later than 2026-08-25, note in
  `schema-notes.md` that the FX rate (and possibly the coal price, sourced from a
  14-Aug-2026 Newcastle benchmark) may be stale, without changing the copied
  `vn_context.json` values (the practice copy should match the exact `ee-heat`
  baseline it's extending, not a re-localized one).
- If none of the above apply during a specific task: `None identified.`

## Verification Strategy
- **TEST-001:** `python teach-workspace/tools/verify_workspace.py teach-workspace/gap-ee` → `OK: 11 lessons, 2 records, 0 problems` (final state, after Phase 4).
- **TEST-002:** `python teach-workspace/tools/verify_workspace.py teach-workspace` → lesson/record counts unchanged from before this plan's execution (confirms no leakage into the existing BESS/grid-EE track).
- **TEST-003:** `cd teach-workspace/gap-ee/capstone/reopt-practice && julia --project=. run_scenario.jl garment_factory_process_heat.json` → `CO2 emissions, optimal (t/yr)  : 13740.0` (± 1.0), reproducing the Phase-3 baseline.
- **TEST-004:** `cd teach-workspace/gap-ee/capstone/reopt-practice && julia --project=. run_scenario.jl garment_factory_process_heat_hp_storage.json` → optimal-case CO2 emissions strictly less than `13740.0`, OR a documented reason in `schema-notes.md` for why not.
- **TEST-005:** `git -C /c/Users/tukum/Downloads/ee-heat status --short` → no changes to any tracked file, at every phase boundary from Phase 3 onward.
- **MANUAL-001:** Open each of the 11 lessons' `.html` files in a browser and click through every quiz question — confirm each question reveals a correct/incorrect state and a `.explain` paragraph on click (validates `assets/quiz.js` wiring, which `verify_workspace.py` does not itself execute).
- **MANUAL-002:** MEASUR walkthrough (Task 02-04) — confirm, by reading MEASUR's own UI, that Settings → Default Settings shows Metric units and the three VN electricity rates after entry; MEASUR has no CLI so this cannot be automated (CON-001).
- **MANUAL-003:** EnergyPlus run (Task 03-06) — open `out/eplusout.err` and confirm it contains no `**Severe**` or `**Fatal**` lines (EnergyPlus's own convention for a failed run).
- **OBS-001:** After Phase 5's commit, `git -C /c/Users/tukum/Downloads/agentic-degrees log -1 --stat` should show only files under `teach-workspace/gap-ee/`, `research/`, and `plans/` — any file outside those three paths in the diff is a leak to investigate before considering the commit final.

## Risks and Alternatives
- **RISK-001:** The entire course depends on `ee-heat` remaining available at its
  current path and content on the executing machine — it is a live, actively-updated
  client engagement repo, not a frozen archive. If `activeContext.md` or
  `vn_context.json` change materially between planning and execution (e.g. a new,
  updated FX rate or a real supplier site replacing the placeholder), lessons
  0001–0010's specific numbers may drift from what's currently in `ee-heat`.
  Mitigation: DEC-014 (reference by path, don't copy) is the deliberate tradeoff
  here — lessons should say "see `ee-heat/tools/reopt/vn_context.json`'s current
  value" rather than hardcoding numbers wherever the lesson's point is the *method*,
  and hardcode numbers (with an explicit "as of 2026-08-18" date) only where the
  lesson's point is reproducing a specific historical finding (e.g. the 13,740
  tCO2/yr baseline, which is a checkpoint to reproduce, not a live number).
- **RISK-002:** A foreign executor running this plan on a machine where `ee-heat`
  sits at a different path, or is unavailable at all, cannot complete Phases 3–4 as
  written. Mitigation: ASM-004 states the assumed path plainly at every command site
  (not just once) specifically so a path substitution is mechanical; if `ee-heat` is
  fully unavailable, Phases 1–2 (scaffold + foundational lessons) still stand alone
  and can be executed and verified independently.
- **ALT-001:** Continue the existing global lesson numbering (`teach-workspace/
  lessons/0008...`) instead of a separate `gap-ee/` namespace — rejected (DEC-009):
  mixes two missions with different gates/timelines into one `LESSON-MAP.md` and one
  `PROGRESS.md`.
- **ALT-002:** Commit capstone work directly into `ee-heat/tools/reopt/` as real
  project progress instead of an isolated practice copy — rejected (DEC-013): keeps
  training iteration out of the client engagement's git history; the practice
  copy's result can still be manually ported into `ee-heat` later if it proves
  genuinely deliverable-quality (that porting step is explicitly out of scope for
  this plan).
- **ALT-003:** Re-purpose the existing `ElectricHeater` block (raise its `cop` from
  1.0 to 3.11) instead of adding a distinct `ASHPWaterHeater` technology — considered
  in planning and rejected in favor of `ASHPWaterHeater`, because
  `ee-heat/activeContext.md` and `ee-heat/tools/README.md` both already name
  `ASHPWaterHeater` as REopt's distinct heat-pump technology (separate from
  `ElectricHeater`, which represents straight resistance heat) — using the
  purpose-built technology is more technically correct and more faithful to what an
  actual Gap deliverable would model.

## Suggested Next Step
Execute PHASE-01 first — it has no dependencies and its exit criteria (the verifier
passing with `0 lessons, 0 records, 0 problems` against `teach-workspace/gap-ee`) are
independently checkable before any lesson content is written. Proceed to PHASE-02
only after PHASE-01's exit criteria are confirmed.
