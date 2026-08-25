# 0005 · TEA & LCOH Fundamentals

> gap-ee week 1, day 5 · 45-60 min. Companion markdown; canonical version is
> `0005-tea-lcoh-fundamentals.html`.

## 1. Discounting & NPV

Future cash flows divided by `(1+r)^n` (r = 10% offtaker rate in the scenarios). NPV sums
discounted capital + fuel/electricity/O&M − savings. **NPV $0** in REopt output = building it
doesn't beat doing nothing (why the COP-1.0 electric heater gets size 0).

## 2. Simple payback

```
payback_years = capital_cost / annual_net_savings
```
Undiscounted, blind past payback year. Communicate with it; decide with NPV/LCOH.

## 3. LCOH

```
LCOH = total lifecycle cost / total lifetime heat delivered    [$/MMBtu]
```
One comparable number per MMBtu across boiler vs heat pump vs solar thermal.

Worked example — 60,000 MMBtu/yr, r = 10%, 20 yr (annuity factor ≈ 8.514):

```
System H heat pump: capex $2.4M → $281,900/yr; O&M $24k;
electricity: 17,584,260 kWh_th ÷ COP 3.11 ≈ 5,653,460 kWh_e × $0.06983 ≈ $394,800/yr
LCOH_H = (281,900+24,000+394,800)/60,000 ≈ $11.68/MMBtu   (energy term alone ≈ $6.58/MMBtu)

System B coal boiler: capex $600k → $70,500/yr; O&M $12k;
coal: 80,000 MMBtu × $5.30 = $424,000/yr
LCOH_B = (70,500+12,000+424,000)/60,000 ≈ $8.44/MMBtu
```

Reads:
- Energy-only heat cost at blended normal rate = $6.58/MMBtu — matches ee-heat's published
  COP-3.11 figure.
- Off-peak pricing (−35%) via thermal storage flips the verdict → that optimization is the
  capstone's job, hour by hour.
- Capital dominates LCOH_H ⇒ unoptimized load ⇒ inflated LCOH — sequencing rule with numbers.

## Quiz (6 questions)

1. NPV $0 → **no value created vs BAU; REopt declines to build**.
2. Payback ignores → **time value of money**.
3. LCOH → **lifecycle cost ÷ lifetime heat delivered** ($/MMBtu).
4. System H dominated by → **annualised capital** (~$306K of ~$701K/yr).
5. Heat pump still promising because → **blended rate hides off-peak win + storage lever**.
6. Unoptimized load corrupts → **LCOH** (over-sized machine inflates lifetime cost).

## Primary sources

- NREL/TP-5700-84560 *High-Temperature Heat Pump Model Documentation and Case Studies*:
  https://www.nrel.gov/docs/fy23osti/84560.pdf
- Sequencing rule: `C:\Users\tukum\Downloads\ee-heat\activeContext.md`.
