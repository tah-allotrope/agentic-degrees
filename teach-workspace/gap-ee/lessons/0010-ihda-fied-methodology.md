# 0010 · IHDA/FIED Methodology

> gap-ee week 2, days 9-10 · 30-45 min reading. Companion markdown; canonical version is
> `0010-ihda-fied-methodology.html`.

## 1. The problem

Sites book all heat at header conditions ("10 bar(g) for everything"). Screening needs the
split by temperature band: MMBtu/yr below 100°C, 100–200°C, above. Mis-binned load hides heat-
pump wins (60–95°C band judged against 184°C steam economics).

## 2. The method (Enduse_Calc.py)

1. **End-use taxonomy** — fixed vocabulary of industrial end uses.
2. **Priors per end use × industry** — typical temperature ranges (US GHGRP/MECS ≤2018 — does
   NOT transfer).
3. **Allocate fuel to temperature bins** — sector energy × shares × ranges → binned demand;
   each bin gets its own candidate technology set.
4. **Conservation checksum** — bins roll up to known site total.

FIED adds unit-level characterization structure: each thermal unit by capacity, fuel,
utilization, age — copy as survey template.

## 3. Why numbers never transfer

- GHGRP/MECS = US reporting universes (coverage bias, not measurement).
- US textile mix ≠ VN CMT garment wet-processing intensity.
- ≤2018 vintage vs fast-retooling VN industry.
- No VN/ID equivalent exists — only tool in the stack where localization was impossible.

Defensible workflow: taxonomy + binning yes; priors from supplier data as collected; explicit
UNVERIFIED PLACEHOLDER labels meanwhile (vn_context.json discipline).

## Quiz (6 questions)

1. IHDA answers → **heat-demand split by temperature/end use without direct measurement**.
2. Header-only booking breaks screening → **low-temp loads judged at high-grade economics**.
3. What transfers → **structure**; not GHGRP/MECS numbers.
4. FIED adds → **unit-level characterization survey structure**.
5. Missing prior today → **explicit labelled placeholder, replaced by supplier data later**.
6. Localization impossible because → **the tool IS a US dataset; no domestic equivalent yet**.

## Primary source

NLR `Industrial-Heat-Demand-Analysis` (`Enduse_Calc.py`) + `foundational-industry-energy-data`
at `C:\Users\tukum\Downloads\ee-heat\tools\reference\`; rule from `ee-heat/tools/README.md` §5.
