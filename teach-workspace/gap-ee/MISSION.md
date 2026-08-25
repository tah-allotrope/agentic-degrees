# Mission: GAP Energy-Efficiency-as-a-Service Crash Course

## Why

Become independently able to operate the Gap Inc. clean-heat toolchain — MEASUR,
REopt.jl, `heat_pump_model`, EnergyPlus, IHDA/FIED — and defend a technical finding
without deferring to a consultant, on the active Gap Inc. engagement. The engagement's
own finding (Vietnam's 2.86x peak/off-peak tariff spread means there is no single
breakeven COP for an industrial heat pump against a coal steam boiler; the design answer
is heat pump + thermal storage) is the course's spine: every lesson builds toward being
able to reproduce it from raw inputs and extend it.

## Success looks like

- Localize MEASUR v1.8.3 to Vietnam (Metric units, VN electricity rates, VN emission
  factors) and run Steam System Modeler + Waste Heat Recovery on garment-plant defaults.
- Build, run, and read a REopt.jl process-heat scenario from `vn_context.json` inputs in
  an isolated practice copy, reproducing the published NPV/emissions numbers.
- Reproduce the breakeven-COP table (off-peak 1.88 / normal 2.90 / peak 5.37) by hand
  from the raw VND tariff and FX rate.
- Run `heat_pump_model` on the 45°C→95°C dye-house case and verify ideal COP 6.22 /
  actual COP 3.11, knowing exactly why its cost output must never be used.
- Run EnergyPlus against the Ho Chi Minh weather file and state why the tool is standby
  for this scope.
- Explain the IHDA/FIED temperature-range-by-end-use method and why its US numbers can
  never be quoted for a Vietnamese plant.
- Independently reproduce and extend the Vietnam garment-factory breakeven-COP +
  thermal-storage finding: size an `ASHPWaterHeater` + `HotThermalStorage` pair in REopt
  inside a practice copy.

## Constraints

- 2 weeks, 15–20 h/wk, running parallel to — and fully separate from — the existing
  BESS/grid-EE Phase-1 mission's budget (that mission keeps its own 12–14 h/wk).
- English only.
- Free/public sources only.
- All practice work happens inside `teach-workspace/gap-ee/capstone/reopt-practice/`;
  the live `ee-heat` repository is read-only reference material and is never modified.

## Out of scope

- Client memo / deliverable-writing craft.
- Solar, BESS, or DPPA content (a different workstream).
- Any edit to the live `ee-heat` repository, including its git history.
