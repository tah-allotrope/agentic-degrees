# 0003 · Steam Systems Fundamentals

> gap-ee week 1, days 2-3 · 45-60 min. Companion markdown; canonical version is
> `0003-steam-systems-fundamentals.html`.

## 1. Boiler efficiency

```
η_boiler = useful heat in steam / fuel energy burned      (placeholder plant: 0.75 as-found)
```

- Coal $5.30/MMBtu fuel → **$7.07/MMBtu useful delivered heat** ($5.30 ÷ 0.75). This is the
  denominator of every breakeven-COP comparison later.
- Efficiency gains shrink the load AND worsen heat-pump relative economics → sequencing rule.

## 2. The five checks (VN settings card's exact order)

1. **Condensate return** — saves fuel + treatment chemicals + water; usually biggest, cheapest.
2. **Blowdown rate & heat recovery** — purge concentrated water without dumping its heat;
   flash tank + HX preheats make-up.
3. **Flash steam recovery** — high-pressure condensate dropped to lower pressure partially
   re-boils (10–20% per stage); capture it into deaerator/low-pressure header.
4. **Stack losses / excess air** — trim excess O₂, add economizer; cheapest combustion-side win.
5. **Distribution insulation** — bare headers/valves radiate+conduct away all shift.

Ordering = largest-and-cheapest first for a garment plant.

## Worked example — condensate return

```
60,000 MMBtu/yr load, coal $5.30/MMBtu.
Dump vs 80% return: make-up ΔT ≈ 43°C → ~180 kJ/kg extra sensible duty at η=0.75,
plus water/chemical/blowdown costs. Multiply by operating hours → Check #1 justified.
```

MEASUR computes it exactly from your pressures and loads — that is lesson 0004.

## Quiz (6 questions)

1. Condensate return saves → **fuel + chemicals + water**.
2. Blowdown → **purging concentrated boiler water** to cap dissolved solids.
3. Flash steam → **condensate dropped to lower pressure re-boils part of itself**.
4. Useful heat cost → **$7.07/MMBtu** ($5.30 ÷ 0.75).
5. Ordering logic → **largest-and-cheapest first**, not MEASUR capability limits.
6. Skipping optimization before REopt → **over-sized equipment, wrong LCOH** (~30% over-buy).

## Primary sources

- DOE AMO Steam Sourcebook 2nd ed.:
  https://www.energy.gov/sites/prod/files/2014/05/f15/steamsourcebook.pdf
- Checklist order: `C:\Users\tukum\Downloads\ee-heat\tools\measur\VN-settings-card.md`,
  "What to look for first".
