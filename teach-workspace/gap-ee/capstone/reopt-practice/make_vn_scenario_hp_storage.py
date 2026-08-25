"""Build the REopt HP+TES capstone scenario from vn_context.json.

Capstone variant of make_vn_scenario.py (teach-workspace/gap-ee course):
 - removes the placeholder ElectricHeater block (baseline proved REopt declines it),
 - adds ASHPWaterHeater with the corroborated dye-house COP 3.11 curve,
 - adds HotThermalStorage so REopt sizes thermal storage itself,
 - adds DomesticHotWaterLoad as the <=95 C load the pair serves (20% of process heat),
 - writes garment_factory_process_heat_hp_storage.json (never overwrites the baseline).

    "C:\\Users\\tukum\\Downloads\\ee-heat\\tools\\.venv\\Scripts\\python.exe" make_vn_scenario_hp_storage.py
"""
import json
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).parent
CTX = json.loads((HERE / "vn_context.json").read_text(encoding="utf-8"))

# REopt's built-in CRB load profiles are 2017 profiles, so the tariff calendar
# must be 2017 or the peak windows land on the wrong days of the week.
TARIFF_YEAR = 2017

# --- capstone-specific constants -------------------------------------------------
DHW_SHARE = 0.20          # dye-house/wash-water share of process heat served at <=95 C
HP_COP = 3.11             # corroborated by heat_pump_model on the 45->95 C case
TES_MAX_GAL = 20000       # generous bound; optimizer decides the actual size


def tou_vector():
    """8760 hourly energy rates in USD/kWh, excl. VAT."""
    t = CTX["electricity_tariff"]
    fx = CTX["fx"]["vnd_per_usd"]
    peak, normal, off = (t["rates_vnd_per_kwh"][k] / fx for k in ("peak", "normal", "off_peak"))

    rates, day = [], date(TARIFF_YEAR, 1, 1)
    while day.year == TARIFF_YEAR:
        sunday = day.weekday() == 6
        for hour in range(24):
            if hour < 6:                        # 00:00-06:00 off-peak, every day
                rates.append(off)
            elif not sunday and 17 <= hour < 22:  # Mon-Sat 17:30-22:30, hourly approx
                rates.append(peak)
            else:
                rates.append(normal)
        day += timedelta(days=1)

    assert len(rates) == 8760, f"expected 8760 hourly rates, built {len(rates)}"
    return rates, peak, normal, off


def main():
    rates, peak, normal, off = tou_vector()
    fac, fuel, grid = CTX["facility_placeholder"], CTX["boiler_fuel"], CTX["grid_emissions"]

    dhw_annual_mmbtu = fac["process_heat_annual_mmbtu"] * DHW_SHARE

    scenario = {
        "_generated_by": "make_vn_scenario_hp_storage.py from vn_context.json - capstone variant",
        "Site": {
            "latitude": fac["latitude"],
            "longitude": fac["longitude"],
            # Real TMYx 2011-2025 dry-bulb series for HCMC Tan Son Nhat (from
            # ee-heat's weather file). Supplying it stops REopt from calling the
            # PVWatts web API (needs NLR_DEVELOPER_API_KEY) to synthesize ambient
            # temps for the ASHPWaterHeater COP curve.
            "outdoor_air_temperature_degF": json.loads(
                (HERE / "hcmc_ambient_temp_degF.json").read_text(encoding="utf-8")
            ),
        },
        "ElectricLoad": {
            # ElectricLoad uses doe_reference_name; ProcessHeatLoad uses
            # industrial_reference_name. Both accept the FlatLoad_* variants.
            "doe_reference_name": fac["shift_pattern"],
            "annual_kwh": fac["annual_kwh"],
            "year": TARIFF_YEAR,
        },
        "ElectricTariff": {"tou_energy_rates_per_kwh": rates},
        "ElectricUtility": {
            "emissions_factor_series_lb_CO2_per_kwh": grid["lb_co2_per_kwh"],
            "emissions_factor_CO2_decrease_fraction": grid["decrease_fraction"],
            # Must be an 8760 array. REopt's signature says Union{Real,Array} but a
            # scalar fails with "Unable to convert renewable_energy_fraction_series".
            "renewable_energy_fraction_series": [grid["renewable_energy_fraction"]] * 8760,
        },
        "ProcessHeatLoad": {
            "industrial_reference_name": fac["shift_pattern"],
            "annual_mmbtu": fac["process_heat_annual_mmbtu"],
            "year": TARIFF_YEAR,
        },
        # The <=95 C dye-house/wash-water band, declared as a DHW-quality load:
        # ASHPWaterHeater is wired by REopt to the DomesticHotWaterLoad only.
        "DomesticHotWaterLoad": {
            "doe_reference_name": fac["shift_pattern"],
            "annual_mmbtu": dhw_annual_mmbtu,
            "year": TARIFF_YEAR,
        },
        "ExistingBoiler": {
            "production_type": "steam",
            "efficiency": fac["existing_boiler_efficiency"],
            "fuel_type": "natural_gas",  # stands in for coal - see vn_context.json
            "fuel_cost_per_mmbtu": fuel["usd_per_mmbtu"],
            "emissions_factor_lb_CO2_per_mmbtu": fuel["emissions_factor_lb_co2_per_mmbtu"],
        },
        # ElectricHeater placeholder removed: the Phase-3 baseline showed REopt
        # declines resistance heat (size 0, NPV $0) against coal at every hour.
        "ASHPWaterHeater": {
            "installed_cost_per_ton": 2250.0,   # REopt DHW default; costs stay REopt's (CON-002)
            "om_cost_per_ton": 40.0,
            # Flat conservative COP curve anchored on the corroborated finding:
            # HCMC ambient is always above 50 F, so interpolation yields COP 3.11 all year.
            "heating_cop_reference": [HP_COP],
            "heating_cf_reference": [1.4],
            "heating_reference_temps_degF": [50.0],
            # serve the dye-house (DHW-quality) load, not just building DHW defaults
            "force_into_system": True,
        },
        # REopt v0.61.0 proforma.jl bug workaround: its ASHPWaterHeater O&M branch
        # reads p.s.ashp (the SpaceHeater struct) instead of p.s.ashp_wh, crashing
        # with `type Nothing has no field om_cost_per_kw` when no ASHPSpaceHeater
        # key exists. Provide a struct-with-zero-capacity: max_ton gets clamped to 0
        # by the zero space-heating load, so the optimizer can never build it.
        "ASHPSpaceHeater": {
            "max_ton": 0.001,
            "installed_cost_per_ton": 2250.0,
            "om_cost_per_ton": 40.0,
            "heating_cop_reference": [3.11],
            "heating_cf_reference": [1.4],
            "heating_reference_temps_degF": [50.0],
            "force_into_system": False,
            "force_dispatch": False,
        },
        "HotThermalStorage": {
            # Generous bound so the OPTIMIZER decides the size (plan TASK-04-02).
            "max_gal": TES_MAX_GAL,
        },
        "Financial": {
            "analysis_years": 20,
            "offtaker_discount_rate_fraction": 0.10,
            "elec_cost_escalation_rate_fraction": 0.03,
            "existing_boiler_fuel_cost_escalation_rate_fraction": 0.03,
        },
    }

    out = HERE / "garment_factory_process_heat_hp_storage.json"
    out.write_text(json.dumps(scenario, indent=2), encoding="utf-8")

    blended = sum(rates) / len(rates)
    print(f"wrote {out.name}")
    print(f"  peak     ${peak:.5f}/kWh   ({rates.count(peak):>4} h/yr)")
    print(f"  normal   ${normal:.5f}/kWh   ({rates.count(normal):>4} h/yr)")
    print(f"  off-peak ${off:.5f}/kWh   ({rates.count(off):>4} h/yr)")
    print(f"  simple hourly average: ${blended:.5f}/kWh")
    print(f"  coal ${fuel['usd_per_mmbtu']}/MMBtu at {fac['existing_boiler_efficiency']:.0%} boiler "
          f"= ${fuel['usd_per_mmbtu']/fac['existing_boiler_efficiency']:.2f}/MMBtu delivered heat")
    print(f"  DHW(dye-house) load split out: {dhw_annual_mmbtu:.0f} MMBtu/yr "
          f"({DHW_SHARE:.0%} of {fac['process_heat_annual_mmbtu']})")


if __name__ == "__main__":
    main()
