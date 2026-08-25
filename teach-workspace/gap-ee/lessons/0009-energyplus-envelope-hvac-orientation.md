# 0009 · EnergyPlus Envelope/HVAC Orientation

> gap-ee week 2, day 9 · 45-60 min hands-on. Companion markdown; canonical version is
> `0009-energyplus-envelope-hvac-orientation.html`.

## 1. The run (inside ee-heat's gitignored dir — zero tracked-state risk)

```
cd C:\Users\tukum\Downloads\ee-heat\tools\energyplus
.\EnergyPlus-26.1.0-6f2e40d102-Windows-x86_64\energyplus.exe ^
  -w weather\VNM_SVN_Ho.Chi.Minh-Tan.Son.Nhat.Intl.AP.489000_TMYx.2011-2025.epw ^
  -d out ^
  -r EnergyPlus-26.1.0-6f2e40d102-Windows-x86_64/ExampleFiles/1ZoneUncontrolled.idf
```

Verified (2026-08-25 run): "Completed Successfully", ~12 s.
`Site:Location,Ho.Chi.Minh-Tan.Son.Nhat.Intl.AP SVN VNM SRC-TMYx WMO#=489000,10.82,106.65,7.00,...`
in `out/eplusout.eio`; err summary: **3 warnings, 0 Severe, 0 Fatal**.

## 2. What ran physically

Single zone, no HVAC → hourly heat balance (conduction, solar, infiltration) on a full TMYx
year for HCMC. Weather trio: .epw (typical year), .ddy (design days), .stat (climate summary).

## 3. Why standby

Targets are PROCESS end uses (dye baths, wash water, dryers on steam/HW loops) — not building
zones. E+ has no steam headers, no boiler part-load economics, no TOU optimization. Future
role: factory-floor ventilation/cooling if it proves material. "Do not spend Stage 1 hours here."

Pattern worth keeping: every tool shipped US-only defaults; localize data first, verify
ingestion explicitly, then check model-class vs question.

## Quiz (6 questions)

1. Site:Location confirms → **weather file genuinely ingested** (not silently defaulted).
2. Failure convention → **Severe/Fatal lines**; warnings are normal.
3. Zero tracked-state risk → **tools/energyplus/ is gitignored by construction**.
4. Standby despite working → **model-class mismatch: buildings ≠ dye-house steam**.
5. Re-entry trigger → **ventilation/cooling becomes a material EE opportunity**.
6. Shared localization flaw → **US-only shipped defaults everywhere** — localization is the
   engagement's core engineering layer.

## Primary source

EnergyPlus v26.1.0 portable + climate.onebuilding.org TMYx HCMC weather file;
`C:\Users\tukum\Downloads\ee-heat\tools\README.md` §4.
