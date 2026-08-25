# Lesson Map: GAP Energy-Efficiency-as-a-Service Crash Course (2 weeks, 11 lessons)

Numbers are assigned at authoring time (`max(existing) + 1`, zero-padded 4 digits); the rows
below are listed in intended study order. `ee-heat` paths are read-only references at
`C:\Users\tukum\Downloads\ee-heat\`.

| # | Day | Slug | Primary tool/source | Focus |
|---|---|---|---|---|
| 0001 | 1 | thermo-and-heat-transfer-primer | free DOE/public thermo reference | conduction, convection, sensible vs. latent heat, why °C/bar(g)/kJ units matter |
| 0002 | 1–2 | refrigeration-cycle-and-cop | free public refrigeration-cycle reference | vapor-compression cycle, COP definition, ideal vs. actual COP |
| 0003 | 2–3 | steam-systems-fundamentals | DOE AMO steam-system reference | boiler efficiency, blowdown, condensate return, flash steam, header balance |
| 0004 | 3–4 | measur-hands-on-steam-and-waste-heat | MEASUR v1.8.3 + `ee-heat/tools/measur/VN-settings-card.md` | localize MEASUR to Vietnam, run Steam System Modeler + Waste Heat Recovery on the placeholder garment-plant defaults |
| 0005 | 5 | tea-lcoh-fundamentals | free public TEA/LCOH reference | discounting, payback, levelized cost of heat, why sizing against an unoptimized load overstates equipment |
| 0006 | 6–7 | reopt-hands-on-scenario-building | `ee-heat/tools/reopt/` (read) → practice copy | `ProcessHeatLoad`/`ExistingBoiler`/`ElectricHeater` inputs, run the existing baseline scenario in a practice copy, reproduce the published NPV/emissions numbers |
| 0007 | 7 | tou-tariffs-and-breakeven-cop | `ee-heat/tools/reopt/vn_context.json` | reproduce the breakeven-COP table by hand using the plan's Specification formula |
| 0008 | 8 | heat-pump-model-cross-check | `ee-heat/tools/heat-pump-model/` | run the CoolProp-based model, verify the corroborated COP 3.11 dye-house finding, understand why its cost output is unusable |
| 0009 | 9 | energyplus-envelope-hvac-orientation | `ee-heat/tools/energyplus/` | run `1ZoneUncontrolled.idf` against the Ho Chi Minh weather file; understand why this tool is standby (envelope/HVAC only, not dye-house steam) |
| 0010 | 9–10 | ihda-fied-methodology | `ee-heat/tools/reference/` | temperature-range-by-end-use methodology; why the US EPA/EIA numbers can't be reused but the method can |
| 0011 | 11–14 | capstone-thermal-storage-sizing | practice copy of `ee-heat/tools/reopt/` | add `ASHPWaterHeater` (COP 3.11) + `HotThermalStorage` to the practice scenario, run, verify against the breakeven-COP table |
