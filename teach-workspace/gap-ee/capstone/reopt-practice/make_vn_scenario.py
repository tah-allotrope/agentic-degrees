"""Build the REopt scenario from vn_context.json.

Generates the 8760-hour Vietnamese time-of-use tariff vector and writes
garment_factory_process_heat.json. Re-run after editing vn_context.json.

    ../.venv/Scripts/python.exe make_vn_scenario.py
"""
import json
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).parent
CTX = json.loads((HERE / "vn_context.json").read_text(encoding="utf-8"))

# REopt's built-in CRB load profiles are 2017 profiles, so the tariff calendar
# must be 2017 or the peak windows land on the wrong days of the week.
TARIFF_YEAR = 2017


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

    scenario = {
        "_generated_by": "make_vn_scenario.py from vn_context.json - do not hand-edit, edit the context file",
        "Site": {"latitude": fac["latitude"], "longitude": fac["longitude"]},
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
        "ExistingBoiler": {
            "production_type": "steam",
            "efficiency": fac["existing_boiler_efficiency"],
            "fuel_type": "natural_gas",  # stands in for coal - see vn_context.json
            "fuel_cost_per_mmbtu": fuel["usd_per_mmbtu"],
            "emissions_factor_lb_CO2_per_mmbtu": fuel["emissions_factor_lb_co2_per_mmbtu"],
        },
        "ElectricHeater": {
            "cop": 1.0,
            "can_serve_process_heat": True,
            "installed_cost_per_mmbtu_per_hour": 110000.0,
        },
        "Financial": {
            "analysis_years": 20,
            "offtaker_discount_rate_fraction": 0.10,
            "elec_cost_escalation_rate_fraction": 0.03,
            "existing_boiler_fuel_cost_escalation_rate_fraction": 0.03,
        },
    }

    out = HERE / "garment_factory_process_heat.json"
    out.write_text(json.dumps(scenario, indent=2), encoding="utf-8")

    blended = sum(rates) / len(rates)
    print(f"wrote {out.name}")
    print(f"  peak     ${peak:.5f}/kWh   ({rates.count(peak):>4} h/yr)")
    print(f"  normal   ${normal:.5f}/kWh   ({rates.count(normal):>4} h/yr)")
    print(f"  off-peak ${off:.5f}/kWh   ({rates.count(off):>4} h/yr)")
    print(f"  simple hourly average: ${blended:.5f}/kWh")
    print(f"  coal ${fuel['usd_per_mmbtu']}/MMBtu at {fac['existing_boiler_efficiency']:.0%} boiler "
          f"= ${fuel['usd_per_mmbtu']/fac['existing_boiler_efficiency']:.2f}/MMBtu delivered heat")


if __name__ == "__main__":
    main()
