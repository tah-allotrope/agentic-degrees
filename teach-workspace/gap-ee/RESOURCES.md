# RESOURCES — trusted sources for the gap-ee crash course

> Knowledge comes from high-trust sources, never the teacher's parametric memory.
> `ee-heat` paths are absolute on this machine (`C:\Users\tukum\Downloads\ee-heat\`)
> and are read-only reference material. URLs below were located and checked live
> (HTTP 200) at authoring time, 2026-08-25.

## Knowledge

### The engagement itself (local, read-only)

- `C:\Users\tukum\Downloads\ee-heat\activeContext.md` — priority order, tool ranking,
  and the breakeven-COP finding (1.88 / 2.90 / 5.37) with the 13,740 tCO2/yr verified
  baseline. Read first; everything in this course hangs off it.
- `C:\Users\tukum\Downloads\ee-heat\tools\README.md` — per-tool usage, localization
  state, the five US-default traps, and why SAM/PySAM cannot express Vietnam's Mon–Sat
  peak window.
- `C:\Users\tukum\Downloads\ee-heat\tools\measur\VN-settings-card.md` — every value to
  enter into MEASUR by hand, plus the garment-plant default parameters.
- `C:\Users\tukum\Downloads\ee-heat\tools\reopt\vn_context.json` — single source of
  truth for all Vietnam numbers (tariff, FX, grid EF, coal price/EF), each with source.

### Thermo / heat transfer (free public)

- DOE AMO, *Improving Steam System Performance: A Sourcebook for Industry*, 2nd ed. —
  <https://www.energy.gov/sites/prod/files/2014/05/f15/steamsourcebook.pdf> — the
  sourcebook MEASUR's steam modules are built on; primary source for lessons 0001–0003.
- LibreTexts Engineering Thermodynamics (Yan), §6.3 "Refrigerator and heat pump" —
  <https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Introduction_to_Engineering_Thermodynamics_(Yan)/06%3A_Entropy_and_the_Second_Law_of_Thermodynamics/6.03%3A_Refrigerator_and_heat_pump> —
  vapor-compression cycle and COP definition; primary source for lesson 0002.
- BCcampus OpenEd, *Introduction to Engineering Thermodynamics*, §6.4 "Carnot cycles" —
  <https://pressbooks.bccampus.ca/thermo1/chapter/6-4-carnot-cycles/> — ideal vs.
  actual COP / second-law reasoning; secondary source for lesson 0002.

### Techno-economics (free public)

- NREL/TP-5700-84560, *High-Temperature Heat Pump Model Documentation and Case Studies*
  (2023) — <https://www.nrel.gov/docs/fy23osti/84560.pdf> — defines LCOH/NPV/payback
  machinery for industrial heat pumps; primary source for lesson 0005.
- REopt.jl documentation (NREL) — <https://reopt.nrel.gov/reopt-jl> — scenario input
  reference for lessons 0006 and 0011.

## Gaps (verified findings)

- REopt.jl's `HotThermalStorage` exact input schema is **not documented anywhere local**
  — `ee-heat/tools/README.md` only names its existence in the "Relevant inputs" list.
  Resolution path: Julia reflection (`fieldnames`) at capstone time, before writing any
  JSON — see plan ASM-002 and capstone `capstone/reopt-practice/schema-notes.md`.
