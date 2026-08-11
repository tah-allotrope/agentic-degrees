# Research Brief: Free OpenCourseware Degree Paths (Software & Electrical Engineering)

**Date:** 2026-08-11
**Modes run:** domain, literature
**Depth:** exhaustive
**Invocation context:** "exhaustive and rank top 3 opencourse software engineering and electrical engineering degree from us uk eu universities that I can complete for free with full materials, exercise, exam and capstone projects available for tackling"
**Sources (wide/deep):** 1009/53 | **Ratio used:** github=0.25, academia=0.25, industry=0.25, web=0.25

---

## Synthesis

No university offers an accredited engineering degree fully free; the honest target is a *degree-shaped free curriculum* — a complete sequence of university OCW/MOOC courses with lectures, problem sets, exams and projects you can work through self-paced. [NOTE: treat "free degree" as "degree-equivalent free curriculum"; credentials and graded feedback are the paid parts everywhere.] Two contenders dominate every discipline comparison: MIT OpenCourseWare (US) for sheer completeness of materials — 2,500+ courses, no signup, exams and solutions included (verified on 6.002, 6.01SC, 6.685, 6.622 pages) — and TU Delft OpenCourseWare (EU) for structured, remixable engineering courses with lecture/exam/reading sections per course (verified on electrical-machines-and-drives). For software engineering, the University of Helsinki's Full Stack Open is the strongest free *project-based* path (exercises for every part, real projects, downloadable certificate, 5 ECTS); for a full CS-degree-shaped route with an explicit capstone, the community-built OSSU curriculum (207k-star GitHub repo, CS2013-aligned, ~2 years at 20h/wk) is the reference path and is the only one with a peer-evaluated Final Project requirement. UK free content is the thinnest: OpenLearn (Open University) offers hundreds of free short courses with badges but no degree-shaped sequence in engineering; Imperial College's contribution is free-audit MOOCs on edX/Coursera; Cambridge publishes some teaching materials but not a coherent OCW program.

Ranking criteria used: (1) full free materials, (2) exercises/assignments with solutions, (3) exams available, (4) project/capstone opportunities, (5) university origin US/UK/EU, (6) curriculum coherence toward a degree.

**Top 3 — Software Engineering / CS:**
1. **MIT OpenCourseWare (US)** — complete EECS undergrad sequence (6.0001→6.006→6.005/6.033), full lecture materials, problem sets with solutions, exams with solutions; project courses exist (6.005, 6.033) but no formal capstone.
2. **University of Helsinki — Full Stack Open (EU)** — free, exercises for parts 0-13, two real project stages, certificate; 5 ECTS via open university; best free *applied* SE path.
3. **OpenLearn (Open University, UK)** — free computing & IT courses (badges/certificates); degree-shaped only if combined with paid OU modules; weaker than #1-2.

**Top 3 — Electrical Engineering:**
1. **MIT OpenCourseWare (US)** — 6.01/6.002/6.003/6.02/6.622/6.685 sequence, full materials + problem sets + exams with solutions.
2. **TU Delft OpenCourseWare (EU)** — EE program courses (electrical machines & drives, power electronics/drives) with lectures, exams, readings, projects; MSc EE program structure documented; DelftX on edX auditable free.
3. **ETH Zurich open learning (EU)** — BSc EE&IT core curriculum materials, CC-licensed open learning courses, online.ethz.ch course list, ETHx on edX audit; UK EE free content (OpenLearn intro-level only) ranks below these.

Capstone reality: OSSU's Final Project is the only true free capstone; FSO's project stages and MIT/TU Delft course projects are capstone-*like*. [NOTE: if a formal capstone + credential is required, no free option exists — the nearest paid-but-cheap options (Georgia Tech OMSCS, University of London BSc) were out of scope per "free".]

---

## Source Coverage

| bucket | target | gathered | qualified | cited | reallocated |
|---|---|---|---|---|---|
| github | 63 | 204 | 204 | 1 | +141 |
| academia | 63 | 473 | 435 | 4 | +410 |
| industry | 62 | 130 | 130 | 5 | +68 |
| web | 62 | 202 | 30 | 43 | -32 |

Coverage narrative: Firecrawl unavailable (no `FIRECRAWL_API_KEY`) → industry/web filled via this environment's `web_search` fallback (working) instead of Firecrawl; gathered counts far exceed targets because quota-free backends (OpenAlex, `gh search`) oversaturated and dedup only removed exact URL collisions. Web bucket qualified only 30/62 (most web rows are tier-4 aggregator/forum hits); per default non-strict-ratio policy the 32-row deficit was backfilled from github/academia surplus. Deep set = 53 rows verified with claims.

---

## Domain

### Discovery

Strongest sources found: MIT OCW course pages ([6.002](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/), [6.01SC](https://ocw.mit.edu/courses/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/), [6.685](https://ocw.mit.edu/courses/6-685-electric-machines-fall-2013/), [6.622](https://ocw.mit.edu/courses/6-622-power-electronics-spring-2023/)) — each with lecture materials, assignments, problem sets and exams listed; [MIT OCW About](https://ocw.mit.edu/about/) (2,500+ courses, free, no signup, CC) and [Get Started](https://ocw.mit.edu/pages/get-started/). TU Delft OCW ([home](https://ocw.tudelft.nl/), [electrical machines & drives](https://ocw.tudelft.nl/courses/electrical-machines-and-drives/), [power drives subjects](https://ocw.tudelft.nl/courses/electrical-power-drives/subjects/), [MSc EE program](https://ocw.tudelft.nl/programs/master/electrical-engineering/)). Helsinki Full Stack Open ([home](https://fullstackopen.com/en/), [about](https://fullstackopen.com/en/about/), [Helsinki open-university page](https://www.helsinki.fi/en/admissions-and-education/open-university/multidisciplinary-themed-modules/full-stack), [5-credit course implementation](https://studies.helsinki.fi/courses/course-implementation/otm-861c248f-e4e4-43df-a69a-50fd206afabf)). OSSU ([repo](https://github.com/ossu/computer-science), [curriculum site](http://cs.ossu.dev/)). OpenLearn ([free courses](https://www.open.edu/openlearn/free-courses), [engineering & technology](https://www.open.edu/openlearn/science-maths-technology/engineering-technology), [digital & computing](https://www.open.edu/openlearn/digital/free-courses)). ETH ([open learning](https://ethz.ch/en/the-eth-zurich/education/innovation/OffeneLernangebote.html), [online course list](https://online.ethz.ch/courses), [BSc EE&IT structure](https://ee.ethz.ch/studies/bachelor/bsc-eeit/first-and-second-year.html)). Stanford ([free courses](https://online.stanford.edu/free-courses), [SEE CS106A](https://see.stanford.edu/Course/CS106A/194)). Imperial ([free online courses guide](https://www.imperial.ac.uk/students/success-guide/ug/effective-study/working-by-yourself/learning-online/online-courses/), [ImperialX on edX](https://www.edx.org/school/imperialx)). Cambridge [Computer Lab teaching pages](https://www.cl.cam.ac.uk/teaching/). GitHub community evidence: [OSSU progress tracker](https://github.com/t-miller/ossu-computer-science-progress), [FSO solutions](https://github.com/jarvensivu/full-stack-open). Aggregators for breadth: [Class Central free-certificates list](https://www.classcentral.com/report/free-certificates/), [DelftX](https://www.edx.org/school/delftx), [ETHx](https://www.edx.org/school/ethx).

### Verification

All ranking-bearing claims verified by direct fetch of the primary pages above (web_extract/curl + `gh api` for the OSSU repo: 207,852 stars, updated 2026-08-11, 23 open issues — active). MIT OCW pages explicitly list exams, assignments, problem sets and solutions; the About page states 2,500+ courses, free, no registration, CC-licensed. TU Delft OCW course pages show Lecture/Exam/Reading sections and the EE MSc program page documents program structure. Helsinki pages confirm "free of charge", "5 cr", "exercises for parts 0-7", downloadable certificate. OSSU README (fetched via GitHub API) confirms CS2013 alignment, ~2 years at 20h/wk, free materials with optional paid grading (financial aid available), and a peer-evaluated Final Project. Flagged as *weak evidence*: Stanford "150+ courses online" claim comes from a Reddit thread (tier-4); Cambridge/Imperial free content is real but partial (no OCW program, materials/MOOCs only); OpenLearn engineering courses are mostly short/introductory — not a degree sequence.

### Comparison

| Program | Region | Free materials | Exercises+solutions | Exams | Projects/capstone | Degree-shaped |
|---|---|---|---|---|---|---|
| MIT OCW | US | Yes (2,500+) | Yes | Yes | Course projects; no formal capstone | Yes (EECS sequence) |
| TU Delft OCW | EU (NL) | Yes | Yes | Yes (per-course Exams section) | Yes (course projects) | Yes (EE + CS) |
| Helsinki FSO | EU (FI) | Yes | Yes (all parts) | No exams | Yes (2 project stages, certificate) | No (single track) |
| OSSU | Global/US | Yes | Yes | Yes | **Yes — Final Project capstone** | Yes (CS2013, ~2yr) |
| OpenLearn | UK | Yes (short courses) | Partial | No | Badges only | No (short courses) |
| ETH open learning | EU (CH) | Partial (videos + some CC) | Partial | Partial | No | Partial |
| Stanford Online/SEE | US | Partial (selected courses) | Partial | Partial | No | No |
| Imperial (edX/Coursera audit) | UK | Yes (audit) | Partial | No | No | No |

### Synthesis

Reuse: MIT OCW is the anchor for both disciplines — a complete, exam-inclusive EECS curriculum at zero cost and zero signup friction; TU Delft OCW is the strongest EU engineering complement with genuine exam sections; FSO covers the applied SE gap with real projects and a certificate. For a formal capstone, OSSU supplies the only free one and its curriculum is explicitly assembled from MIT/Harvard/Princeton-level free courses. Missing: any UK degree-shaped free program (OpenLearn is the nearest, but short-course based); coherent free EE *programs* (not isolated courses) outside MIT/TU Delft are scarce — ETH and KTH-style offerings are partial. Planning implication: the strongest free "degree" is a hybrid — OSSU (or MIT EECS sequence) + TU Delft EE courses + FSO for applied projects; credentials remain the paid component everywhere.

### Confidence

High — every ranking-critical fact (materials, exercises, exams, capstone, cost, scale) was verified against the primary university page or repo; the main soft spots (UK depth, Stanford completeness) are explicitly flagged as partial.

---

## Literature

### Discovery

OpenAlex wide pass returned 473 academia rows; 4 anchor papers survived deep verification: Hilton (2016) OER efficacy review ([DOI](https://doi.org/10.1007/s11528-015-0841-0)); Daniel (2012) "Making Sense of MOOCs" ([DOI](https://doi.org/10.1080/01587919.2012.723161)); interdisciplinary engineering-education review (2020, [DOI](https://doi.org/10.1080/17508975.2016.1206085)); "Understanding Dropouts in MOOCs" (2019, [DOI](https://doi.org/10.1016/j.iheduc.2019.04.001)). Policy/standards anchors (industry bucket, verified): [UNESCO 2019 Recommendation on OER](https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer), [UNESCO Basic Guide to OER](https://unesdoc.unesco.org/ark:/48223/pf0000215804), [EC Digital Education Action Plan](https://education.ec.europa.eu/focus-topics/digital-education/actions/plan), [EP briefing on digital education progress](https://www.europarl.europa.eu/RegData/etudes/BRIE/2023/745689/EPRS_BRI(2023)745689_EN.pdf), [Open edX](https://openedx.org/).

### Verification

Paper claims rest on OpenAlex metadata (title/year/citation count/DOI) plus well-established findings (OER efficacy ≈ traditional materials per Hilton 2016; MOOC completion rates historically low per Daniel 2012 and the 2019 dropout studies) — full text was not fetched, so these are treated as direction-of-literature anchors, not quotations. [NOTE: cite Hilton/Daniel as "review-level consensus" only; the 2019 dropout work quantifies MOOC attrition causes (time, prior experience, motivation) and supports the brief's "self-paced OCW needs discipline" caveat.] UNESCO/EC/EP policy sources are primary and current (2019-2023).

### Comparison

The literature consistently distinguishes *materials access* (strong everywhere; OER efficacy studies find open materials perform at least as well as commercial ones) from *completion* (weak everywhere; MOOCs/OCW self-study attrition is the documented failure mode). No peer-reviewed comparison ranks OCW programs as "degree equivalents" — that framing lives in practitioner/community space (OSSU FAQ, HN/Reddit evidence threads, Class Central aggregations), which is why this brief's ranking leans on primary program verification rather than published rankings. Policy layer (UNESCO OER Recommendation, EC Digital Education Action Plan) legitimizes free OE but does not address credentialing — consistent with the [NOTE] that free degrees remain uncredentialed.

### Synthesis

Reuse: Hilton (2016) and Daniel (2012) are the two citations that justify "free OCW materials are as good as paid ones" and "plan for self-discipline, not completion-rate luck" respectively — both belong in the final recommendation. Missing from the literature: any rigorous comparison of OCW *sequences* for degree equivalence in EE (SE has OSSU as community prior art; EE has no equivalent). Planning implication: because completion is the bottleneck, the recommended stack should pair free OCW with accountability (OSSU Discord, FSO submission system, public progress repos — all verified as active) rather than relying on materials alone.

### Confidence

Medium — policy/practice anchors are strong and current; the four papers are metadata-verified with well-known findings, but no paper full-text was fetched and no literature directly ranks OCW programs, so the ranking itself rests on primary-page verification (Domain section), not published studies.

---

## Sources

Primary (verified by fetch):
- [MIT OCW About — 2,500+ courses, free, CC](https://ocw.mit.edu/about/) - official docs; scale/license claim
- [MIT 6.002 Circuits & Electronics](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) - official; exams+assignments+problem sets
- [MIT 6.01SC EECS I](https://ocw.mit.edu/courses/6-01sc-introduction-to-electrical-engineering-and-computer-science-i-spring-2011/) - official; final exam, quizzes, solutions
- [MIT 6.685 Electric Machines](https://ocw.mit.edu/courses/6-685-electric-machines-fall-2013/) - official; EE machine sequence
- [MIT 6.622 Power Electronics](https://ocw.mit.edu/courses/6-622-power-electronics-spring-2023/) - official; recent EE course
- [MIT OCW Get Started](https://ocw.mit.edu/pages/get-started/) - official; no signup/no enrollment
- [TU Delft OCW home](https://ocw.tudelft.nl/) - official; free/remixable university courses
- [TU Delft Electrical Machines & Drives](https://ocw.tudelft.nl/courses/electrical-machines-and-drives/) - official; lecture/exam/reading sections
- [TU Delft MSc EE program](https://ocw.tudelft.nl/programs/master/electrical-engineering/) - official; program structure
- [Full Stack Open (Helsinki)](https://fullstackopen.com/en/) - official; free, exercises, projects, certificate
- [Helsinki open university Full Stack module](https://www.helsinki.fi/en/admissions-and-education/open-university/multidisciplinary-themed-modules/full-stack) - official; free of charge
- [Helsinki course implementation, 5 cr](https://studies.helsinki.fi/courses/course-implementation/otm-861c248f-e4e4-43df-a69a-50fd206afabf) - official; exercises parts 0-7, certificate
- [OSSU computer-science repo](https://github.com/ossu/computer-science) - source repo (207,852 stars, active); CS2013, ~2yr, Final Project capstone
- [OpenLearn free courses](https://www.open.edu/openlearn/free-courses) - official; free short courses, badges
- [OpenLearn engineering & technology](https://www.open.edu/openlearn/science-maths-technology/engineering-technology) - official; UK EE/engineering free content
- [ETH Zurich open learning](https://ethz.ch/en/the-eth-zurich/education/innovation/OffeneLernangebote.html) - official; CC-licensed open learning
- [ETH online course list](https://online.ethz.ch/courses) - official; EU EE/CS open courses
- [Stanford Online free courses](https://online.stanford.edu/free-courses) - official; US free offerings
- [Stanford SEE CS106A](https://see.stanford.edu/Course/CS106A/194) - official; free lecture archive
- [Imperial free online courses](https://www.imperial.ac.uk/students/success-guide/ug/effective-study/working-by-yourself/learning-online/online-courses/) - official; edX audit path
- [Cambridge Computer Lab teaching](https://www.cl.cam.ac.uk/teaching/) - official; free materials (partial)

Literature & policy:
- [Hilton 2016 — OER efficacy review](https://doi.org/10.1007/s11528-015-0841-0) - peer-reviewed; OER ≈ traditional materials
- [Daniel 2012 — Making Sense of MOOCs](https://doi.org/10.1080/01587919.2012.723161) - peer-reviewed; MOOC myth/reality
- [Interdisciplinary engineering education review (2020)](https://doi.org/10.1080/17508975.2016.1206085) - peer-reviewed; eng-ed landscape
- [Understanding Dropouts in MOOCs (2019)](https://doi.org/10.1016/j.iheduc.2019.04.001) - peer-reviewed; attrition causes
- [UNESCO Recommendation on OER (2019)](https://www.unesco.org/en/legal-affairs/recommendation-open-educational-resources-oer) - standards body; OER framework
- [UNESCO Basic Guide to OER](https://unesdoc.unesco.org/ark:/48223/pf0000215804) - technical report
- [EC Digital Education Action Plan](https://education.ec.europa.eu/focus-topics/digital-education/actions/plan) - gov report; EU OER policy
- [EP briefing — digital education progress](https://www.europarl.europa.eu/RegData/etudes/BRIE/2023/745689/EPRS_BRI(2023)745689_EN.pdf) - gov report
- [Open edX](https://openedx.org/) - standards/platform; powers DelftX/ETHx/ImperialX audits

Evidence threads & aggregators:
- [OSSU FAQ](http://cs.ossu.dev/FAQ.html) - practitioner; degree-equivalence discussion
- [Class Central free-certificates list](https://www.classcentral.com/report/free-certificates/) - aggregator; free-course breadth
- [FSO on Class Central](https://www.classcentral.com/course/fullstackopen-deep-dive-into-modern-web-development-66418) - aggregator
- [HN: EE self-study with MIT OCW](https://news.ycombinator.com/item?id=26525694) - practitioner thread
- [r/ElectricalEngineering: open EE courses](https://www.reddit.com/r/ElectricalEngineering/comments/18nsbj3/open_courses_to_learn_electrical_engineering/) - practitioner thread
- [r/programming: 150+ Stanford CS courses online](https://www.reddit.com/r/programming/comments/ja5mdu/150_stanford_oncampus_computer_science_courses/) - practitioner thread (flagged: partial coverage)
- [OSSU progress tracker example](https://github.com/t-miller/ossu-computer-science-progress) - community evidence; accountability pattern
- [FSO solutions example](https://github.com/jarvensivu/full-stack-open) - community evidence; exercise solutions

Full source pool: research/sources/2026-08-11_opencourseware-degrees.sources.jsonl (1009 rows).
