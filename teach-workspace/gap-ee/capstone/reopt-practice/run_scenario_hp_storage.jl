#!/usr/bin/env julia
# Capstone runner: same logic as run_scenario.jl, plus in-memory type conversion.
#
# Why this exists: JSON.jl parses every numeric array as Vector{Any}. The baseline
# scenario never hit this because its big arrays feed constructors that convert
# internally; Site's outdoor_air_temperature_degF does NOT convert, and REopt's
# Site kwarg demands Union{Nothing, Vector{<:Real}} -> TypeError on Vector{Any}.
# Fix: read the scenario Dict here, convert the arrays to Vector{Float64}, then
# call REopt.run_reopt(ms, d::Dict) directly.
#
#   julia --project=. run_scenario_hp_storage.jl garment_factory_process_heat_hp_storage.json

using REopt, JuMP, HiGHS, JSON

scenario_file = length(ARGS) >= 1 ? ARGS[1] : "garment_factory_process_heat_hp_storage.json"
println("Scenario: ", scenario_file)

d = JSON.parsefile(scenario_file)

# --- type conversions (Vector{Any} -> Vector{Float64}) -------------------------
site = d["Site"]
site["outdoor_air_temperature_degF"] =
    convert(Vector{Float64}, site["outdoor_air_temperature_degF"])

et = d["ElectricTariff"]
et["tou_energy_rates_per_kwh"] =
    convert(Vector{Float64}, et["tou_energy_rates_per_kwh"])

eu = d["ElectricUtility"]
eu["renewable_energy_fraction_series"] =
    convert(Vector{Float64}, eu["renewable_energy_fraction_series"])
eu["emissions_factor_series_lb_CO2_per_kwh"] =
    eu["emissions_factor_series_lb_CO2_per_kwh"]

m1 = Model(optimizer_with_attributes(HiGHS.Optimizer, "output_flag" => false, "log_to_console" => false))
m2 = Model(optimizer_with_attributes(HiGHS.Optimizer, "output_flag" => false, "log_to_console" => false))
results = run_reopt([m1, m2], d)

println("\n=== Headline results ===")
fin = get(results, "Financial", Dict())
println("NPV (\$)                      : ", round(get(fin, "npv", NaN), digits=0))
println("Lifecycle cost, optimal (\$)  : ", round(get(fin, "lcc", NaN), digits=0))
println("Lifecycle cost, BAU (\$)      : ", round(get(fin, "lcc_bau", NaN), digits=0))

if haskey(results, "ASHPWaterHeater")
    hp = results["ASHPWaterHeater"]
    println("\nASHP water heater size (ton)       : ", get(hp, "size_ton", 0.0))
    println("ASHP thermal served (mmbtu/yr)     : ",
            round(get(hp, "annual_thermal_production_mmbtu", 0.0), digits=0))
    println("ASHP electric use (kWh/yr)         : ",
            round(get(hp, "annual_electric_consumption_kwh", 0.0), digits=0))
end

if haskey(results, "HotThermalStorage")
    tes = results["HotThermalStorage"]
    println("\nHot TES size (kWh-thermal)         : ", get(tes, "size_kwh", 0.0))
    println("Hot TES size (gal)                 : ", get(tes, "size_gal", 0.0))
end

if haskey(results, "ExistingBoiler")
    eb = results["ExistingBoiler"]
    println("\nBoiler fuel, optimal (mmbtu/yr)    : ",
            round(get(eb, "annual_fuel_consumption_mmbtu", 0.0), digits=0))
    println("Boiler fuel, BAU (mmbtu/yr)        : ",
            round(get(eb, "annual_fuel_consumption_mmbtu_bau", 0.0), digits=0))
end

if haskey(results, "Site")
    s = results["Site"]
    println("\nCO2 emissions, optimal (t/yr)      : ",
            round(get(s, "annual_emissions_tonnes_CO2", NaN), digits=1))
    println("CO2 emissions, BAU (t/yr)          : ",
            round(get(s, "annual_emissions_tonnes_CO2_bau", NaN), digits=1))
end

outname = "results_" * replace(basename(scenario_file), ".json" => "") * ".json"
open(outname, "w") do f
    JSON.print(f, results, 2)
end
println("\nFull results written to ", outname)
