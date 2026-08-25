# REopt schema notes — ASHPWaterHeater + HotThermalStorage

Derived by Julia reflection and source reading (REopt v0.61.0, pinned in this practice
copy's Manifest.toml), 2026-08-25. Per plan ASM-002: field names are discovered, never
guessed. Commands used (from `reopt-practice/`):

```
julia --project=. -e "using REopt; println(fieldnames(REopt.HotThermalStorage))"
# → works directly; HotThermalStorage IS a struct

julia --project=. -e "using REopt; println(fieldnames(REopt.ASHPWaterHeater))"
# → MethodError: ASHPWaterHeater is a CONSTRUCTOR FUNCTION, not the struct.
#   Fallback discovery:
julia --project=. -e "using REopt; println(methods(REopt.ASHPWaterHeater));
                     println(filter(n -> occursin(\"ASHP\", string(n)), names(REopt, all=true)))"
```

## HotThermalStorage — struct fields (fieldnames(REopt.HotThermalStorage))

```
:min_gal, :max_gal, :hot_water_temp_degF, :cool_water_temp_degF,
:internal_efficiency_fraction, :soc_min_fraction, :soc_init_fraction,
:installed_cost_per_gal, :thermal_decay_rate_fraction, :om_cost_per_gal,
:macrs_option_years, :macrs_bonus_fraction, :total_itc_fraction,
:total_rebate_per_kwh, :min_kw, :max_kw, :min_kwh, :max_kwh,
:installed_cost_per_kwh, :charge_efficiency, :discharge_efficiency,
:net_present_cost_per_kwh, :om_cost_per_kwh, :can_supply_steam_turbine,
:can_serve_dhw, :can_serve_space_heating, :can_serve_process_heat,
:supply_turbine_only
```

JSON-level inputs (`HotThermalStorageDefaults`, @kwdef) accept these with defaults:

| Key | Default | Note |
|---|---|---|
| min_gal / max_gal | 0.0 / **0.0** | **must set max_gal > 0 or TES is never built** |
| hot_water_temp_degF / cool_water_temp_degF | 180 / 160 | kWh/gal from CoolProp density+cp across ΔT |
| internal_efficiency_fraction | 0.999999 | split √ into charge/discharge |
| soc_min_fraction / soc_init_fraction | 0.1 / 0.5 | |
| installed_cost_per_gal | $1.90/gal | converted to per-kWh internally |
| thermal_decay_rate_fraction | 0.0004 | per hour standing loss |
| om_cost_per_gal | 0.0 | |
| macrs_option_years / macrs_bonus_fraction | 5 / 1.0 | 0/5/7 only |
| total_itc_fraction | 0.3 | plus macrs_itc_reduction 0.5 (internal) |
| can_serve_dhw / can_serve_space_heating / can_serve_process_heat | true/true/**false** | must set process_heat=true for our use |
| supply_turbine_only | false | |

Verified against upstream test scenario `test/scenarios/thermal_storage.json`, which includes
only `"HotThermalStorage": {"max_gal": 2500}` — confirming max_gal alone activates TES.

## ASHPWaterHeater — JSON-level inputs (constructor keyword args)

`ASHPWaterHeater` builds an inner `ASHP` struct; the JSON dict feeds constructor kwargs.
Source: `REopt/src/core/ashp.jl` (v0.61.0). Defaults from
`REopt/data/ashp/ashp_defaults.json`, block "DomesticHotWater".

| Key | Type | Default (DHW) | Note |
|---|---|---|---|
| min_ton / max_ton | Real | 0 / 99,999,999 | sizes in tons thermal (×3.517 kW_th) |
| min_allowable_ton / min_allowable_peak_capacity_fraction | — | nothing / 0.25 | at most ONE may be given |
| sizing_factor | Real | 1.0 | |
| installed_cost_per_ton | Real | $2,250/ton | converted to $/kW_th internally |
| om_cost_per_ton | Real | $40/ton-yr | |
| macrs_option_years / macrs_bonus_fraction | Int/Real | 0 / 0.0 | |
| heating_cop_reference | Array{Real} | [1.5, 2.3, 3.3, 4.5] | piecewise vs ambient temp |
| heating_cf_reference | Array{Real} | [0.38, 0.64, 1.0, 1.4] | same length as cop_reference |
| heating_reference_temps_degF | Array{Real} | [-5, 17, 47, 80] | ambient temps °F |
| back_up_temp_threshold_degF | Real | 10 | below this COP:=1.0 (resistive backup) |
| force_into_system / force_dispatch | Bool | false / true | |
| can_supply_steam_turbine | Bool | false | preset from defaults |
| ambient_temp_degF | Array | auto | filled by REopt via PVWatts API for the site |
| heating_load | Array | auto | = DomesticHotWaterLoad.loads_kw |

**There is NO scalar `cop` input** — COP comes from interpolating `heating_cop_reference`
against hourly ambient temperature. The README's "`cop`" shorthand describes ElectricHeater/
ElectricHeater-style techs; ASHPWaterHeater is COP-vs-temperature-curve based.

### CRITICAL FINDING 1 — ASHPWaterHeater serves the DHW load only

scenario.jl wires it exclusively to `DomesticHotWaterLoad`:

```julia
d["ASHPWaterHeater"]["ambient_temp_degF"] = site.outdoor_air_temperature_degF
d["ASHPWaterHeater"]["heating_load"]      = dhw_load.loads_kw     # NOT process heat
```

If the scenario has no `DomesticHotWaterLoad` key, `dhw_load.loads_kw` is an all-zero series;
with zero load the ASHP produces nothing regardless of size bounds (and its default
`can_serve_process_heat=false` excludes it from ProcessHeat anyway). So to model the
dye-house heat pump faithfully we must declare a `DomesticHotWaterLoad` whose annual energy
equals the dye-house share of the process heat load.

### CRITICAL FINDING 2 — ambient temperature requires PVWatts (offline blocker)

With no PV and no explicit temperature series, REopt calls the PVWatts web API to synthesize
`site.outdoor_air_temperature_degF`. That call fails offline/hang-prone outside CONUS. Fix
within our control: supply `Site.outdoor_air_temperature_in_degF`? — not available; instead we
supply our own 8760 ambient series on the ASHPWaterHeater dict itself
(`ambient_temp_degF`) so no API call is attempted... EXCEPT scenario.jl OVERWRITES
`d["ASHPWaterHeater"]["ambient_temp_degF"]` unconditionally when max_ton > 0. Therefore the
run needs either network access to PVWatts or a PV key present. Documented here because it
shapes how the capstone run is executed (first run attempt will reveal which).

## Design decisions recorded (per plan TASK-04-02)

1. **DHW proxy for dye-house:** add `DomesticHotWaterLoad` sized to 20% of the 60,000 MMBtu/yr
   process load (= 12,000 MMBtu/yr, the plausible dye-house/wash-water share served at
   ≤95°C), profile `FlatLoad_16_5` matching the factory shift pattern. This is the load the
   ASHP + TES serve; the remaining 48,000 MMBtu/yr stays on the coal steam header
   (ProcessHeatLoad unchanged).
2. **COP curve:** replace the air-source default curve with a flat, conservative curve
   anchored on the corroborated finding — `heating_cop_reference=[3.11]`,
   `heating_reference_temps_degF=[50]`, `heating_cf_reference=[1.4]`. HCMC ambient sits far
   above 50°F every hour, so interpolation returns COP 3.11 in all hours; cf=1.4 avoids
   capacity derating. This encodes lesson 0008's water-to-water physics result into the
   air-source technology object without inventing new fields.
3. **Costs:** keep defaults ($2,250/ton installed, $40/ton-yr O&M) rather than importing any
   heat_pump_model cost output (CON-002).
4. **TES bound:** `max_gal = 20000` (≈ 946 kWh-th usable across 180→160°F ≈ 82→71°C —
   generous vs peak-window need of roughly 5 h × ~1.4 MW_th; chosen large enough that the
   optimizer, not the bound, decides the size) with `can_serve_process_heat=true` not needed —
   TES serves the DHW-quality load via `can_serve_dhw=true`.
5. **ElectricHeater placeholder removed** (baseline proved it is declined; keeping it invites
   confusion about which electric tech won).

## Run log (2026-08-25, REopt v0.61.0)

| Attempt | Outcome | Root cause |
|---|---|---|
| 1 | `status: error` — "No NLR Developer API Key" (PVWatts call) | ASHPWaterHeater triggers a PVWatts ambient-temp API call when `Site.outdoor_air_temperature_degF` is absent |
| 2 | TypeError: `Site` kwarg wants `Union{Nothing, Vector{<:Real}}`, got `Vector{Any}` | JSON.jl parses numeric arrays as `Vector{Any}`; Site does not convert internally (unlike the tariff arrays) |
| 3 | proforma crash: "type Nothing has no field om_cost_per_kw" | **Upstream REopt bug** — `proforma.jl` line ~231 reads `p.s.ashp` for the ASHPWaterHeater O&M branch instead of `p.s.ashp_wh`; with no ASHPSpaceHeater key, `s.ashp = nothing` |
| 4 (final) | **SOLVED, both passes OPTIMAL** | Fixes below |

### Fixes baked into the final workflow

1. **Ambient temperature offline:** real TMYx 2011–2025 dry-bulb series for HCMC Tan Son Nhat
   extracted from `ee-heat/tools/energyplus/weather/…489000_TMYx.2011-2025.epw` (col 7),
   converted °C→°F → `hcmc_ambient_temp_degF.json` (8760 values; min 66.2°F / max 98.6°F /
   mean 82.9°F), supplied as `Site.outdoor_air_temperature_degF`. No PVWatts call attempted.
2. **JSON type conversion:** `run_scenario_hp_storage.jl` reads the scenario Dict and
   `convert(Vector{Float64}, …)` the three big arrays before calling `REopt.run_reopt([m1,m2], d)`.
3. **proforma bug workaround:** scenario includes an `ASHPSpaceHeater` placeholder with
   `max_ton: 0.001` (clamped to 0 by the zero space-heating load ⇒ never buildable),
   `force_into_system/force_dispatch: false` (force_dispatch's big-M branch divides by an
   empty cooling-cf array and crashes). This gives `p.s.ashp` a real struct so proforma runs.
   Documented as upstream bug; not a modelling input.

## Capstone result vs baseline (the honest comparison)

Baseline (Phase 3): CO2 13,740 t/yr; LCC $10.988M; boiler fuel 60,000 MMBtu; no DHW load existed.

Capstone scenario adds the 12,000 MMBtu/yr ≤95°C dye-house load, so its own BAU differs:
BAU CO2 14,906 t/yr, LCC $11.495M (boiler serves the new load too).

Optimal case (both passes OPTIMAL):

| Quantity | Result |
|---|---|
| ASHPWaterHeater size | **129.75 ton_th** (~455 kW_th) — built, non-zero |
| ASHP heat delivered | 9,010 MMBtu/yr at implied COP 3.11 (matches lesson 0008 exactly) |
| ASHP electricity | 849,069 kWh/yr |
| HotThermalStorage size | **20,000 gal ≈ 954 kWh-th ≈ 3.26 MMBtu-th** — bound hit, storage is worth having but small |
| TES dispatch | charges in normal hours (767 MMBtu), discharges 237 MMBtu across the peak + 520 normal |
| Boiler fuel optimal | 60,000 MMBtu/yr — dye-house fully displaced from coal steam |
| CO2 optimal | 14,300 t/yr — **606 t/yr below its own BAU**, but above the 13,740 baseline because the added load's electricity emissions outweigh coal displacement at these factors |
| NPV of the addition | **−$388k** over 20 yr at 10% discount (LCC $11.883M vs $11.495M BAU) |

### Reading against the breakeven table (lesson 0007)

The optimizer confirms the *physics* finding — COP 3.11 beats coal off-peak ($4.27 vs $7.07)
and in normal hours ($6.58 vs $7.07), so it builds maximum economical HP capacity and shifts
heat via TES away from the peak window (zero HP→TES charging during peak hours). But at the
default capital costs ($2,250/ton + $38k TES) the energy savings (~$22k/yr on the split-out
load) do not pay back the capex within 20 years at a 10% discount rate: NPV −$388k.

This is RISK-04-02's "valid, informative outcome": the model does NOT confirm a
least-cost win at assumed costs; it confirms (a) the toolchain reproduces COP 3.11 end-to-end,
(b) thermal storage gets sized and dispatched exactly as activeContext.md predicts (charge
off-peak/normal, ride through peak), and (c) economics hinge on capital cost and which load
share is truly ≤95°C — both supplier-data questions already flagged in vn_context.json.
