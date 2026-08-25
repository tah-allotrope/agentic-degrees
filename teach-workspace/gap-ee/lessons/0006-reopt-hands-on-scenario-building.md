# 0006 · REopt Hands-On: Scenario Building

> gap-ee week 2, days 6-7 · 90-120 min hands-on. Companion markdown; canonical version is
> `0006-reopt-hands-on-scenario-building.html`.

## 0. Setup (practice copy — never touch live ee-heat)

```
cd C:\Users\tukum\Downloads\agentic-degrees\teach-workspace\gap-ee\capstone\reopt-practice
julia --project=. -e "using Pkg; Pkg.instantiate()"     # once; minutes of precompile
"C:\Users\tukum\Downloads\ee-heat\tools\.venv\Scripts\python.exe" make_vn_scenario.py
julia --project=. run_scenario.jl garment_factory_process_heat.json
```

Verified baseline output (2026-08-25 run):
- `Electric heater size (mmbtu/hr): 0.0`, `NPV ($) : 0.0`
- `CO2 emissions, optimal (t/yr) : 13740.1` (±1.0 tolerance vs published 13,740)
- `termination_status = OPTIMAL` ×2; EASIUR/AVERT warnings expected & harmless.

## 1. Scenario JSON, field by field

| Key | Content | Trap |
|---|---|---|
| Site | lat 10.95, lon 106.82 | US-only lookups → warnings |
| ElectricLoad | 12 GWh/yr, FlatLoad_16_5, year 2017 | `doe_reference_name` |
| ElectricTariff | `tou_energy_rates_per_kwh` (8760) | length must be 8760 |
| ElectricUtility | EF series 1.4533 lb/kWh; RE fraction [0.45]×8760; decrease 0 | RE fraction must be ARRAY |
| ProcessHeatLoad | 60,000 MMBtu/yr steam | `industrial_reference_name` |
| ExistingBoiler | steam, η 0.75, natural_gas @ $5.30 + 214.2 lb CO₂/MMBtu | coal workaround |
| ElectricHeater | COP 1.0, $110k/(MMBtu/h) | declined in baseline |
| Financial | 20 yr, 10% discount, 3% escalation | matches lesson 0005 |

## 2. Coal workaround (memorize)

No native coal type → `natural_gas` + override BOTH:
`fuel_cost_per_mmbtu: 5.30`, `emissions_factor_lb_CO2_per_mmbtu: 214.2`.
Missing EF override ⇒ −45% coal emissions, all abatement claims wrong.

## 3. Why TARIFF_YEAR = 2017

Built-in load profiles are 2017 calendars; matching years keeps Mon–Sat peaks on the right
weekdays (else the SAM-style −4.2% class of error).

## 4. Reading output

- Two solves: BAU vs optimal — compare LCCs to each other.
- Emissions check: 60,000 MMBtu × 214.2 lb ÷ 2204.6 ≈ 5,829 t boiler + 7,911 t grid = 13,740.
- `results_garment_factory_process_heat.json` = full dump for Phase-4 comparison.

## Quiz (6 questions)

1. natural_gas for coal → **no native coal; override BOTH cost and EF**.
2. ProcessHeatLoad key → **industrial_reference_name**.
3. Scalar RE fraction → **runtime failure**; use [x]×8760.
4. Baseline heater verdict → **0 MMBtu/hr, NPV $0 — resistance loses at every hour**.
5. TARIFF_YEAR 2017 → **load-profile calendar alignment**.
6. 13,740.1 vs 13,740 → **valid reproduction within ±1.0 rounding**.

## Primary source

NREL REopt.jl docs (https://reopt.nrel.gov/reopt-jl) + the pinned practice-copy files
(byte-identical copies of `C:\Users\tukum\Downloads\ee-heat\tools\reopt\`).
