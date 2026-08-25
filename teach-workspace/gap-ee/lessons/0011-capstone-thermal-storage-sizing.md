# 0011 · Capstone: Heat Pump + Thermal Storage Sizing

> gap-ee week 2, days 11-14 · the gate. Companion markdown; canonical version is
> `0011-capstone-thermal-storage-sizing.html`. Full audit trail:
> `../capstone/reopt-practice/schema-notes.md`.

## 1. Schema discovery (before any JSON)

- `HotThermalStorage`: struct, 28 fields; JSON needs only `max_gal > 0` to activate.
- `ASHPWaterHeater`: constructor function (fieldnames fails); JSON keys = constructor kwargs;
  **no scalar cop** — COP interpolates a curve vs hourly ambient; wired ONLY to the
  DomesticHotWaterLoad series ⇒ dye-house band declared as DHW-quality load
  (12,000 of 60,000 MMBtu/yr).

## 2. Three blockers → root causes → fixes

| Symptom | Root cause | Fix |
|---|---|---|
| PVWatts "No NLR Developer API Key" → NaN | ASHP needs hourly ambient temps | Real TMYx HCMC dry-bulb year from ee-heat's weather file → Site.outdoor_air_temperature_degF |
| TypeError: Vector{Any} vs Vector{<:Real} | JSON.jl parses arrays as Any; Site doesn't convert | `run_scenario_hp_storage.jl` converts arrays in memory |
| proforma: Nothing has no field om_cost_per_kw | Upstream bug: proforma reads p.s.ashp for WaterHeater O&M | Inert ASHPSpaceHeater placeholder (max_ton→0, force_dispatch off) |

## 3. Results — both passes OPTIMAL

| Quantity | Baseline P3 | Capstone BAU | Capstone optimal |
|---|---|---|---|
| CO2 t/yr | 13,740 | 14,906 | **14,300** (−606 vs own BAU) |
| LCC 20 yr | $10.988M | $11.495M | $11.883M (NPV −$388k) |
| Boiler fuel MMBtu/yr | 60,000 | 72,000 | 60,000 (dye-house fully displaced) |
| ASHP size | — | — | **129.7 ton_th**, 9,010 MMBtu/yr @ COP 3.11 |
| TES size | — | — | **20,000 gal ≈ 3.26 MMBtu-th** (bound) |

Dispatch: charge off-peak/normal (767 MMBtu), discharge across Mon–Sat peak (237) + normal
(520). Zero peak-hour charging — matches activeContext.md's design answer exactly.

## 4. Honest verdict (RISK-04-02)

Physics + dispatch confirmed end-to-end (implied delivered-heat COP = 3.11 exactly).
Least-cost win NOT confirmed at default costs: NPV −$388k ($292k HP capex + $38k TES vs
~$22k/yr net energy savings at a 10% discount). CO2 above the old baseline only because the
scenario adds a new load; like-for-like it falls.

Open levers (supplier data): capital quotes, true ≤95°C load share, tariff exposure.
Never tune inputs post-hoc to force a win.

## Quiz (6 questions)

1. PVWatts call because → ambient temps missing for the HP COP curve.
2. DHW-load declaration → ASHPWaterHeater is wired only to dhw_load.loads_kw.
3. COP encoding → flat reference curve [3.11] @ 50°F (HCMC never below).
4. TES behavior → built at bound; charges cheap hours, discharges the peak.
5. Not a regression → like-for-like BAU comparison: −606 t/yr.
6. Defensible conclusion → physics/dispatch confirmed; economics open on supplier data.

## Primary source

Capstone artifacts in `capstone/reopt-practice/`; extended finding:
`ee-heat/activeContext.md`; REopt.jl v0.61.0 source for schema/bug provenance.
