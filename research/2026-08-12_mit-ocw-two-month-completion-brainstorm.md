---
title: "Complete MIT OCW Material via Teach Skill — Parallel EE+SE Phase 1 (2 Months)"
date: "2026-08-12"
type: "brainstorm"
depth: "standard"
source_request: "a multiphase/weeks to plan complete the material using the teach skill in the next 2 months"
slug: "mit-ocw-two-month-completion"
---

# Brainstorm: Complete MIT OCW Material via Teach Skill — Parallel EE+SE Phase 1

> Supersedes `research/2026-08-11_mit-ocw-two-month-completion-brainstorm.md` (auto-mode
> draft). Every decision below was human-confirmed in an interactive interview on 2026-08-12;
> the 08-11 draft's auto-selections were overridden where noted. Archive or delete the 08-11
> file before running `/plan` so the two do not collide.

## Problem & Why Now
The workspace holds a complete free MIT OCW degree-equivalent curriculum (19 courses, 710 files:
software-engineering/ x10, electrical-engineering/ x9) plus the exhaustive OCW ranking brief
(research/2026-08-11_opencourseware-degrees.md). The material exists; the problem is **executing
it**. The research brief's literature finding is the crux: free OCW materials perform as well as
paid ones (Hilton 2016), but **self-study completion is the documented failure mode** (Daniel 2012;
MOOC dropout studies 2019). The user wants a multi-phase, week-by-week plan to actually work
through the material in the next 2 months, using the `teach` skill (MISSION.md-grounded,
retrieval-practice lessons, learning records) as the learning engine. Why now: the curriculum was
just downloaded and pushed to a private repo; momentum is maximal and the teach workspace does not
exist yet.

Reality check that shapes everything: 19 MIT courses ≈ 2,500-3,000h of material. The user runs a
full-time country-director job and has a 3-month-old child (b. May 2026). The user has committed to
a **12-14h/week budget, 60/40 EE/SE split** → **~100-110h in the 2-month window**. The window
target is aggressive by design (see DEC-003); checkpoints and the defer-don't-quit rule (DEC-011)
are the safety valves.

## Current vs Desired State
- **Current state:** 19 courses downloaded and organized (6.01SC: 29 PDFs + 12 zips incl. finals
  F09-F11, design-lab archives, hw zips; 6.002: 37 PDFs incl. hw1-10, quizzes, labs, finals;
  6.0002: full lecture notes + problem sets). Research brief + source ledger done; repo
  `tah-allotrope/agentic-degrees` (private) pushed. No teaching workspace, no study cadence, no
  learning records, no assessment history. Zero courses started.
- **Desired state:** A `teach-workspace/` (MISSION.md, RESOURCES.md, lessons/*.html,
  learning-records/*.md, reference/*.html, assets/, GLOSSARY.md, NOTES.md) running in the repo;
  8 weeks of dual-track study: 6.01SC completed (F11 + design lab gated), 6.002 completed through
  the full 14-week arc at compressed pace (all hw, both quizzes, final gated), 6.0002 entered via
  a 6.0001-primer and advanced substantially; each week closed with a learning record + agent
  session; later phases sketched so the whole 19-course map has a place.
- **Key repo surfaces:** `mit-ocw-curriculum/software-engineering/` (6.0001, 6.0002 dirs),
  `mit-ocw-curriculum/electrical-engineering/01-intro-to-eecs-1-6.01SC/` and
  `02-circuits-and-electronics-6.002/` (syllabus.txt, videos.txt, PDFs, zips, software/),
  `research/2026-08-11_opencourseware-degrees.md`, `research/sources/*.jsonl` (ledger).

## Resolved Decisions
> Confirmed interactively 2026-08-12. Deltas vs the 08-11 auto draft are marked.
> DEC-001..014 continuity from the auto draft unless noted.

- **DEC-001 (REVISED):** Mission = **dual-track from day one** — EE core ("Build the EE core that
  makes me dangerous on BESS/grid/machines for VIDA/DPPA work") **plus** the software-engineering
  track running in parallel. — user explicitly overrode the auto "EE-first, SE-second" ordering.
- **DEC-002 (REVISED):** Time budget = **12-14h/week, ~60/40 EE/SE** (4-5 weekday morning sessions
  of ~60-75 min + one weekend block of ~2-4h). — upgraded from the auto 10h/wk.
- **DEC-003 (REVISED):** Window scope = **6.01SC complete + 6.002 FULL (hw1-10, quiz1 + quiz2,
  timed final) + 6.0002 entered with substantial progress**. — user accepted that 6.01SC velocity
  must exceed nominal; flagged as HIGH RISK in ASM-002.
- **DEC-004:** Teach workspace lives at **`agentic-degrees/teach-workspace/`** (subfolder of the
  private repo, committed to git); run `/teach` from there.
- **DEC-005:** Lesson granularity = **1-2 tight-scoped teach lessons per OCW unit** with retrieval
  quizzes, tied to MISSION.md. Window lesson map ≈ 10 lessons for 6.01SC, ~12 for 6.002,
  ~8-10 for 6.0002 (incl. the primer).
- **DEC-006:** RESOURCES.md = curated from the downloaded OCW material (syllabus.txt, lecture-note
  PDFs, videos.txt playlists) + canonical textbooks (6.002: Agarwal & Lang; 6.003: Oppenheim;
  6.0001/6.0002: Guttag).
- **DEC-007:** Assessment = two gates per course: (a) teach lesson quizzes weekly (retrieval
  practice), (b) the course's own past exams, timed, graded against provided solutions — 6.01SC
  finals F09-F11, 6.002 quizzes + final, 6.0002 problem sets + final.
- **DEC-008 (CONFIRMED by user):** **Weekly 30-45 min agent teach/review session** — review
  learning records, take the week's synthesis quiz, commission next week's lessons.
- **DEC-009:** Videos = **YouTube streaming only** via videos.txt (no downloads) — user's explicit
  standing instruction; teach lessons link relevant lectures as primary sources.
- **DEC-010 (REVISED):** Progress tracking = learning records (native) + **weekly git commit+push**
  of teach-workspace — aligned with the user's standing git-after-agent-runs habit.
- **DEC-011:** Contingency = **"defer, don't quit"** — any unit stalling >1 week is logged as
  deferred with a re-entry plan and the schedule flexes (swap to a lighter unit). Week 6 is a
  built-in buffer.
- **DEC-012 (CONFIRMED in framing):** Phase 1 capstone = **timed 6.01SC final (F11) + the design-
  lab project**; 6.002's timed final is the second gate. Both documented in learning records.
- **DEC-013:** Lesson language = **English**.
- **DEC-014:** No new downloads — all Phase 1 materials are already local; the plan is pure
  execution + teach-workspace build.
- **DEC-015 (NEW):** Python baseline = **rusty** → one **6.0001-primer teach lesson** in week 1
  (Python essentials: functions, lists, dicts, loops, recursion-light) before entering 6.0002;
  full 6.0001 not run.
- **DEC-016 (NEW):** Clock starts **now** — Phase 0 scaffolding the week of Aug 12; **Week 1 =
  Mon Aug 17**; window ends **Sun Oct 11** (8 weeks).

## Phase Roadmap (multiphase, feeds /plan)
- **Phase 0 (wk of Aug 12):** Build teach-workspace scaffold (MISSION.md, RESOURCES.md,
  GLOSSARY.md, NOTES.md, assets/stylesheet, lessons/ template), commit+push. Produce the window
  lesson map (DEC-005) and the week-1 Python diagnostic + primer lesson.
- **Phase 1 (weeks 1-8 = Aug 17 - Oct 11) — dual-track:**
  - **Wk 1:** 6.01SC units 1-2 (2 lessons); Python diagnostic + 6.0001-primer lesson; set cadence.
  - **Wk 2:** 6.01SC units 3-4; 6.0002 lecture units 1-2 + pset 1.
  - **Wk 3:** 6.01SC units 5-6; 6.002 starts (hw1-2); 6.0002 lecture units 3-4 + pset 2.
  - **Wk 4:** 6.01SC units 7-8 + **timed F11 + design lab (capstone 1)**; 6.002 hw3-4; 6.0002
    lecture unit 5 + pset 3. **Mid-window velocity checkpoint** (re-baseline the rest).
  - **Wk 5:** 6.002 hw5-6 + **timed quiz1**; 6.0002 lecture units 6-7 + pset 4.
  - **Wk 6 (buffer):** catch-up lane — 6.002 hw7-8, 6.0002 pset 5, or defer-swaps.
  - **Wk 7:** 6.002 hw9-10 + **timed quiz2**; 6.0002 final pset / review.
  - **Wk 8:** **6.002 timed final (capstone 2)**; 6.0002 final (timed) if pace held; phase-gate
    review, learning records, final commit; refresh Phase 2 plan.
  - Every week: 30-45 min agent session (Sun evening or Mon morning), one learning record,
    weekly git commit+push.
- **Phase 2 (months 3-5):** 6.002 remainder if the full arc slipped, then 6.003 signals & systems
  (full problem-set + solution set in folder).
- **Phase 3 (months 5-7):** 6.007 EM energy + 6.012 microelectronic devices (exam archives in
  folder).
- **Phase 4 (months 7-10):** The professional payoff — 6.061 power systems → 6.685 machines →
  6.622 power electronics (119 files incl. handwritten notes + design project).
- **Phase 5 (later, optional):** SE track deepens (6.042J → 6.006 → 6.033 → 6.046J...) as a
  parallel/successor track. Milestone review before Phase 5.

## Assumptions & Constraints
- **ASM-001:** 12-14h/week is sustainable for the full 8 weeks; revisit at the wk-4 checkpoint.
- **ASM-002 (HIGH RISK):** Teach-acceleration (retrieval lessons + skipping redundant video hours)
  compresses the ~260h nominal window scope (6.01SC ≈100h, 6.002 ≈100h, 6.0002 ≈60h) into
  ~100-110h available. Full 6.002 completion depends on >2x compression; checkpoints + DEC-011
  absorb slippage without abandoning the phase.
- **ASM-003:** The 3-month-old's sleep is volatile; wk 6 buffer + defer-don't-quit absorb it.
- **ASM-004:** One 6.0001-primer lesson is sufficient entry into 6.0002 at rusty-Python level.
- **CON-001:** No new downloads / no paid tools; everything uses the local curriculum + YouTube.
- **CON-002:** Lessons are English, HTML, self-contained, committed to the private repo.
- **CON-003:** 2-month window ends 2026-10-11; Phase 1 gates must close by then.

## Approaches Considered
- **Chosen:** Parallel dual-track teach-skill depth — EE core (6.01SC + 6.002) with SE track
  (6.0002) alongside, small HTML lessons with retrieval quizzes, weekly agent sessions, authentic
  exam+design-lab gates. Why: counters the documented OCW dropout mode; uses what's already local;
  both professional tracks progress simultaneously.
- **ALT-001:** EE-only serial Phase 1 (yesterday's auto plan) — **rejected by user today**: wants
  both tracks from day one.
- **ALT-002:** Pure self-study with the README curriculum maps, no teach workspace — rejected:
  reproduces the known failure mode.
- **ALT-003:** Start directly at the power courses (6.061/6.622) — rejected: presumes
  circuits/signals foundations.
- **ALT-004:** 2-month blitz on all 19 courses (surface-level) — rejected as dishonest: impossible
  at 12-14h/wk; produces fluency without storage strength.

## Out of Scope
- Downloading lecture videos (user instruction: YouTube links only).
- Running full 6.0001 (only a primer lesson; Python baseline is "rusty", not zero).
- Any paid credential, graded feedback, or certificate.
- Modifying the downloaded curriculum files (read-only study).
- 6.005/6.824 OCW-thin courses (supplementary links already noted in their READMEs).
- Completing all 19 courses inside this window (multi-phase by design).

## Open Questions
1. **Q-001:** What is the 6.0002 completion target by wk 8 — full course (all lecture units +
   all problem sets + timed final), or lectures + psets 1-5 + final if pace allows?
   - **Recommended default:** Lectures through unit 7 + psets 1-5 + timed final if pace allows;
     remaining psets defer to Phase 2.
   - **Why this matters:** Sets the SE-track gate; with the EE load (DEC-003), full-pset 6.0002
     completion may be the first thing to flex.

## Suggested Next Step
Run `/plan mit-ocw-two-month-completion` to turn this into a multi-phase implementation plan
(week-by-week Phase 1, teach-workspace scaffolding, lesson commissioning, gates).
