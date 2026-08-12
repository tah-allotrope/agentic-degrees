---
title: "MIT OCW Two-Month Completion — Dual-Track EE + SE Phase 1"
date: "2026-08-12"
status: "draft"
request: "A multi-phase, week-by-week plan to work through the downloaded MIT OCW material over the next 2 months using a teaching-workspace method"
plan_type: "multi-phase"
research_inputs:
  - "research/2026-08-12_mit-ocw-two-month-completion-brainstorm.md"
  - "research/2026-08-11_opencourseware-degrees.md"
---

# Plan: MIT OCW Two-Month Completion — Dual-Track EE + SE Phase 1

## Objective
Turn the 19-course MIT OpenCourseWare curriculum already downloaded into this repository into an
executed study program: build a self-contained teaching workspace at `teach-workspace/`, then run
eight weeks of dual-track study (electrical engineering + software engineering) from **Mon 2026-08-17
through Sun 2026-10-11** at 12–14 hours per week, closing each week with a written learning record
and a git commit. The material already exists and is free; the documented failure mode for open
courseware is non-completion, so this plan is about cadence, retrieval practice, and verifiable gates
— not about acquiring more content.

## Context Snapshot
- **Current state:** 19 MIT OCW courses (710 files, ~313 MB) are downloaded and organized under
  `mit-ocw-curriculum/` in two tracks. A research brief and a source ledger exist. The repository
  `tah-allotrope/agentic-degrees` (private, remote `origin`, branch `main`) has one commit. There is
  **no** teaching workspace, no study cadence, no learning records, no assessment history, and zero
  courses started.
- **Desired state:** `teach-workspace/` exists and is committed, containing `MISSION.md`,
  `RESOURCES.md`, `GLOSSARY.md`, `NOTES.md`, `PROGRESS.md`, `assets/`, `lessons/*.html`,
  `reference/*.html`, `learning-records/*.md`, `assessments/*.md`, `work/`, and
  `tools/verify_workspace.py`. Eight weeks of study are executed and evidenced: 6.01SC completed with
  a timed final and a capstone project, 6.002 driven through the full homework set with both timed
  quizzes and a timed final, 6.0002 entered via a Python primer and advanced through its problem
  sets. Every week has one learning record and one pushed commit.
- **Key repo surfaces:**
  - `mit-ocw-curriculum/electrical-engineering/01-intro-to-eecs-1-6.01SC/` — `README.md`,
    `syllabus.txt`, `videos.txt`, `manifest.json`, `software/tutorial.py`, `other/` (42 files:
    `MIT6_01SCS11_textbook.pdf`, `MIT6_01SCS11_chap01.pdf` … `chap08.pdf`, `MIT6_01SCS11_cmax.pdf`,
    `MIT6_01SCS11_hw1.pdf` … `hw4.pdf`, `hw1.zip` … `hw4.zip`, `swLab01.zip` … `swLab03.zip`,
    `designLab01.zip` … `designLab03.zip`, finals `MIT6_01SCS11_final_{S09,F09,S10,F10,S11}.pdf`
    each with a matching `_sol.pdf`, midterm solutions
    `MIT6_01SCS11_mid01_{F09,F10,S10,S11}_sol.pdf` and `MIT6_01SCS11_mid02_F10_sol.pdf`).
  - `mit-ocw-curriculum/electrical-engineering/02-circuits-and-electronics-6.002/` — `README.md`,
    `syllabus.txt`, `videos.txt`, `software/{prelab_3_2.m,prelab_3_5.m}`, `other/` (37 files:
    `hw1.pdf` … `hw10.pdf`, `lab0.pdf` … `lab4.pdf`, `lab_handout.pdf`, `labpractices.pdf`,
    `eesafety.pdf`, ten `demo_*.pdf`, `quiz1_{f03,f06,s04,s07}.pdf`, `quiz2_{f04,s04,s07}.pdf`,
    `final_f00.pdf`, `final_s07.pdf`). **No solution files and no lecture notes exist for 6.002.**
  - `mit-ocw-curriculum/software-engineering/02-computation-data-science-6.0002/` — `README.md`,
    `syllabus.txt`, `videos.txt`, `software/{lect5.py,python-install.zip}`, `other/` (16 files:
    `MIT6_0002F16_lec1.pdf` … `lec8.pdf`, `MIT6_0002F16_StyleGuide.pdf`,
    `MIT6_0002F16_PythonResurcs.pdf`, `Lecture1.zip`, `PS1.zip` … `PS5.zip`).
  - `mit-ocw-curriculum/software-engineering/01-intro-to-cs-python-6.0001/` — `other/`
    (`MIT6_0001F16_Lec1.pdf` … `Lec5.pdf`, `MIT6_0001F16_ps1.pdf`, `ps0.zip`, `ps2.zip`, `PS3.zip`,
    `ps4.zip`, `ps5.zip`, `MIT6_0001F16_StyleGuide.pdf`, `MIT6_0001F16_additional.pdf`).
  - `mit-ocw-curriculum/README.md` — the 19-course curriculum map and prerequisite ordering.
  - `curriculum.json`, `download_ocw.py`, `fix_videos_622.py` — the downloader tooling that produced
    the tree. **Not touched by this plan.**
- **Out of scope:**
  - Downloading lecture videos. Videos are streamed from YouTube only.
  - Running the full 6.0001 course (a single Python primer lesson only).
  - Any paid credential, certificate, tutor, or graded feedback service.
  - Modifying anything under `mit-ocw-curriculum/` — that tree is read-only study material.
  - Courses 6.005 and 6.824 (thin OCW material; noted in their own READMEs).
  - Completing all 19 courses inside this window. Phases 2–5 are sketched, not executed.

## Environment & Conventions
- **Stack:** No application runtime. Deliverables are Markdown files, self-contained HTML lesson
  files (no build step, no external CDN), and small standard-library Python scripts. Python 3.11 is
  installed and on `PATH` as `python` (verify with `python --version`). Git 2.x is installed; the
  repository is at the paths shown below with remote `origin` =
  `https://github.com/tah-allotrope/agentic-degrees.git`, working branch `main`.
- **Setup:** No project-wide dependency install exists or is needed for the workspace itself. The
  only dependency-bearing work is the 6.0002 problem sets:
  ```
  python -m venv teach-workspace/.venv
  teach-workspace/.venv/Scripts/python -m pip install --upgrade pip
  teach-workspace/.venv/Scripts/python -m pip install matplotlib numpy
  ```
  (On macOS/Linux the interpreter path is `teach-workspace/.venv/bin/python`.) `matplotlib` and
  `numpy` are required by `ps3_visualize.py` and by the plotting sections of PS4/PS5. Nothing else
  is installed.
- **Build / Run:** There is no build. To open a lesson, launch the HTML file in the default browser:
  - Windows: `start "" teach-workspace/lessons/0001-python-essentials-primer.html`
  - macOS: `open teach-workspace/lessons/0001-python-essentials-primer.html`
  - Linux: `xdg-open teach-workspace/lessons/0001-python-essentials-primer.html`
- **Test:** Full suite: `python -m unittest discover -s teach-workspace/tools -p "test_*.py" -v`
  (standard library `unittest`; no pytest, no CI in this repo). Single test:
  `python -m unittest teach-workspace.tools.test_verify_workspace.TestCheckNumbering.test_gap -v`.
  Workspace integrity check: `python teach-workspace/tools/verify_workspace.py teach-workspace`.
  Course problem-set checks are the scripts shipped inside the OCW zips, run from the extracted
  directory — e.g. `python ps3_tests_f16.py`, `python ps4_tests.py`, `python ps5_test.py`.
- **Conventions & traps:**
  - **Timezone:** all dates and times in this plan are `Asia/Ho_Chi_Minh` (UTC+7). Weeks run Monday
    → Sunday. "Week 1" = Mon 2026-08-17 … Sun 2026-08-23. "Week 8" = Mon 2026-10-05 … Sun 2026-10-11.
  - **Units:** study effort is measured in hours per week (`h/week`) of focused time; exam durations
    are in minutes; exam scores are percentages of the paper's own point total.
  - **Numbering:** lessons are `teach-workspace/lessons/NNNN-<dash-case-slug>.html`; learning records
    are `teach-workspace/learning-records/NNNN-<dash-case-slug>.md`; both use a zero-padded 4-digit
    integer that is `max(existing) + 1`, starting at `0001`. The two sequences are **independent**.
  - **Assessment records** are `teach-workspace/assessments/YYYY-MM-DD-<exam-id>.md`, e.g.
    `2026-09-13-601sc-final-S11.md`.
  - **Language:** English, for every artifact.
  - **Read-only curriculum:** never write into `mit-ocw-curriculum/`. Extract zips into
    `teach-workspace/work/<course>/` instead.
  - **Style:** Markdown wrapped at 100 columns; HTML lessons must link the shared stylesheet
    `../assets/style.css` rather than inlining styles; Python follows PEP 8 with 4-space indents and
    no third-party imports in `teach-workspace/tools/`.
- **Repo map:**
  ```
  agentic-degrees/
  ├── curriculum.json            # 19-course descriptor used by the downloader
  ├── download_ocw.py            # downloader (do not run again; material is complete)
  ├── fix_videos_622.py          # one-off video-link fixer (not used by this plan)
  ├── mit-ocw-curriculum/        # READ-ONLY study material
  │   ├── README.md              # curriculum map + prerequisite order
  │   ├── electrical-engineering/01-intro-to-eecs-1-6.01SC/{README.md,syllabus.txt,videos.txt,other/,software/}
  │   ├── electrical-engineering/02-circuits-and-electronics-6.002/{…}
  │   └── software-engineering/02-computation-data-science-6.0002/{…}
  ├── research/                  # research briefs (input to this plan)
  ├── plans/                     # this plan
  └── teach-workspace/           # CREATED BY THIS PLAN
  ```

## Research Inputs
- From `research/2026-08-12_mit-ocw-two-month-completion-brainstorm.md` (interactively confirmed
  decisions, superseding an earlier auto-generated draft):
  - The mission is **dual-track from day one**: an EE core aimed at battery-energy-storage / grid /
    electrical-machines fluency for professional work, **plus** the software-engineering track in
    parallel. An EE-first, SE-second ordering was explicitly rejected.
  - Budget is **12–14 h/week split 60/40 EE/SE**, delivered as 4–5 weekday morning sessions of
    60–75 minutes plus one weekend block of 2–4 hours. Total available in the window ≈ 96–112 h.
  - Window scope: 6.01SC complete (timed final + design-lab capstone), 6.002 complete (hw1–hw10,
    both timed quizzes, timed final), 6.0002 entered and substantially advanced.
  - The scope is deliberately aggressive: the nominal MIT contact-hour load for these three courses
    is roughly 260 h against ~100–110 h available, i.e. it depends on better than 2× compression.
    The safety valves are a mid-window velocity checkpoint at the end of week 4, a dedicated buffer
    week 6, and a standing **"defer, don't quit"** rule — any unit stalling more than one week is
    logged as deferred with a re-entry plan instead of being abandoned.
  - Personal constraints that shape pacing: a full-time country-director job and a child born
    May 2026, so sleep and evenings are volatile; morning sessions are the reliable slot.
  - Python baseline is **rusty, not zero** → one primer lesson (functions, lists, dicts, loops,
    light recursion) before entering 6.0002; the full 6.0001 course is not run.
  - Videos are **streamed from YouTube only**, never downloaded; lessons link the relevant lecture
    as a primary source.
  - Progress tracking = learning records plus a weekly git commit and push of the workspace.
- From `research/2026-08-11_opencourseware-degrees.md` (the exhaustive OCW ranking brief):
  - The literature splits cleanly: open materials perform at least as well as commercial ones
    (Hilton 2016, OER efficacy review, https://doi.org/10.1007/s11528-015-0841-0), while
    **completion is the documented weak point** of self-paced open courseware (Daniel 2012,
    https://doi.org/10.1080/01587919.2012.723161; "Understanding Dropouts in MOOCs", 2019,
    https://doi.org/10.1016/j.iheduc.2019.04.001, which attributes attrition to time, prior
    experience, and motivation). Planning implication carried into this plan: pair the free material
    with accountability structure — a public-to-self progress repo, fixed weekly gates, and timed
    exams — rather than relying on the material alone.
  - No accredited free engineering degree exists anywhere; the honest target is a degree-shaped free
    curriculum. Credentials and graded feedback are the paid parts everywhere, which is why every
    gate in this plan is self-administered and self-graded against an explicit rubric.
  - MIT OCW was selected over TU Delft OCW, OpenLearn, and edX audit tracks specifically because its
    course pages ship exams and (for most courses) solutions — verified on the 6.002, 6.01SC, 6.685
    and 6.622 pages. This is why authentic past exams are the primary gate mechanism here.
  - Community accountability is the recommended complement (OSSU Discord and similar are active);
    the workspace's `RESOURCES.md` carries a Wisdom section for this.

## Assumptions and Constraints
- **ASM-001:** 12–14 h/week is sustainable for the full eight weeks. Re-baselined at the week-4
  checkpoint using the rule in `## Specification` §3.
- **ASM-002 (HIGH RISK):** Retrieval-practice lessons plus skipping redundant lecture-video hours
  compress ~260 h of nominal material into ~100–110 h of study. Full 6.002 completion depends on
  this. The week-4 checkpoint and the defer rule absorb slippage without abandoning the phase.
- **ASM-003:** The brainstorm names the 6.01SC capstone exam as "F11". **No F11 final exists in the
  repository.** The available finals are `MIT6_01SCS11_final_{S09,F09,S10,F10,S11}.pdf`, each with a
  matching `_sol.pdf`. — **BINDING DEFAULT:** the graded capstone exam is
  `MIT6_01SCS11_final_S11.pdf` (the paper matching the Spring 2011 course version that the notes and
  labs come from), graded against `MIT6_01SCS11_final_S11_sol.pdf`. `MIT6_01SCS11_final_F10.pdf` is
  the optional untimed dry run; `final_S09`, `final_F09`, `final_S10` are held in reserve for retakes.
- **ASM-004:** 6.01SC midterms exist **only as solution files** (`mid01_F09_sol.pdf`,
  `mid01_F10_sol.pdf`, `mid01_S10_sol.pdf`, `mid01_S11_sol.pdf`, `mid02_F10_sol.pdf`) — the blank
  papers were not published. — **BINDING DEFAULT:** treat midterm solutions as worked examples to
  read *after* attempting the corresponding homework, never as timed assessments. Do not schedule a
  6.01SC midterm gate.
- **ASM-005:** 6.002 (OCW Spring 2007) ships **no solutions at all** — not for hw1–hw10, not for the
  quizzes, not for the finals; `syllabus.txt` lists its resource types as Exams, Lecture Videos, and
  Problem Sets only. — **BINDING DEFAULT:** grade all 6.002 work with the dual-method self-grading
  protocol in `## Specification` §4 (solve, then independently re-derive by a second method and/or
  check numerically in Python), and record a confidence rating plus open questions in the assessment
  file. Never treat an ungraded 6.002 answer as verified.
- **ASM-006:** The 6.01SC design-lab and homework zips are skeleton files that import the MIT `lib601`
  / `soar` robot-simulator package and assume physical robot hardware. Neither is present —
  `software/` contains only `tutorial.py`. — **BINDING DEFAULT:** the capstone project is implemented
  in **pure standard-library Python** inside `teach-workspace/work/6.01SC/capstone/`: reimplement the
  state-machine composition and the proportional/PD wall-following controller from the
  `designLab02`/`designLab03` skeletons against a hand-written 40-line kinematic simulator stub
  written as part of the capstone. No external package, no hardware, no download.
- **ASM-007:** `mit-ocw-curriculum/electrical-engineering/02-circuits-and-electronics-6.002/videos.txt`
  names only Lecture 1 and Lecture 25 explicitly; the rest are behind the MIT OCW YouTube channel
  link. — **BINDING DEFAULT:** in week 3, resolve the 6.002 lecture list once from the OCW course page
  `https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/` and record the resolved
  per-lecture YouTube URLs in `teach-workspace/RESOURCES.md`. Do **not** edit `videos.txt` or anything
  else under `mit-ocw-curriculum/`.
- **ASM-008:** Only lecture slide decks 1–8 of 6.0002 are downloaded locally; the Fall 2016 course
  runs longer. — **BINDING DEFAULT:** the local decks define the required scope; any lecture beyond
  deck 8 is streamed from the MIT OCW YouTube playlist and is optional stretch work.
- **ASM-009:** Lecture-topic labels used in the lesson maps below follow the published course
  sequences. — **BINDING DEFAULT:** if a slide deck's or chapter's actual title differs from the
  label used here, keep the deck/chapter **order** as authoritative and rename the lesson to match
  the real title; do not reorder the schedule.
- **ASM-010:** The brainstorm left one open question — the 6.0002 completion target by week 8. The
  local material contains exactly five problem sets (PS1–PS5) and **no exam**. — **BINDING DEFAULT:**
  the software-track gate is PS1–PS3 completed and passing their bundled test scripts by end of week 6
  (mandatory), PS4–PS5 by end of week 8 (target, deferrable to Phase 2 under the rule in
  `## Specification` §3), plus one 90-minute self-written timed synthesis assessment drawn from decks
  1–8 in week 8. There is no 6.0002 final exam to sit.
- **ASM-011:** 6.0002 problem-set code was written for Python 3.5 and the zips contain stale
  `__pycache__` artifacts (`ps3.cpython-35.pyc`, `ps3_verify_movement27.cpython-35.pyc`, `test.pyc`).
  — **BINDING DEFAULT:** run the `.py` sources under Python 3.11 in the workspace virtualenv, delete
  extracted `.pyc` files immediately after extraction, and fix any incompatibility in the extracted
  copy under `teach-workspace/work/` (never in the curriculum tree), logging the fix in `NOTES.md`.
- **ASM-012:** Exam durations are taken from each paper's own cover page. — **BINDING DEFAULT:** when
  a paper states no duration, use 180 minutes for a final and 90 minutes for a quiz.
- **CON-001:** No new course downloads, no paid tools, no paid services. Everything runs on the local
  curriculum tree, streamed YouTube lectures, and the Python standard library plus `matplotlib`/`numpy`.
- **CON-002:** All lessons are English, HTML, self-contained (no external CDN, no network fetch at
  view time), and committed to the private repository.
- **CON-003:** The window closes Sun 2026-10-11. Every Phase-1 gate must be attempted before then;
  anything unattempted is explicitly deferred in writing, not silently dropped.
- **DEC-001:** Dual-track from day one — EE core plus SE track in parallel, not sequentially.
- **DEC-002:** 12–14 h/week, 60/40 EE/SE split.
- **DEC-003:** Window scope = 6.01SC complete + 6.002 full arc + 6.0002 substantially advanced.
- **DEC-004:** The workspace lives at `teach-workspace/` inside this repository and is committed.
- **DEC-005:** Lesson granularity = one to two tightly-scoped lessons per course unit, each with a
  retrieval quiz and an explicit tie to `MISSION.md`. Window lesson map ≈ 10 for 6.01SC, ~12 for
  6.002, ~8 for 6.0002 including the primer.
- **DEC-006:** `RESOURCES.md` is curated from the downloaded material (syllabi, lecture-note PDFs,
  video playlists) plus the canonical textbooks: Agarwal & Lang for 6.002, Oppenheim for 6.003,
  Guttag for 6.0001/6.0002.
- **DEC-007:** Two assessment gates per course: weekly in-lesson retrieval quizzes, and the course's
  own past exams sat under time and graded (against published solutions where they exist — see
  ASM-005 for 6.002).
- **DEC-008:** A 30–45 minute weekly teaching/review session, Sunday evening or Monday morning:
  review the week's learning records, take a synthesis quiz, commission the next week's lessons.
- **DEC-009:** Videos streamed from YouTube only, never downloaded.
- **DEC-010:** Progress tracked by learning records plus a weekly commit and push of
  `teach-workspace/`.
- **DEC-011:** "Defer, don't quit" — see `## Specification` §3.
- **DEC-012:** Phase-1 capstone 1 = timed 6.01SC final plus the design-lab project; capstone 2 = the
  timed 6.002 final.
- **DEC-013:** All lessons in English.
- **DEC-014:** No new downloads; this is pure execution plus workspace construction.
- **DEC-015:** One 6.0001-derived Python primer lesson in week 0, not the full 6.0001 course.
- **DEC-016:** Week 1 starts Mon 2026-08-17; the window ends Sun 2026-10-11.

## Specification

### §1 Weekly time budget

Let `H` be the hours studied in a given week, `E` the electrical-engineering hours, and `S` the
software-engineering hours.

```
H  ∈ [12, 14]        hours per calendar week (Mon–Sun)
E  = 0.60 × H        → 7.2 h ≤ E ≤ 8.4 h
S  = 0.40 × H        → 4.8 h ≤ S ≤ 5.6 h
H  = Σ(weekday sessions) + weekend_block
     weekday sessions: 4 or 5 sessions × 60–75 min  = 4.0–6.25 h
     weekend_block:    1 block × 2–4 h
Window total = Σ(H over weeks 1..8) ∈ [96, 112] hours
```

Symbol meanings: `H` = total focused study hours logged in `PROGRESS.md` for that week, excluding
breaks and excluding the weekly review session; `E` = hours spent on 6.01SC and 6.002 combined;
`S` = hours spent on 6.0002 and the Python primer combined. The weekly review session (30–45 min,
DEC-008) is logged separately and is not counted inside `H`.

### §2 Exam scoring and pass thresholds

For any sat paper, let `p` = points earned and `P` = the paper's stated total points. If the paper
states no point total, assign 1 point per sub-question and use the resulting count as `P`.

```
Score = 100 × p / P        (percent, one decimal place)

Score ≥ 70.0            → PASS. Record and move on.
55.0 ≤ Score < 70.0     → PARTIAL. Write one targeted remediation lesson on the two weakest
                          topics, then re-sit a different year's paper within 7 days.
Score < 55.0            → FAIL. Re-study the unit (re-read the chapter, redo the homework),
                          then re-sit a different year's paper. Log a deferral if this pushes
                          any other scheduled item out of its week.
```

### §3 Week-4 velocity checkpoint and the defer-don't-quit rule

At the end of week 4 (Sun 2026-09-13), compute:

```
V = C / 20

C = number of the 20 scheduled week-1..week-4 deliverables actually completed,
    counted from the PROGRESS.md checklist for weeks 1–4 (each lesson authored = 1,
    each homework completed = 1, each problem set passing its tests = 1,
    each timed exam sat = 1).
```

Apply exactly one branch:

1. `V ≥ 0.85` → keep the full scope unchanged for weeks 5–8.
2. `0.60 ≤ V < 0.85` → move 6.0002 PS4 and PS5 to Phase 2. Keep every EE item. Record the change as
   a deferral entry (below).
3. `V < 0.60` → additionally move the 6.002 timed final to Phase 2, keep both 6.002 quizzes, and
   reduce week-7/8 6.002 homework to hw9 only. Record the deferral.

**Defer-don't-quit rule (applies at any time, not just week 4):** when any single unit has consumed
more than one calendar week without reaching its exit criterion, stop working it that week and:

1. Append a deferral entry to `teach-workspace/PROGRESS.md` under `## Deferrals` with: date, item,
   the reason, the specific re-entry trigger, and the phase it moves to.
2. Write a learning record naming the concrete sticking point (not "ran out of time").
3. Swap in the next-lightest scheduled item from the same track so the week still closes with work
   completed.

Nothing is ever deleted from the scope — it is moved with a written re-entry plan.

### §4 6.002 dual-method self-grading protocol (required — no solutions exist)

For each 6.002 homework problem and each quiz/final question:

1. Solve it once, writing the full working in
   `teach-workspace/work/6.002/hw<N>/solution.md` (or `assessments/<file>.md` for exams).
2. Re-derive the same numeric answer by a **different** method. Acceptable second methods, in order
   of preference: node method vs. Thévenin/Norton equivalent; superposition vs. direct solve;
   symbolic result evaluated numerically in a small Python snippet stored beside the solution;
   limiting-case sanity check (set a component to 0 or ∞ and confirm the expression degenerates
   correctly); dimensional analysis on the symbolic result.
3. Record a confidence rating: `high` (both methods agree), `medium` (one method plus a passing
   limiting-case check), `low` (single method only).
4. For exams, `p` in §2 counts only questions rated `high` or `medium` as correct; every `low`
   question counts as zero and is added to the open-questions list at the bottom of the assessment
   file for the next weekly review session.

### §5 Teaching-workspace file contract

The workspace is self-describing; these formats are the contract, restated here so no external
document is needed.

- `MISSION.md` — one per workspace, under one screen. Sections: `# Mission: {topic}`, `## Why`
  (1–3 sentences naming the concrete real-world outcome, not "to understand X"),
  `## Success looks like` (observable capabilities), `## Constraints`, `## Out of scope`.
- `RESOURCES.md` — `# {Topic} Resources`, then `## Knowledge` and `## Wisdom (Communities)`. Every
  entry is a link plus a one-line annotation saying what it covers and when to reach for it. A
  `## Gaps` section lists areas where no good resource was found.
- `GLOSSARY.md` — `# {Topic} Glossary`, a one-sentence topic description, then `## Terms` with
  entries of the form `**Term**:` / one-to-two-sentence definition / `_Avoid_: alias, alias`. A term
  is added only once it has been used correctly, not when first encountered.
- `learning-records/NNNN-slug.md` — a title line plus one to three sentences: what was learned or
  established, and why it changes what to teach next. Optional `Status: superseded by LR-NNNN`
  frontmatter, `Evidence`, and `Implications` sections. Written when understanding is demonstrated,
  when prior knowledge is disclosed, when a misconception is corrected, or when the mission shifts —
  never as an activity log.
- `lessons/NNNN-slug.html` — one self-contained HTML file teaching one tightly-scoped thing.
  Required elements, all verified by `tools/verify_workspace.py`:
  1. `<link rel="stylesheet" href="../assets/style.css">` — never inline styles.
  2. A `Primary source` link to the highest-quality source for the topic (the OCW PDF, the specific
     YouTube lecture, or the textbook chapter).
  3. A link back to `../MISSION.md` stating in one sentence how this lesson serves the mission.
  4. A retrieval quiz section marked `<section class="quiz">` with at least three questions where
     every answer option for a given question has the same word count (and, where practical, the
     same character count) so formatting leaks no clue.
  5. A closing reminder to ask the teaching agent follow-up questions.
- `reference/*.html` — compressed, print-friendly cheat sheets (formula sheets, algorithm cards).
  Lessons are read once; reference documents are read repeatedly.
- `assets/` — shared components, starting with `style.css` and `quiz.js`. Reuse is the default: read
  `assets/` before authoring any lesson and add to it rather than duplicating code inline.

### §6 Weekly cadence (identical every week, weeks 1–8)

1. **Mon–Fri, 4–5 mornings, 60–75 min each:** work the scheduled lesson or homework for that day.
2. **Sat or Sun, one 2–4 h block:** the week's heavy item (a lab, a problem set, or a timed exam).
3. **Sun evening (or Mon 06:00) — 30–45 min review session:** re-read the week's learning records,
   take a mixed synthesis quiz drawn from *previous* weeks (spacing + interleaving, not this week's
   material), update `GLOSSARY.md`, and commission the next week's lessons.
4. **Immediately after the review session:** update `PROGRESS.md` (hours, checklist, deferrals),
   write the week's learning record, run
   `python teach-workspace/tools/verify_workspace.py teach-workspace`, then:
   ```
   git add teach-workspace plans
   git commit -m "teach: week NN — <one-line summary of what closed>"
   git push origin main
   ```

## Phase Summary
| Phase | Goal | Dependencies | Primary outputs |
|---|---|---|---|
| PHASE-01 | Build and verify the teaching workspace (Wed 2026-08-12 → Sun 2026-08-16) | None | `teach-workspace/` scaffold, `tools/verify_workspace.py` + tests, lesson 0001 Python primer, full lesson map, first commit |
| PHASE-02 | Weeks 1–2 (2026-08-17 → 2026-08-30): launch dual-track cadence | PHASE-01 | 6.01SC chapters 1–4 lessons + hw1–hw2 + swLab01–02, 6.0002 decks 1–2 + PS1, 2 learning records, 2 commits |
| PHASE-03 | Weeks 3–4 (2026-08-31 → 2026-09-13): open 6.002, sit capstone 1, run the velocity checkpoint | PHASE-02 | 6.01SC finished + timed final S11 + design-lab capstone, 6.002 lessons 1–4 + hw1–hw4, 6.0002 decks 3–5 + PS2–PS3, checkpoint decision recorded |
| PHASE-04 | Weeks 5–6 (2026-09-14 → 2026-09-27): 6.002 quiz 1 and the buffer week | PHASE-03 | 6.002 lessons 5–8 + hw5–hw8 + timed quiz 1, 6.0002 decks 6–7 + PS4, all deferrals cleared or re-planned |
| PHASE-05 | Weeks 7–8 (2026-09-28 → 2026-10-11): 6.002 quiz 2, capstone 2, phase gate | PHASE-04 | 6.002 lessons 9–12 + hw9–hw10 + timed quiz 2 + timed final, 6.0002 PS5 + timed synthesis assessment, phase-gate review |
| PHASE-06 | Close the window and hand off to Phase 2 (by Mon 2026-10-12) | PHASE-05 | `PHASE-1-REVIEW.md`, refreshed `ROADMAP.md` for Phases 2–5, updated mission, final commit |

## Detailed Phases

### PHASE-01 - Workspace Scaffold and Lesson Map
**Goal**
By Sun 2026-08-16, a committed, verifiable `teach-workspace/` exists with its mission, resources,
shared assets, integrity checker, the full eight-week lesson map, and lesson 0001 (the Python primer
plus a diagnostic) ready to take on Monday morning. Zero course study happens in this phase.

**Tasks**
- [ ] TASK-01-01: Create the directory skeleton exactly:
      `teach-workspace/{assets,lessons,reference,learning-records,assessments,tools,work}` and
      `teach-workspace/work/{6.01SC,6.002,6.0002}`. Add `teach-workspace/.gitignore` containing
      `__pycache__/`, `*.pyc`, `.venv/`.
- [ ] TASK-01-02: Write `teach-workspace/MISSION.md` per §5. `## Why` states the professional
      outcome: being able to read a battery-energy-storage or grid one-line diagram, size and sanity-
      check power-electronics and machine specifications, and write the computational models that
      support those decisions — without deferring to a consultant. `## Success looks like` lists:
      analyse an arbitrary resistive network by the node method under time pressure; predict the
      transient and frequency response of a first- and second-order circuit; design a proportional
      controller and state its stability condition; build a state-machine model of a physical system
      in Python; run a Monte Carlo simulation and state a confidence interval correctly.
      `## Constraints` records 12–14 h/week, mornings, an infant at home, the 2026-10-11 window.
      `## Out of scope` mirrors this plan's Out of scope list.
- [ ] TASK-01-03: Write `teach-workspace/RESOURCES.md` per §5. `## Knowledge` must contain, at
      minimum, one annotated entry each for: the 6.01SC course notes
      (`../mit-ocw-curriculum/electrical-engineering/01-intro-to-eecs-1-6.01SC/other/MIT6_01SCS11_textbook.pdf`),
      the 6.01SC OCW page and YouTube playlist from that course's `videos.txt`, the 6.002 OCW page
      `https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/`, the 6.002 textbook
      (Agarwal & Lang, *Foundations of Analog and Digital Electronic Circuits*, ISBN 9781558607354 —
      reference only; not required to buy), the 6.0002 slide decks, Guttag's *Introduction to
      Computation and Programming Using Python*, and Oppenheim's *Signals and Systems* (for Phase 2).
      `## Wisdom (Communities)` lists at least two active, well-moderated communities for
      accountability and question-asking. Add a `## Gaps` section that records explicitly: *no
      solutions are published for 6.002 — see the dual-method self-grading protocol*.
- [ ] TASK-01-04: Write `teach-workspace/GLOSSARY.md` with the header, the topic sentence, and an
      empty `## Terms` section. Terms are added only as they are demonstrably understood.
- [ ] TASK-01-05: Write `teach-workspace/NOTES.md` recording the working preferences that shape
      lesson design: 60–75 minute morning sessions, English, retrieval-practice-first, no video
      downloads, prefers worked numeric examples over prose, and the standing rule that the
      curriculum tree is read-only.
- [ ] TASK-01-06: Write `teach-workspace/PROGRESS.md` containing (a) an `## Hours` table with columns
      `Week | Dates | EE h | SE h | Total h | Review session (y/n)`, pre-filled with the eight week
      rows and their exact date ranges (Week 1 2026-08-17→2026-08-23, Week 2 08-24→08-30, Week 3
      08-31→09-06, Week 4 09-07→09-13, Week 5 09-14→09-20, Week 6 09-21→09-27, Week 7 09-28→10-04,
      Week 8 10-05→10-11); (b) a `## Checklist` section with one unchecked box per deliverable from
      PHASE-02 through PHASE-05, grouped by week; (c) an empty `## Deferrals` section with the column
      header `Date | Item | Reason | Re-entry trigger | Moved to`.
- [ ] TASK-01-07: Write `teach-workspace/assets/style.css` — a single print-friendly stylesheet:
      a readable serif body at 1.6 line-height with a max content width of 38rem, sans-serif headings,
      a `.quiz` block style, a `.callout` style, a monospace `code`/`pre` style, and an
      `@media print` block that hides quiz answer reveals and forces black-on-white.
- [ ] TASK-01-08: Write `teach-workspace/assets/quiz.js` — dependency-free vanilla JavaScript that
      finds every `<section class="quiz">`, renders each `<li data-answer="…">` option as a clickable
      button, reveals correct/incorrect immediately on click, and shows a running score. No external
      library, no network call.
- [ ] TASK-01-09: Write the failing tests first at
      `teach-workspace/tools/test_verify_workspace.py` (see **Test Specs**), run them, confirm they
      fail because `verify_workspace.py` does not exist yet, then implement
      `teach-workspace/tools/verify_workspace.py` until they pass.
- [ ] TASK-01-10: Write `teach-workspace/LESSON-MAP.md` — the full eight-week lesson map, one row per
      planned lesson with columns `Week | Track | Slug | Source material | Retrieval focus`. Use the
      slugs listed in the PHASE-02…PHASE-05 File Changes sections verbatim. Lesson numbers are left
      blank and filled in when each lesson is authored (numbers are assigned at creation time per the
      numbering convention).
- [ ] TASK-01-11: Author lesson `0001-python-essentials-primer.html` from
      `mit-ocw-curriculum/software-engineering/01-intro-to-cs-python-6.0001/other/MIT6_0001F16_Lec1.pdf`
      through `Lec5.pdf` and `MIT6_0001F16_StyleGuide.pdf`. Scope: functions and scope, list and dict
      operations, comprehensions, iteration patterns, tuple unpacking, one light recursion example,
      and the 6.0001 style rules. It must contain a 10-question diagnostic quiz whose result is
      recorded in learning record `0001` (see TASK-01-12), and must satisfy every requirement in §5.
- [ ] TASK-01-12: Take the diagnostic in lesson 0001 and write
      `teach-workspace/learning-records/0001-python-baseline.md` recording the diagnostic score, which
      of the seven primer topics were shaky, and the resulting rule for 6.0002 lessons (e.g. "dict
      comprehensions need re-teaching inside the PS1 lesson").
- [ ] TASK-01-13: Delete the superseded brainstorm draft
      `research/2026-08-11_mit-ocw-two-month-completion-brainstorm.md` so only the confirmed
      2026-08-12 brief remains as the planning source of record.
- [ ] TASK-01-14: Create the virtualenv and install the two required packages using the commands in
      `## Environment & Conventions → Setup`. Confirm with
      `teach-workspace/.venv/Scripts/python -c "import matplotlib, numpy; print('deps ok')"`.
- [ ] TASK-01-15: Run the workspace checker and the unit tests (see **Exit Criteria**), then commit
      and push with message `teach: phase 0 — workspace scaffold, lesson map, python primer`.

**File Changes**
- `teach-workspace/.gitignore` (create): the three ignore lines listed in TASK-01-01. Nothing else.
- `teach-workspace/MISSION.md` (create): per TASK-01-02. One screen maximum.
- `teach-workspace/RESOURCES.md` (create): per TASK-01-03, with `## Knowledge`, `## Wisdom
  (Communities)`, and `## Gaps`.
- `teach-workspace/GLOSSARY.md` (create): header plus empty `## Terms`.
- `teach-workspace/NOTES.md` (create): per TASK-01-05.
- `teach-workspace/PROGRESS.md` (create): per TASK-01-06, all eight week rows pre-filled.
- `teach-workspace/LESSON-MAP.md` (create): per TASK-01-10.
- `teach-workspace/assets/style.css` (create): per TASK-01-07.
- `teach-workspace/assets/quiz.js` (create): per TASK-01-08.
- `teach-workspace/tools/verify_workspace.py` (create): the checker, standard library only.
- `teach-workspace/tools/test_verify_workspace.py` (create): the unit tests, `unittest` only.
- `teach-workspace/lessons/0001-python-essentials-primer.html` (create): per TASK-01-11.
- `teach-workspace/learning-records/0001-python-baseline.md` (create): per TASK-01-12.
- `research/2026-08-11_mit-ocw-two-month-completion-brainstorm.md` (delete): superseded draft.
- `mit-ocw-curriculum/**` (leave alone): read-only. No file in this tree is created, modified, or
  deleted by any phase of this plan.
- `curriculum.json`, `download_ocw.py`, `fix_videos_622.py` (leave alone).

**Function Signatures**
All in `teach-workspace/tools/verify_workspace.py`, standard library only
(`pathlib`, `re`, `sys`, `argparse`):

- `scan_numbered(directory: pathlib.Path, suffix: str) -> list[tuple[int, pathlib.Path]]` — returns
  `(number, path)` pairs for every file in `directory` whose name matches
  `^(\d{4})-[a-z0-9-]+<suffix>$`, sorted ascending by number; returns `[]` when the directory does
  not exist; silently ignores non-matching filenames.
- `check_numbering(items: list[tuple[int, pathlib.Path]], label: str) -> list[str]` — returns a list
  of human-readable problem strings for duplicate numbers and for gaps in the sequence starting at 1;
  returns `[]` when the sequence is contiguous from `0001` or when `items` is empty.
- `check_lesson(path: pathlib.Path) -> list[str]` — returns one problem string per missing required
  lesson element (stylesheet link, primary source, mission link, quiz section); returns `[]` for a
  fully conformant lesson.
- `check_required_files(workspace: pathlib.Path) -> list[str]` — returns one problem string per
  missing required workspace file among `MISSION.md`, `RESOURCES.md`, `GLOSSARY.md`, `NOTES.md`,
  `PROGRESS.md`, `LESSON-MAP.md`, `assets/style.css`, `assets/quiz.js`.
- `collect_problems(workspace: pathlib.Path) -> list[str]` — runs all four checks over the workspace
  and returns the concatenated problem list in the order: required files, lesson numbering, record
  numbering, per-lesson checks.
- `main(argv: list[str]) -> int` — parses one optional positional argument (the workspace directory,
  default `teach-workspace`), prints either
  `OK: {n} lessons, {m} records, 0 problems` or the problem list followed by
  `FAIL: {k} problems`, and returns `0` on success, `1` when problems exist.

**Test Specs**
Written before the implementation, in `teach-workspace/tools/test_verify_workspace.py`, each using a
`tempfile.TemporaryDirectory()` fixture:

- `check_numbering([(1, Path("0001-a.html")), (2, Path("0002-b.html"))], "lessons")` → `[]`
- `check_numbering([(1, Path("0001-a.html")), (3, Path("0003-c.html"))], "lessons")` →
  `["lessons: gap at 0002"]`
- `check_numbering([(1, Path("0001-a.html")), (1, Path("0001-b.html"))], "lessons")` →
  `["lessons: duplicate number 0001"]`
- `check_numbering([], "lessons")` → `[]`
- `check_numbering([(2, Path("0002-a.html"))], "lessons")` → `["lessons: gap at 0001"]`
- `scan_numbered(<dir containing "0001-x.html", "notes.txt", "0010-y.html">, ".html")` →
  `[(1, <dir>/0001-x.html), (10, <dir>/0010-y.html)]` — the non-matching `notes.txt` is ignored.
- `scan_numbered(<path that does not exist>, ".html")` → `[]`
- `check_lesson(<file containing all four required elements>)` → `[]`
- `check_lesson(<file with no stylesheet link>)` → `["0001-x.html: missing assets/style.css link"]`
- `check_lesson(<file with no 'Primary source' text>)` → `["0001-x.html: missing primary source"]`
- `check_lesson(<file with no href to ../MISSION.md>)` → `["0001-x.html: missing mission link"]`
- `check_lesson(<file with no <section class="quiz">>)` → `["0001-x.html: missing quiz section"]`
- `check_required_files(<workspace missing GLOSSARY.md only>)` → `["missing required file: GLOSSARY.md"]`
- `main(["<complete valid workspace>"])` → returns `0` and prints a line starting with `OK:`
- `main(["<workspace missing NOTES.md>"])` → returns `1` and prints a final line starting with `FAIL:`

**Dependencies**
- Python 3.11 on `PATH`. No third-party packages for the tools themselves.
- `matplotlib` and `numpy` inside `teach-workspace/.venv` (needed later, installed now).

**Exit Criteria**
- [ ] `python -m unittest discover -s teach-workspace/tools -p "test_*.py" -v` reports `OK` with at
      least 15 tests run.
- [ ] `python teach-workspace/tools/verify_workspace.py teach-workspace` prints
      `OK: 1 lessons, 1 records, 0 problems` and exits `0`.
- [ ] `teach-workspace/LESSON-MAP.md` contains one row for every lesson slug named in PHASE-02
      through PHASE-05 (27 rows) plus a row for lesson `0001` — 28 rows total.
- [ ] Lesson `0001` opens in a browser, the quiz scores interactively, and the page renders correctly
      with JavaScript disabled (content readable; only the interactive scoring is lost).
- [ ] `git log --oneline -1` shows the phase-0 commit and `git status --porcelain teach-workspace`
      prints nothing.
- [ ] `research/2026-08-11_mit-ocw-two-month-completion-brainstorm.md` no longer exists.

**Phase Risks**
- **RISK-01-01:** Over-building the scaffold consumes the week and delays week 1. Mitigation: the
  scaffold is time-boxed to 5 hours total; `style.css` and `quiz.js` are deliberately minimal and are
  expected to grow one component at a time as lessons demand it.
- **RISK-01-02:** The primer under- or over-shoots the actual Python baseline. Mitigation: the
  diagnostic runs first and its result is written into learning record 0001, which governs how much
  Python re-teaching is embedded in the early 6.0002 lessons.

### PHASE-02 - Weeks 1–2: Launch the Dual Track
**Goal**
Establish the cadence and get both tracks moving: 6.01SC through the software-engineering and
signals-and-systems material with its first two homeworks and software labs, and 6.0002 opened with
its first problem set completed and passing.

**Tasks**
- [ ] TASK-02-01 (Week 1, EE, ~7.5 h): Study 6.01SC Unit 1 — Object-Oriented Programming and State
      Machines — from `MIT6_01SCS11_chap01.pdf` and `chap02.pdf`, streaming the matching lectures from
      the playlist in that course's `videos.txt`. Author lessons `oop-for-engineering-models` and
      `state-machines-the-sm-abstraction`.
- [ ] TASK-02-02 (Week 1, EE): Extract `swLab01.zip` and `hw1.zip` into
      `teach-workspace/work/6.01SC/` and complete `MIT6_01SCS11_hw1.pdf` plus the software-lab
      exercises, writing answers in `teach-workspace/work/6.01SC/hw1/solution.md` and working code
      beside it. Where a skeleton imports `lib601`/`soar`, implement the required behaviour as a
      standalone function and note the substitution (ASM-006).
- [ ] TASK-02-03 (Week 1, SE, ~5 h): Study 6.0002 deck `MIT6_0002F16_lec1.pdf` (optimization and the
      knapsack problem) and author lesson `greedy-vs-optimal-knapsack`. Run and read
      `Lecture1.zip → lecture1.py` and answer `Lecture 1 Questions.txt` in
      `teach-workspace/work/6.0002/lecture1-answers.md`.
- [ ] TASK-02-04 (Week 1): Sunday review session per §6; write learning record
      `0002-<slug>`; update `PROGRESS.md`; commit `teach: week 01 — 6.01SC ch1–2, 6.0002 lec1`.
- [ ] TASK-02-05 (Week 2, EE, ~7.5 h): Study 6.01SC `chap03.pdf` and `chap04.pdf` (signals and
      systems; difference equations and the system-composition algebra). Author lessons
      `signals-and-systems-difference-equations` and `lti-poles-and-convergence`. Complete
      `MIT6_01SCS11_hw2.pdf` with `hw2.zip` and `swLab02.zip` into
      `teach-workspace/work/6.01SC/hw2/`.
- [ ] TASK-02-06 (Week 2, SE, ~5 h): Study `MIT6_0002F16_lec2.pdf` (graph-theoretic models and
      search); author lesson `graph-models-and-shortest-paths`. Extract `PS1.zip` into
      `teach-workspace/work/6.0002/ps1/`, delete any extracted `.pyc`, and complete `ps1a.py` and
      `ps1b.py` per `MIT6_0002F16_ProblemSet1.pdf` (cow-transport greedy vs. brute-force partitions).
- [ ] TASK-02-07 (Week 2): Review session; learning record `0003-<slug>`; `PROGRESS.md` update;
      commit `teach: week 02 — 6.01SC ch3–4, 6.0002 lec2 + PS1`.

**File Changes**
- `teach-workspace/lessons/NNNN-oop-for-engineering-models.html` (create)
- `teach-workspace/lessons/NNNN-state-machines-the-sm-abstraction.html` (create)
- `teach-workspace/lessons/NNNN-greedy-vs-optimal-knapsack.html` (create)
- `teach-workspace/lessons/NNNN-signals-and-systems-difference-equations.html` (create)
- `teach-workspace/lessons/NNNN-lti-poles-and-convergence.html` (create)
- `teach-workspace/lessons/NNNN-graph-models-and-shortest-paths.html` (create)
- `teach-workspace/reference/state-machine-patterns.html` (create): the SM class contract, the
  composition operators (cascade, parallel, feedback), and a worked two-state example — the card that
  gets reread all window.
- `teach-workspace/reference/difference-equations-and-poles.html` (create): the operator notation, the
  characteristic-equation-to-pole recipe, and the convergence rule stated as an inequality.
- `teach-workspace/work/6.01SC/hw1/solution.md` and `hw2/solution.md` (create), plus the extracted
  and completed skeleton `.py` files beside them.
- `teach-workspace/work/6.0002/lecture1-answers.md` (create).
- `teach-workspace/work/6.0002/ps1/` (create): extracted PS1 contents with `ps1a.py`/`ps1b.py`
  completed.
- `teach-workspace/learning-records/0002-*.md`, `0003-*.md` (create).
- `teach-workspace/PROGRESS.md` (modify): tick week 1 and week 2 checklist boxes, fill the hours row.
- `teach-workspace/GLOSSARY.md` (modify): add terms only once used correctly — expect *state machine*,
  *transducer*, *pole*, *unit-sample response*, *greedy algorithm*, *knapsack*.

**Function Signatures**
Study code written into `teach-workspace/work/`, not library code. The two interfaces that later
weeks depend on and must therefore be stable:
- `class SM: def start_state(self) -> object; def get_next_values(self, state, inp) -> tuple[object, object]; def transduce(self, inputs: list) -> list` — the 6.01 state-machine contract,
  reimplemented in `teach-workspace/work/6.01SC/lib/sm.py` without `lib601`; `transduce` returns the
  output sequence produced by feeding `inputs` through the machine from its start state.
- `greedy(items: list, max_cost: float, key_function) -> tuple[list, float]` — 6.0002 PS1 greedy
  selection; returns the chosen items and the total value achieved.

**Test Specs**
- `SM` cascade of a delay machine (`Delay(0)`) with an accumulator, transducing `[1, 2, 3]` →
  `[0, 1, 3]` (delay emits the initial value first, then the running sum lags by one step).
- `Delay(100).transduce([1, 2, 3])` → `[100, 1, 2]`
- `Accumulator(0).transduce([1, 2, 3])` → `[1, 3, 6]`
- `Accumulator(0).transduce([])` → `[]` (empty input yields empty output, no exception)
- Difference-equation check: for `y[n] = 0.5·y[n-1] + x[n]` with `y[-1] = 0` and
  `x = [1, 0, 0, 0]` → `y = [1, 0.5, 0.25, 0.125]`; the pole is `0.5`, `|0.5| < 1`, so the system
  converges — the lesson quiz must ask for exactly this conclusion.
- PS1: `python ps1a.py` with the shipped `ps1_cow_data.txt` runs without error and prints a greedy
  and a brute-force trip breakdown; the brute-force result uses no more trips than the greedy result.
- PS1 edge case: a cow whose weight exceeds the 10-unit limit must be reported as unshippable rather
  than silently dropped.

**Dependencies**
- PHASE-01 complete (workspace verified, primer taken).
- `teach-workspace/.venv` present for any plotting.

**Exit Criteria**
- [ ] Six new lessons exist and `python teach-workspace/tools/verify_workspace.py teach-workspace`
      exits `0`.
- [ ] `MIT6_01SCS11_hw1.pdf` and `hw2.pdf` are worked in full with written solutions committed.
- [ ] `python ps1a.py` and `python ps1b.py` run to completion from
      `teach-workspace/work/6.0002/ps1/` using the workspace virtualenv.
- [ ] Two learning records (`0002`, `0003`) exist and each names a specific demonstrated
      understanding, not a coverage log.
- [ ] `PROGRESS.md` shows logged hours for weeks 1 and 2 with `Total h` ≥ 12 for each; if under 12,
      a deferral entry explains it.
- [ ] Two commits pushed with the `teach: week 01` / `teach: week 02` messages.

**Phase Risks**
- **RISK-02-01:** The `lib601`-dependent skeletons stall week 1. Mitigation: ASM-006 — write
  `work/6.01SC/lib/sm.py` in week 1 as the first task, before touching any skeleton, so every later
  6.01SC exercise has a working `SM` base class.
- **RISK-02-02:** Two tracks in one week feels like context thrash. Mitigation: EE occupies the
  weekday mornings, SE occupies the weekend block for weeks 1–2; do not interleave inside a session.

### PHASE-03 - Weeks 3–4: Open 6.002, Sit Capstone 1, Run the Checkpoint
**Goal**
Finish 6.01SC end-to-end including the timed final and the design-lab capstone, bring 6.002 online
with its first four homeworks, advance 6.0002 through PS2 and PS3, and execute the week-4 velocity
checkpoint that re-baselines the rest of the window.

**Tasks**
- [ ] TASK-03-01 (Week 3, EE ~4 h): Study 6.01SC `chap05.pdf` and `chap06.pdf` (system performance
      and control-system design). Author lessons `characterizing-system-performance` and
      `designing-proportional-controllers`. Complete `MIT6_01SCS11_hw3.pdf` with `hw3.zip` (contains
      the `CMax` search tooling) and `swLab03.zip`.
- [ ] TASK-03-02 (Week 3, EE ~3.5 h): Open 6.002. Resolve the lecture URLs per ASM-007 and record them
      in `RESOURCES.md`. Study lectures 1–4 (lumped abstraction, KVL/KCL, node method, superposition)
      and author lessons `lumped-abstraction-and-kvl-kcl` and `node-method-and-superposition`.
      Complete `hw1.pdf` and `hw2.pdf` under the dual-method protocol (§4).
- [ ] TASK-03-03 (Week 3, SE ~5 h): Study `MIT6_0002F16_lec3.pdf` and author
      `graph-optimization-problems`. Extract `PS2.zip`, complete `ps2.py` (the MIT campus shortest-path
      problem with constraints) against `graph.py` and `mit_map.txt`.
- [ ] TASK-03-04 (Week 3): Review session; learning record; commit
      `teach: week 03 — 6.01SC ch5–6, 6.002 hw1–2, 6.0002 PS2`.
- [ ] TASK-03-05 (Week 4, EE ~3 h): Study 6.01SC `chap07.pdf` and `chap08.pdf` (discrete probability
      and state estimation; search and its optimization) plus `MIT6_01SCS11_cmax.pdf`. Author lessons
      `discrete-probability-and-bayesian-state-estimation` and `search-uniform-cost-and-heuristics`.
      Complete `MIT6_01SCS11_hw4.pdf` with `hw4.zip`.
- [ ] TASK-03-06 (Week 4, EE ~2 h — **CAPSTONE 1a**): Sit `MIT6_01SCS11_final_S11.pdf` in one
      uninterrupted timed block (duration from the paper's cover page; default 180 minutes per
      ASM-012), closed-book except a single hand-written formula sheet. Grade against
      `MIT6_01SCS11_final_S11_sol.pdf` using §2. Write
      `teach-workspace/assessments/2026-09-13-601sc-final-S11.md` with per-question points, the score,
      the pass/partial/fail verdict, and the two weakest topics.
- [ ] TASK-03-07 (Week 4, EE ~2.5 h — **CAPSTONE 1b**): Build the design-lab capstone in
      `teach-workspace/work/6.01SC/capstone/` per ASM-006: a pure-standard-library kinematic simulator
      stub plus a state-machine composition implementing proportional (and PD) wall-following, driven
      from the `designLab02`/`designLab03` skeleton logic. Produce a short
      `capstone/README.md` showing the controller gain, the observed steady-state error, and the gain
      value at which the simulated behaviour becomes oscillatory.
- [ ] TASK-03-08 (Week 4, EE ~1 h): 6.002 lectures 5–8 (Thévenin/Norton, digital abstraction);
      author lessons `thevenin-norton-equivalents` and `digital-abstraction-and-static-discipline`;
      complete `hw3.pdf` and `hw4.pdf` under §4.
- [ ] TASK-03-09 (Week 4, SE ~5 h): Study `MIT6_0002F16_lec4.pdf` and `lec5.pdf` (stochastic thinking;
      random walks) with `software/lect5.py`. Author lesson
      `stochastic-thinking-and-random-walks`. Extract `PS3.zip`, delete the bundled `.pyc` files,
      complete `ps3.py` and make `python ps3_tests_f16.py` pass.
- [ ] TASK-03-10 (Week 4, Sunday 2026-09-13 — **CHECKPOINT**): Compute `V` per §3 from the
      `PROGRESS.md` week-1..4 checklist, apply exactly one branch, and write the decision into
      `PROGRESS.md` under `## Deferrals` (or a one-line "V = x.xx, scope unchanged" note when branch 1
      applies). Write the week-4 learning record. Commit
      `teach: week 04 — 6.01SC complete + final S11, 6.002 hw3–4, PS3, checkpoint V=<value>`.

**File Changes**
- `teach-workspace/lessons/NNNN-characterizing-system-performance.html` (create)
- `teach-workspace/lessons/NNNN-designing-proportional-controllers.html` (create)
- `teach-workspace/lessons/NNNN-discrete-probability-and-bayesian-state-estimation.html` (create)
- `teach-workspace/lessons/NNNN-search-uniform-cost-and-heuristics.html` (create)
- `teach-workspace/lessons/NNNN-lumped-abstraction-and-kvl-kcl.html` (create)
- `teach-workspace/lessons/NNNN-node-method-and-superposition.html` (create)
- `teach-workspace/lessons/NNNN-thevenin-norton-equivalents.html` (create)
- `teach-workspace/lessons/NNNN-digital-abstraction-and-static-discipline.html` (create)
- `teach-workspace/lessons/NNNN-graph-optimization-problems.html` (create)
- `teach-workspace/lessons/NNNN-stochastic-thinking-and-random-walks.html` (create)
- `teach-workspace/reference/node-method-recipe.html` (create): the six-step node-method procedure,
  the sign convention for a current entering vs. leaving a node, and one fully worked three-node
  example with numbers — the single most-reused card for 6.002.
- `teach-workspace/reference/bayes-state-estimation-card.html` (create).
- `teach-workspace/assessments/2026-09-13-601sc-final-S11.md` (create): per TASK-03-06.
- `teach-workspace/work/6.01SC/capstone/` (create): `simulator.py`, `controller.py`, `run.py`,
  `README.md`.
- `teach-workspace/work/6.01SC/hw3/`, `hw4/` (create).
- `teach-workspace/work/6.002/hw1/` … `hw4/` (create): each with `solution.md` containing the primary
  derivation, the second-method check, and the confidence rating per §4.
- `teach-workspace/work/6.0002/ps2/`, `ps3/` (create).
- `teach-workspace/RESOURCES.md` (modify): add the resolved 6.002 per-lecture YouTube URLs under
  `## Knowledge`. Leave the `## Gaps` note about missing 6.002 solutions in place.
- `teach-workspace/PROGRESS.md` (modify): weeks 3–4 hours and checklist, plus the checkpoint decision.
- `teach-workspace/GLOSSARY.md` (modify): expect *lumped element*, *node method*, *superposition*,
  *Thévenin equivalent*, *noise margin*, *static discipline*, *belief state*, *admissible heuristic*.

**Function Signatures**
In `teach-workspace/work/6.01SC/capstone/`:
- `simulate(controller: Callable[[float], float], initial_distance: float, steps: int, dt: float = 0.1) -> list[float]` —
  runs the kinematic stub for `steps` timesteps and returns the sequence of wall distances in metres.
- `proportional(k_p: float, target: float) -> Callable[[float], float]` — returns a controller
  function mapping measured distance (metres) to commanded angular velocity (radians per second).
- `pd(k_p: float, k_d: float, target: float, dt: float) -> Callable[[float], float]` — as above with
  a derivative term computed from the change in error per timestep.

**Test Specs**
- `simulate(proportional(k_p=1.0, target=0.5), initial_distance=1.0, steps=200, dt=0.1)` → the final
  value is within `0.02` m of `0.5`, and the sequence is monotonically decreasing for the first 10
  steps (no overshoot at low gain).
- `simulate(proportional(k_p=12.0, target=0.5), initial_distance=1.0, steps=200, dt=0.1)` → the
  sequence changes sign of its error at least four times (sustained oscillation), demonstrating the
  gain–stability trade-off that the lesson quiz asks about.
- `simulate(proportional(k_p=0.0, target=0.5), initial_distance=1.0, steps=50, dt=0.1)` → every value
  equals `1.0` (zero gain means no correction — the degenerate case).
- `python ps3_tests_f16.py` from `teach-workspace/work/6.0002/ps3/` → exits `0` with all tests
  reported passing.
- 6.002 hw1 verification example: for a two-resistor divider with `V_in = 10 V`, `R1 = 1 kΩ`,
  `R2 = 3 kΩ`, the node method gives `V_out = 7.5 V`; the Thévenin second method must give the same
  `7.5 V`, and the limiting check `R2 → ∞` must give `V_out → 10 V`. A mismatch means the answer is
  rated `low` and goes to the open-questions list.

**Dependencies**
- PHASE-02 complete. `work/6.01SC/lib/sm.py` must already exist (built in week 1) because the capstone
  composes state machines.
- Streaming access to YouTube for 6.002 lectures.

**Exit Criteria**
- [ ] All eight 6.01SC chapters are covered by lessons; `MIT6_01SCS11_hw1.pdf` … `hw4.pdf` are worked.
- [ ] `teach-workspace/assessments/2026-09-13-601sc-final-S11.md` exists with a numeric score computed
      per §2 and a stated verdict.
- [ ] `python teach-workspace/work/6.01SC/capstone/run.py` executes and prints the steady-state error
      and the oscillation-onset gain.
- [ ] `python ps3_tests_f16.py` passes from the PS3 work directory.
- [ ] 6.002 hw1–hw4 each have a `solution.md` with a second-method check and a confidence rating on
      every question.
- [ ] `PROGRESS.md` contains the computed `V` value and the applied branch from §3.
- [ ] Two commits pushed (weeks 3 and 4).

**Phase Risks**
- **RISK-03-01:** Week 4 is the heaviest week in the window (two capstone items plus a checkpoint plus
  a problem set). Mitigation: the 6.01SC final is scheduled into the weekend block on Sat 2026-09-12
  and the capstone into Sun 2026-09-13; if either slips, the final takes priority and the capstone
  moves into week 6 (the buffer) via a deferral entry.
- **RISK-03-02:** 6.002 opens without any solutions, so errors can go unnoticed and compound.
  Mitigation: §4 is mandatory from hw1 — no 6.002 answer is recorded without a second-method check.
- **RISK-03-03:** A failing 6.01SC final (score < 55.0) triggers a re-sit that has no room in the
  schedule. Mitigation: re-sit `MIT6_01SCS11_final_F10.pdf` in week 6 (the buffer) rather than
  immediately, and log the deferral.

### PHASE-04 - Weeks 5–6: Quiz 1 and the Buffer Week
**Goal**
Push 6.002 through its amplifier and first-order-dynamics material with a timed quiz-1 gate, advance
6.0002 to PS4, and use week 6 deliberately as the catch-up lane that keeps the window recoverable.

**Tasks**
- [ ] TASK-04-01 (Week 5, EE ~5 h): 6.002 lectures on MOSFET switch-resistor models, digital gate
      design, and small-signal amplifiers. Author lessons `mosfet-switch-resistor-model` and
      `small-signal-amplifier-analysis`. Complete `hw5.pdf` and `hw6.pdf` under §4.
- [ ] TASK-04-02 (Week 5, EE ~2 h — **GATE**): Sit `quiz1_s07.pdf` timed (duration from the paper;
      default 90 minutes per ASM-012), closed-book with one formula sheet. Self-grade under §4 (no
      solution file exists) and write `teach-workspace/assessments/2026-09-20-6002-quiz1-s07.md`.
      Keep `quiz1_f06.pdf`, `quiz1_s04.pdf`, `quiz1_f03.pdf` in reserve for a re-sit.
- [ ] TASK-04-03 (Week 5, SE ~5 h): Study `MIT6_0002F16_lec6.pdf` (Monte Carlo simulation); author
      lesson `monte-carlo-simulation`. Extract `PS4.zip`, complete `ps4.py`, make `python ps4_tests.py`
      pass.
- [ ] TASK-04-04 (Week 5): Review session; learning record; commit
      `teach: week 05 — 6.002 hw5–6 + quiz1, 6.0002 PS4`.
- [ ] TASK-04-05 (Week 6, ~12 h — **BUFFER**): Execute, in this priority order, only what is
      outstanding: (1) any item carrying a deferral entry from weeks 1–5; (2) any exam scoring below
      70.0 gets its remediation lesson and re-sit; (3) 6.002 lectures on energy-storage elements and
      first-order transients with lessons `capacitors-inductors-and-first-order-transients` and
      `second-order-rlc-dynamics`, plus `hw7.pdf` and `hw8.pdf`; (4) 6.0002 PS5 pulled forward.
      Whatever is not reached is logged as a deferral, not dropped.
- [ ] TASK-04-06 (Week 6): Review session; learning record explicitly naming what the buffer absorbed;
      commit `teach: week 06 — buffer: <what closed>`.

**File Changes**
- `teach-workspace/lessons/NNNN-mosfet-switch-resistor-model.html` (create)
- `teach-workspace/lessons/NNNN-small-signal-amplifier-analysis.html` (create)
- `teach-workspace/lessons/NNNN-capacitors-inductors-and-first-order-transients.html` (create)
- `teach-workspace/lessons/NNNN-second-order-rlc-dynamics.html` (create)
- `teach-workspace/lessons/NNNN-monte-carlo-simulation.html` (create)
- `teach-workspace/reference/small-signal-model-card.html` (create): the operating-point-then-perturb
  procedure, the MOSFET small-signal parameters, and the sign conventions.
- `teach-workspace/reference/first-and-second-order-response-card.html` (create): the `τ = RC` and
  `τ = L/R` forms, the second-order `ω₀`/`ζ` definitions, and the under/critical/over-damped
  boundaries stated as inequalities on `ζ`.
- `teach-workspace/assessments/2026-09-20-6002-quiz1-s07.md` (create)
- `teach-workspace/work/6.002/hw5/` … `hw8/` (create)
- `teach-workspace/work/6.0002/ps4/` (create); `ps5/` (create) if pulled forward
- `teach-workspace/PROGRESS.md` (modify): weeks 5–6 rows, checklist, and any new deferrals
- `teach-workspace/GLOSSARY.md` (modify): expect *small-signal model*, *operating point*,
  *transconductance*, *time constant*, *damping ratio*, *Monte Carlo estimate*, *confidence interval*

**Function Signatures**
- `teach-workspace/work/6.0002/ps4/ps4.py` — completes the interfaces defined by the shipped
  `ps4_tests.py`; do not change those signatures.
- No new workspace tooling interfaces change in this phase.

**Test Specs**
- `python ps4_tests.py` from `teach-workspace/work/6.0002/ps4/` → exits `0`, all tests pass.
- Monte Carlo check written into the lesson: estimating π by sampling 10⁶ uniform points in the unit
  square yields `3.14 ± 0.01`; the same estimate with 10² points must be shown to vary by more than
  `0.1` across five runs — the quiz asks the learner to state why, in terms of standard error.
- First-order verification example: for `R = 10 kΩ`, `C = 1 µF`, a step from 0 V to 5 V gives
  `τ = 10 ms` and `v(τ) = 5 × (1 − e⁻¹) = 3.16 V`; the second-method check is the energy/limiting
  argument that `v(∞) = 5 V` and `v(0⁺) = 0 V`.
- Second-order edge case: `R = 0 Ω` in a series RLC gives `ζ = 0`, i.e. undamped sustained
  oscillation at `ω₀ = 1/√(LC)` — the lesson must state this degenerate case explicitly.
- Quiz-1 gate: score computed per §2; a score below 70.0 must produce a remediation lesson file and a
  scheduled re-sit date in `PROGRESS.md`.

**Dependencies**
- PHASE-03 complete, including the week-4 checkpoint decision (which may have reduced scope here).

**Exit Criteria**
- [ ] `teach-workspace/assessments/2026-09-20-6002-quiz1-s07.md` exists with a numeric score and a
      verdict, and every question carries a confidence rating per §4.
- [ ] `python ps4_tests.py` passes.
- [ ] 6.002 hw5–hw8 are complete, or the missing ones have deferral entries with re-entry triggers.
- [ ] `PROGRESS.md` `## Deferrals` has no entry whose re-entry trigger has already passed without
      action.
- [ ] `python teach-workspace/tools/verify_workspace.py teach-workspace` exits `0`.
- [ ] Two commits pushed (weeks 5 and 6).

**Phase Risks**
- **RISK-04-01:** The buffer week gets spent on new material instead of catch-up, leaving weeks 7–8
  overloaded. Mitigation: TASK-04-05's priority order is binding — new 6.002 material is item (3),
  reached only when items (1) and (2) are empty.
- **RISK-04-02:** Self-graded quiz 1 produces false confidence because no solutions exist.
  Mitigation: §4 point 4 — questions rated `low` score zero regardless of how right they feel, and go
  to the next review session as open questions.

### PHASE-05 - Weeks 7–8: Quiz 2, Capstone 2, Phase Gate
**Goal**
Close the 6.002 arc with the frequency-domain and op-amp material, a timed quiz 2, and the timed
final; close the 6.0002 arc with PS5 and a timed synthesis assessment; then run the phase-gate review.

**Tasks**
- [ ] TASK-05-01 (Week 7, EE ~5 h): 6.002 sinusoidal steady state, impedance, and frequency response.
      Author lessons `sinusoidal-steady-state-and-impedance` and `frequency-response-and-filters`.
      Complete `hw9.pdf` and `hw10.pdf` under §4.
- [ ] TASK-05-02 (Week 7, EE ~2 h — **GATE**): Sit `quiz2_s07.pdf` timed (default 90 minutes),
      self-grade under §4, write `teach-workspace/assessments/2026-10-04-6002-quiz2-s07.md`. Reserve
      `quiz2_f04.pdf` and `quiz2_s04.pdf` for a re-sit.
- [ ] TASK-05-03 (Week 7, SE ~5 h): Study `MIT6_0002F16_lec7.pdf` and `lec8.pdf` (confidence
      intervals; sampling and standard error). Author lessons `confidence-intervals-and-error-bars`
      and `sampling-and-standard-error`. Extract `PS5.zip` if not already done, complete `ps5.py`,
      make `python ps5_test.py` pass.
- [ ] TASK-05-04 (Week 7): Review session; learning record; commit
      `teach: week 07 — 6.002 hw9–10 + quiz2, 6.0002 lec7–8 + PS5`.
- [ ] TASK-05-05 (Week 8, EE ~3 h): 6.002 op-amps, negative feedback, and power in digital gates.
      Author lessons `op-amps-and-negative-feedback` and `power-in-digital-circuits`. Read
      `lab_handout.pdf`, `lab0.pdf`–`lab4.pdf` and the relevant `demo_*.pdf` files as a paper
      substitute for the physical lab (no hardware is available); record in the learning record which
      measurements would have been taken and what each would have shown.
- [ ] TASK-05-06 (Week 8, EE ~3 h — **CAPSTONE 2**): Sit `final_s07.pdf` in one uninterrupted timed
      block (duration from the paper; default 180 minutes), one formula sheet allowed. Self-grade
      under §4 and write `teach-workspace/assessments/2026-10-10-6002-final-s07.md`. Keep
      `final_f00.pdf` in reserve.
- [ ] TASK-05-07 (Week 8, SE ~4 h): Write and sit a 90-minute synthesis assessment covering 6.0002
      decks 1–8 — 12 questions: 4 on optimization/graphs, 4 on stochastic simulation, 4 on sampling
      and confidence intervals, each requiring a numeric answer or a short program. Store the paper
      and the graded attempt in `teach-workspace/assessments/2026-10-11-6002-synthesis.md`.
- [ ] TASK-05-08 (Week 8, Sun 2026-10-11): Phase-gate review session (extend to 90 minutes): re-read
      every learning record, take a full-window interleaved synthesis quiz, and update `GLOSSARY.md`
      with every term now genuinely owned. Commit
      `teach: week 08 — 6.002 final, 6.0002 synthesis, phase gate`.

**File Changes**
- `teach-workspace/lessons/NNNN-sinusoidal-steady-state-and-impedance.html` (create)
- `teach-workspace/lessons/NNNN-frequency-response-and-filters.html` (create)
- `teach-workspace/lessons/NNNN-op-amps-and-negative-feedback.html` (create)
- `teach-workspace/lessons/NNNN-power-in-digital-circuits.html` (create)
- `teach-workspace/lessons/NNNN-confidence-intervals-and-error-bars.html` (create)
- `teach-workspace/lessons/NNNN-sampling-and-standard-error.html` (create)
- `teach-workspace/reference/impedance-and-bode-card.html` (create): the `Z` forms for R, L, C, the
  series/parallel combination rules, and the two Bode asymptote rules with corner-frequency placement.
- `teach-workspace/reference/op-amp-golden-rules-card.html` (create)
- `teach-workspace/assessments/2026-10-04-6002-quiz2-s07.md` (create)
- `teach-workspace/assessments/2026-10-10-6002-final-s07.md` (create)
- `teach-workspace/assessments/2026-10-11-6002-synthesis.md` (create)
- `teach-workspace/work/6.002/hw9/`, `hw10/` (create)
- `teach-workspace/work/6.0002/ps5/` (create)
- `teach-workspace/PROGRESS.md` (modify): weeks 7–8 rows and final checklist state
- `teach-workspace/GLOSSARY.md` (modify): expect *impedance*, *corner frequency*, *Bode plot*,
  *virtual short*, *loop gain*, *standard error*, *confidence interval*

**Function Signatures**
- `teach-workspace/work/6.0002/ps5/ps5.py` — completes the interfaces required by the shipped
  `ps5_test.py`; do not change those signatures.
- No workspace tooling interfaces change in this phase.

**Test Specs**
- `python ps5_test.py` from `teach-workspace/work/6.0002/ps5/` → exits `0`, all tests pass.
- Impedance verification example: a series RC with `R = 1 kΩ`, `C = 159 nF` has a corner frequency
  `f_c = 1/(2πRC) ≈ 1.00 kHz`; at `f = f_c` the output magnitude of the low-pass response is
  `1/√2 ≈ 0.707` of input and the phase is `−45°`. Both must be produced by hand and confirmed by a
  Python evaluation of the complex transfer function.
- Frequency-response edge case: at `f → 0` the capacitor is an open circuit (`|H| → 1` for the
  low-pass form); at `f → ∞` it is a short (`|H| → 0`). The lesson quiz must require both limits.
- Op-amp edge case: with the feedback path removed, the golden rules do not apply and the output
  saturates at the supply rail — the lesson must state this explicitly so the rules are not
  over-applied.
- Quiz-2 and final gates: scores computed per §2, each with per-question confidence ratings per §4.

**Dependencies**
- PHASE-04 complete. If the week-4 checkpoint selected branch 3, the 6.002 final in TASK-05-06 has
  already moved to Phase 2 — in that case skip TASK-05-06 and record it as executed-by-deferral.

**Exit Criteria**
- [ ] Three assessment files exist for week 7–8 gates, each with a numeric score and a verdict.
- [ ] `python ps5_test.py` passes (unless PS5 was deferred by the checkpoint, in which case the
      deferral entry exists).
- [ ] All twelve 6.002 lessons named across PHASE-03…PHASE-05 exist, or the missing ones are logged
      as deferrals.
- [ ] `python teach-workspace/tools/verify_workspace.py teach-workspace` exits `0` and reports at
      least 28 lessons and at least 9 learning records.
- [ ] Two commits pushed (weeks 7 and 8).

**Phase Risks**
- **RISK-05-01:** Week 8 stacks a 3-hour final, a 90-minute synthesis assessment, and the phase-gate
  review into one week. Mitigation: the 6.002 final is fixed to Sat 2026-10-10 and nothing else is
  scheduled that day; the synthesis assessment moves to Phase 2 first if the week compresses.
- **RISK-05-02:** No physical lab means the 6.002 lab component is unassessable. Mitigation: the
  paper-lab reading in TASK-05-05 is explicitly recorded as a known gap in `PHASE-1-REVIEW.md` rather
  than being quietly counted as complete.

### PHASE-06 - Window Close and Phase 2 Hand-off
**Goal**
By Mon 2026-10-12, produce an honest written verdict on the eight weeks and a concrete, dated Phase-2
plan, so the next window starts with the same low activation energy this one did.

**Tasks**
- [ ] TASK-06-01: Write `teach-workspace/PHASE-1-REVIEW.md` with: total hours (from `PROGRESS.md`)
      against the 96–112 h target; every gate and its score; every deferral and where it moved; the
      three concepts that proved hardest, with evidence from the learning records; and the two study
      habits that actually worked versus the two that did not.
- [ ] TASK-06-02: Update `teach-workspace/MISSION.md` if the eight weeks changed the goal, and — when
      it changed — write a learning record capturing the shift and why.
- [ ] TASK-06-03: Write `teach-workspace/ROADMAP.md` covering Phases 2–5 with dated windows, carrying
      forward every deferral from `PROGRESS.md`:
      - **Phase 2 (2026-10-12 → 2027-01-10):** any 6.002 remainder, then 6.003 Signals & Systems
        (`mit-ocw-curriculum/electrical-engineering/03-signals-and-systems-6.003/`, which has a full
        problem-set and solution set), plus deferred 6.0002 problem sets.
      - **Phase 3 (2027-01-11 → 2027-03-14):** 6.007 Electromagnetic Energy and 6.012 Microelectronic
        Devices (both carry exam archives).
      - **Phase 4 (2027-03-15 → 2027-06-13):** the professional payoff — 6.061 Electric Power Systems
        → 6.685 Electric Machines → 6.622 Power Electronics (119 files including handwritten notes and
        a design project).
      - **Phase 5 (optional, after a milestone review):** the software track deepens —
        6.042J → 6.006 → 6.033 → 6.046J.
- [ ] TASK-06-04: Reset `PROGRESS.md` for the next window: archive the completed eight-week tables
      into `teach-workspace/archive/2026-08-17-to-2026-10-11-progress.md` and leave `PROGRESS.md`
      holding only the new window's empty tables.
- [ ] TASK-06-05: Run the full verification suite (see `## Verification Strategy`), then commit and
      push `teach: phase 1 complete — review, roadmap, phase 2 hand-off`.

**File Changes**
- `teach-workspace/PHASE-1-REVIEW.md` (create)
- `teach-workspace/ROADMAP.md` (create)
- `teach-workspace/archive/2026-08-17-to-2026-10-11-progress.md` (create)
- `teach-workspace/PROGRESS.md` (modify): archived and reset per TASK-06-04
- `teach-workspace/MISSION.md` (modify): only if the mission genuinely shifted
- `teach-workspace/learning-records/NNNN-*.md` (create): the mission-shift record, if applicable

**Function Signatures**
None — no code interfaces change in this phase.

**Test Specs**
None — no testable behavior changes in this phase. Verification is the full suite in
`## Verification Strategy`.

**Dependencies**
- PHASE-05 complete, including every assessment file.

**Exit Criteria**
- [ ] `teach-workspace/PHASE-1-REVIEW.md` states total logged hours and a score for every gate that
      was attempted, plus an explicit list of what was not attempted and why.
- [ ] `teach-workspace/ROADMAP.md` contains dated windows for Phases 2–5 and carries every open
      deferral forward by name.
- [ ] `python teach-workspace/tools/verify_workspace.py teach-workspace` exits `0`.
- [ ] `git status --porcelain` prints nothing and `git log --oneline -1` shows the phase-1-complete
      commit on `main`, pushed.

**Phase Risks**
- **RISK-06-01:** The review is written optimistically and hides the misses, which corrupts Phase 2
  planning. Mitigation: TASK-06-01 requires the not-attempted list and the score of every gate,
  including failures; a review with no misses listed after an intentionally aggressive window should
  be treated as evidence the review was not honest, not as evidence of a perfect window.

## Gotchas
- **There is no 6.01SC "F11" final.** The available finals are `S09`, `F09`, `S10`, `F10`, `S11`
  (each with a `_sol.pdf`). The capstone uses `final_S11`. Searching for `final_F11` will waste time.
- **6.01SC midterms exist only as solutions** — `mid01_{F09,F10,S10,S11}_sol.pdf` and
  `mid02_F10_sol.pdf`. There are no blank midterm papers, so no midterm can be sat under time. Use
  them as worked examples after attempting the corresponding homework.
- **6.002 ships zero solutions.** Its `syllabus.txt` lists resource types as Exams, Lecture Videos,
  and Problem Sets only — there is nothing to grade against. Every 6.002 answer needs the dual-method
  protocol in §4. This is the single largest quality risk in the window.
- **6.002 has no lecture notes either.** All 6.002 conceptual content comes from the streamed
  lectures plus the Agarwal & Lang textbook; the local PDFs are homework, labs, demos, and exams only.
- **`videos.txt` for 6.002 names only Lecture 1 and Lecture 25.** The rest sit behind the MIT OCW
  channel link. Resolve the list once in week 3 and record it in `RESOURCES.md` — do **not** edit
  `videos.txt`, which lives in the read-only curriculum tree.
- **6.01SC lab and homework zips import `lib601`/`soar`**, which is not in this repository, and the
  design labs assume a physical robot. Write `work/6.01SC/lib/sm.py` in week 1 and treat the
  skeletons as specifications, not runnable code.
- **6.0002 problem-set zips contain Python 3.5 bytecode** (`ps3.cpython-35.pyc`,
  `ps3_verify_movement27.cpython-35.pyc`, `test.pyc`). Delete every `.pyc` immediately after
  extraction, or Python may import stale bytecode instead of the edited source.
- **Never extract into `mit-ocw-curriculum/`.** Every zip is extracted into
  `teach-workspace/work/<course>/`. The curriculum tree stays byte-identical for the whole window;
  `git status mit-ocw-curriculum` must always print nothing.
- **6.002 homework numbering is not week numbering.** `hw1.pdf`–`hw10.pdf` map to this plan's weeks
  3–7 at two per week, not one per week.
- **Lesson and learning-record numbers are independent sequences**, both zero-padded to four digits.
  `lessons/0007-*.html` and `learning-records/0007-*.md` are unrelated documents.
- **Quiz answer options must be word-count-matched.** A longer, more detailed option is a formatting
  tell that lets the learner pattern-match instead of retrieving. This is checked by eye at authoring
  time, not by the script.
- **The weekly synthesis quiz draws on previous weeks, not the current one.** Testing this week's
  material tests fluency; testing older material builds storage strength. Getting this backwards
  quietly defeats the point of the cadence.
- **Hours are logged excluding the review session**, so a week showing exactly 12 h of study plus a
  45-minute review is on budget, not over.
- **Windows path note:** the virtualenv interpreter is `teach-workspace/.venv/Scripts/python` on
  Windows and `teach-workspace/.venv/bin/python` elsewhere. Use the interpreter path directly rather
  than relying on shell activation inside scripts.
- **`idle-n.bat` / `idle-n.zip` / `idleNForWindows.zip`** in the 6.01SC folder are IDLE launchers for
  the 2011 lab environment. They are not needed and should not be run.

## Verification Strategy
- **TEST-001:** `python teach-workspace/tools/verify_workspace.py teach-workspace` → exits `0` and
  prints a single line matching `OK: {n} lessons, {m} records, 0 problems`. Run after every weekly
  review session, before committing.
- **TEST-002:** `python -m unittest discover -s teach-workspace/tools -p "test_*.py" -v` → ends with
  `OK` and reports at least 15 tests run.
- **TEST-003:** from the directory `teach-workspace/work/6.0002/ps3`, run `python ps3_tests_f16.py`
  → exits `0` with all tests reported passing. Equivalent checks: `python ps4_tests.py` run from
  `teach-workspace/work/6.0002/ps4`, and `python ps5_test.py` run from
  `teach-workspace/work/6.0002/ps5`. (Each script resolves its data files relative to the current
  directory, so it must be run from inside its own problem-set directory.)
- **TEST-004:** `python teach-workspace/work/6.01SC/capstone/run.py` → prints a steady-state error
  below `0.02` m for `k_p = 1.0` and an oscillation-onset gain, exits `0`.
- **TEST-005:** `git status --porcelain mit-ocw-curriculum` → prints nothing at every commit point,
  proving the curriculum tree was never modified.
- **TEST-006:** `python -c "import pathlib,sys; p=pathlib.Path('teach-workspace/lessons'); bad=[f.name for f in p.glob('*.html') if 'assets/style.css' not in f.read_text(encoding='utf-8')]; print(bad); sys.exit(1 if bad else 0)"`
  → prints `[]` and exits `0`, proving every lesson links the shared stylesheet instead of inlining
  styles.
- **TEST-007:** `python -c "import pathlib; print(sum(1 for _ in pathlib.Path('teach-workspace/assessments').glob('*.md')))"`
  → prints `5` at the end of PHASE-05 (6.01SC final, 6.002 quiz 1, 6.002 quiz 2, 6.002 final, 6.0002
  synthesis), or a smaller number matched one-for-one by deferral entries in `PROGRESS.md`.
- **MANUAL-001:** Open each new lesson in a browser after authoring: the quiz scores interactively,
  the primary-source link resolves, the mission link resolves, and the page prints to one or two
  pages without clipped content.
- **MANUAL-002:** At each weekly review session, confirm `PROGRESS.md` has an hours row for the week
  with `Total h` between 12 and 14; if outside that band, a one-line reason is written in the same row.
- **MANUAL-003:** At the week-4 checkpoint, confirm the computed `V` and the applied branch from §3
  are written verbatim into `PROGRESS.md` before any week-5 work begins.
- **OBS-001:** `git log --oneline --since=2026-08-17 -- teach-workspace | wc -l` → at least 8 (one
  commit per study week, plus the phase-0 and phase-1-complete commits). A week with no commit is the
  earliest reliable signal that the cadence has broken; treat it as a deferral trigger at the next
  review session.
- **OBS-002:** `python -c "import pathlib; print(sorted(f.name for f in pathlib.Path('teach-workspace/learning-records').glob('*.md')))"`
  → one record per study week plus the baseline record. Missing records mean weeks were run without
  reflection, which is the failure mode the whole cadence exists to prevent.

## Risks and Alternatives
- **RISK-001 (highest):** The compression assumption (ASM-002) fails and week 8 arrives with 6.002
  half-finished. Mitigation: the week-4 checkpoint (§3) forces an explicit, written scope decision at
  the halfway point rather than at the end, and the branch rules protect the EE gates first because
  the mission is EE-led. A partially-completed 6.002 with honest deferrals is a success state; an
  abandoned one is not.
- **RISK-002:** Self-grading 6.002 without solutions produces confident wrong answers that carry into
  6.003 (which depends on it). Mitigation: §4's confidence ratings, plus the rule that `low`-rated
  questions score zero and surface at the next review session; plus a Phase-2 entry requirement that
  every open question from the 6.002 assessment files is resolved before 6.003 starts.
- **RISK-003:** Life volatility — an infant, a full-time country-director role — collapses a week
  entirely. Mitigation: week 6 is a pre-declared buffer, the defer rule guarantees a written re-entry
  plan rather than a silent stall, and the minimum viable week is one 60-minute session plus a review
  session, which still produces a learning record and a commit.
- **RISK-004:** Workspace-building becomes procrastination — more time authoring lessons and polishing
  stylesheets than studying. Mitigation: PHASE-01 is time-boxed to 5 hours; from week 1 the hours
  logged in `PROGRESS.md` count *study*, and lesson authoring is capped at roughly 20 minutes per
  lesson by keeping each lesson to a single tangible win.
- **ALT-001:** EE-only serial Phase 1 (finish 6.01SC and 6.002 before touching software). Not chosen:
  the confirmed decision is both tracks from day one, since both serve live professional needs.
- **ALT-002:** Pure self-study straight from the curriculum README with no teaching workspace. Not
  chosen: it reproduces exactly the documented open-courseware failure mode — materials without
  structure, retrieval practice, or accountability.
- **ALT-003:** Start at the power courses (6.061 / 6.622), which are closest to the professional
  payoff. Not chosen: they presume circuits and signals foundations that this window builds.
- **ALT-004:** A surface-level two-month blitz across all 19 courses. Not chosen: it is arithmetically
  impossible at 12–14 h/week and would produce fluency without storage strength — the illusion of
  mastery this plan is explicitly designed to avoid.

## Suggested Next Step
Execute PHASE-01 between Wed 2026-08-12 and Sun 2026-08-16, finishing with its six exit criteria
verified — in particular `python -m unittest discover -s teach-workspace/tools -p "test_*.py" -v`
reporting `OK` and `python teach-workspace/tools/verify_workspace.py teach-workspace` printing
`OK: 1 lessons, 1 records, 0 problems`. Week 1 study begins Mon 2026-08-17.
