# 0007 · TOU Tariffs & the Breakeven-COP Table

> gap-ee week 2, day 7 · 45-60 min. Companion markdown; canonical version is
> `0007-tou-tariffs-and-breakeven-cop.html`.

## 1. Formula

```
COP_breakeven = (P_elec × 293.071) / (P_coal / η_boiler)
```

Denominator = coal DELIVERED heat: 5.30/0.75 = $7.0667/MMBtu.

## 2. Step 1 — VND→USD by hand (FX = 26,250)

```
peak     : 3,398 ÷ 26,250 = $0.12945/kWh
normal   : 1,833 ÷ 26,250 = $0.06983/kWh
off_peak : 1,190 ÷ 26,250 = $0.04533/kWh     (excl. VAT — correct for a manufacturer)
```

## 3. Step 2 — the three breakeven COPs

```
off-peak : (0.04533 × 293.071)/7.0667 = 1.879 ≈ 1.88
normal   : (0.06983 × 293.071)/7.0667 = 2.895 ≈ 2.90
peak     : (0.12945 × 293.071)/7.0667 = 5.369 ≈ 5.37
```

| Period | $/kWh | h/yr | Breakeven COP |
|---|---|---|---|
| Off-peak (00:00–06:00) | 0.04533 | 2,190 | **1.88** |
| Normal | 0.06983 | 5,010 | **2.90** |
| Peak (Mon–Sat 17:30–22:30) | 0.12945 | 1,560 | **5.37** |

## 4. Step 3 — a real machine against it (COP 3.11)

- Off-peak: $4.27/MMBtu (−40% vs coal) → wins big.
- Normal: $6.58/MMBtu (−7%) → wins modestly.
- Peak: $12.20/MMBtu (+73%) → loses badly.

Blended rate ⇒ one breakeven ~3.3 ⇒ "marginal" — WRONG conclusion. Hour-by-hour:
win off-peak+normal (7,200 h/yr), store, ride through peak. **Design answer: heat pump +
thermal storage** = capstone hypothesis.

FX sensitivity note: 26,250 VND/USD and the 14-Aug-2026 Newcastle-based coal price are
time-stamped inputs; re-check vn_context.json before reusing in live work.

## Quiz (6 questions)

1. Why divide P_coal by η → **fuel→delivered-heat conversion ($7.07 bar)**.
2. 1,190 VND at 26,250 → **$0.04533/kWh**.
3. Peak breakeven → **~5.37**.
4. COP 3.11 off-peak heat cost → **≈$4.27/MMBtu (−40%)**.
5. Blended breakeven misleads because → **hides hour-to-hour spread; storage flips verdict**.
6. Coal to $6.50 → **breakevens FALL** (~4.38 peak); dearer coal lowers the COP bar.

## Primary source

`C:\Users\tukum\Downloads\ee-heat\tools\reopt\vn_context.json` (raw VND + FX + coal),
`C:\Users\tukum\Downloads\ee-heat\tools\README.md` §2 (published table reproduced);
https://reopt.nrel.gov/reopt-jl
