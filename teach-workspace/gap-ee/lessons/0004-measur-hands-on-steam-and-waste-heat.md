# 0004 · MEASUR Hands-On: Steam & Waste Heat

> gap-ee week 1, days 3-4 · 90-120 min hands-on (GUI). Companion markdown; canonical version
> is `0004-measur-hands-on-steam-and-waste-heat.html`.

MEASUR v1.8.3 = Windows GUI, no CLI, no scriptable settings (local DB). All values come from
`C:\Users\tukum\Downloads\ee-heat\tools\measur\VN-settings-card.md` — the card wins on any
disagreement; fresh user profile ⇒ re-enter everything by hand.

## Part A — Localization checklist

- [ ] Units → **Metric** (Settings → Default Settings)
- [ ] Electricity excl. VAT: normal **$0.06983/kWh**, off-peak **$0.04533/kWh**,
      peak **$0.12945/kWh**; use normal for a general sweep (one rate per assessment)
- [ ] Boiler fuel: closest solid fuel, overridden to **$5.02/GJ** (= $5.30/MMBtu)
- [ ] Emission factors: grid **0.1831 kg CO₂/MJ**, coal **92.1 kg CO₂/GJ**
- [ ] Sanity: $5.02/GJ × 1.055 ≈ $5.30/MMBtu ✓

If the module won't accept the solid-fuel workaround cleanly, say so explicitly and point at
the card's "Fuel type" section — never silently pick another value.

## Part B — Steam System Modeler (garment defaults)

Header ≤10 bar(g) · dye-house/HTHW 60–95°C · wash 40–60°C · dryers 80–120°C · boiler η 75% ·
16 h/day 5–6 d/wk.

Walk lesson 0003's order (condensate return → blowdown → flash → excess air), read delivered-
heat cost after each. Run load-*shifting* measures twice: off-peak AND peak rates (2.86× spread
changes the winner). Record baseline vs optimized load — that delta is the load-reduction layer.

## Part C — Waste Heat Recovery module

Point at stack-gas + blowdown streams from Part B's baseline; cross-check against Checks 2–4
savings. Wild disagreement ⇒ re-check entered settings first.

## Quiz (6 questions)

1. Run shifting measures twice → **2.86× spread changes which measure wins**.
2. Steam System Modeler computes → **energy/mass balance of header system + cost of measures**
   (not optimization — that's REopt).
3. US grid factor left in → **abatement overstated ~40% on every electrification measure**.
4. Coal not in list → **closest solid fuel + override BOTH price and EF**.
5. Feeds REopt → **post-optimization thermal load profile = ProcessHeatLoad input**.
6. Fresh Windows profile → **re-enter localization by hand from the card** (local per-user DB).

## Primary source

ORNL/DOE MEASUR v1.8.3 application itself + `ee-heat/tools/measur/VN-settings-card.md`;
methodology background: DOE AMO Steam Sourcebook
(https://www.energy.gov/sites/prod/files/2014/05/f15/steamsourcebook.pdf).
