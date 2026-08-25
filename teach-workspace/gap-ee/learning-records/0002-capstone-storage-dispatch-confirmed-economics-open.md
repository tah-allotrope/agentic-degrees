# 0002 · Capstone result: storage dispatch confirmed, least-cost win not yet

The capstone ran ASHPWaterHeater (COP 3.11 curve) + HotThermalStorage against the practice-copy
scenario with the dye-house load split out (12,000 MMBtu/yr ≤95°C). Both passes solved OPTIMAL:
REopt built 129.7 ton_th of heat pump serving 9,010 MMBtu/yr at exactly COP 3.11, sized TES at
the bound (20,000 gal ≈ 3.26 MMBtu-th), charged it only in off-peak/normal hours and discharged
237 MMBtu across the Mon–Sat evening peak — dispatch matching activeContext.md's prediction.
Economics did NOT confirm a win: NPV −$388k at default costs ($2,250/ton, $38k TES), CO2 14,300
vs BAU 14,906 t/yr (but above the no-DHW-load baseline's 13,740). Conclusion: physics and
dispatch confirmed; the investment case hinges on real supplier data for capital cost, load
share ≤95°C, and tariff exposure — plus two upstream REopt v0.61.0 bugs worked around
(PVWatts ambient dependency, proforma.jl ashp/ashp_wh mix-up), documented in
capstone/reopt-practice/schema-notes.md.
