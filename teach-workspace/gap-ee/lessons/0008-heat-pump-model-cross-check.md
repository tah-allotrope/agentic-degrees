# 0008 · heat_pump_model Cross-Check

> gap-ee week 2, day 8 · 60-90 min hands-on. Companion markdown; canonical version is
> `0008-heat-pump-model-cross-check.html`.

## 1. Regenerate inputs, prove zero-diff

```
cd C:\Users\tukum\Downloads\ee-heat\tools\heat-pump-model
C:\Users\tukum\Downloads\ee-heat\tools\.venv\Scripts\python.exe make_vn_inputs.py
git -C C:\Users\tukum\Downloads\ee-heat status --short    # must show NO tracked changes
```

Diff ⇒ stop and investigate. Never commit inside ee-heat.

## 2. Run the dye-house case

```
..\.venv\Scripts\python.exe -m jupyterlab     → open test_heat_pump.ipynb
```

Case: source 45°C (dye-house wastewater) → sink 95°C, R1234ze(Z), η_II = 0.50.
Expected: ideal COP ≈ 6.22 (real-refrigerant cycle; pure Carnot ~7.36), actual
6.22 × 0.50 = **3.11** — third independent production of this number (0002 hand calc,
0007 tariff drop, now the tool).

Tariff drop: $4.27/MMBtu off-peak (−40%) · $6.58 normal (−7%) · $12.20 peak (+73%).
Same conclusion as REopt from physics instead of optimization: HP + thermal storage.

## 3. Cost side = radioactive

- Negative capital cost; garbled operating-cost units.
- LCOH $2.24/MMBtu < energy floor ($6.58 at COP 3.11) — impossible by construction.
- Stale (Nov 2022), no README, no licence.

Rule: **"Use this model for COP, take costs from REopt."** Rank-3 "reference only," empirically
confirmed.

## Quiz (6 questions)

1. git after generator → **no tracked changes; investigate any diff; never commit in ee-heat**.
2. Why COP trustworthy / cost not → **CoolProp physics vs stale cost module**.
3. Actual COP → **3.11** (0.5 × 6.22).
4. Sub-floor LCOH → **wrong by construction; total cost can't be below energy cost alone**.
5. Why 45→95°C → **plant's real dye-house opportunity in priority band (ii)**.
6. Into capstone goes → **only COP 3.11 as ASHPWaterHeater cop; economics stay REopt's**.

## Primary source

NLR `heat_pump_model` clone (`C:\Users\tukum\Downloads\ee-heat\tools\heat-pump-model\`,
`test_heat_pump.ipynb`) + `make_vn_inputs.py`; caveats in `ee-heat/tools/README.md` §3.
