#!/usr/bin/env julia
# Run a REopt scenario and print the headline clean-heat numbers.
#   julia --project=. run_scenario.jl garment_factory_process_heat.json

using REopt, JuMP, HiGHS, JSON

scenario_file = length(ARGS) >= 1 ? ARGS[1] : "garment_factory_process_heat.json"
println("Scenario: ", scenario_file)

m1 = Model(optimizer_with_attributes(HiGHS.Optimizer, "output_flag" => false, "log_to_console" => false))
m2 = Model(optimizer_with_attributes(HiGHS.Optimizer, "output_flag" => false, "log_to_console" => false))
results = run_reopt([m1, m2], scenario_file)

println("\n=== Headline results ===")
fin = get(results, "Financial", Dict())
println("NPV (\$)                      : ", round(get(fin, "npv", NaN), digits=0))
println("Lifecycle cost, optimal (\$)  : ", round(get(fin, "lcc", NaN), digits=0))
println("Lifecycle cost, BAU (\$)      : ", round(get(fin, "lcc_bau", NaN), digits=0))

if haskey(results, "ElectricHeater")
    eh = results["ElectricHeater"]
    println("\nElectric heater size (mmbtu/hr): ", round(get(eh, "size_mmbtu_per_hour", 0.0), digits=2))
    println("Thermal served (mmbtu/yr)      : ",
            round(get(eh, "annual_thermal_production_mmbtu", 0.0), digits=0))
end

if haskey(results, "ExistingBoiler")
    eb = results["ExistingBoiler"]
    println("\nBoiler fuel, optimal (mmbtu/yr): ", round(get(eb, "annual_fuel_consumption_mmbtu", 0.0), digits=0))
    println("Boiler fuel, BAU (mmbtu/yr)    : ", round(get(eb, "annual_fuel_consumption_mmbtu_bau", 0.0), digits=0))
end

if haskey(results, "Site")
    s = results["Site"]
    println("\nCO2 emissions, optimal (t/yr)  : ",
            round(get(s, "annual_emissions_tonnes_CO2", NaN), digits=1))
    println("CO2 emissions, BAU (t/yr)      : ",
            round(get(s, "annual_emissions_tonnes_CO2_bau", NaN), digits=1))
end

open("results_" * replace(basename(scenario_file), ".json" => "") * ".json", "w") do f
    JSON.print(f, results, 2)
end
println("\nFull results written to results_", replace(basename(scenario_file), ".json" => ""), ".json")
