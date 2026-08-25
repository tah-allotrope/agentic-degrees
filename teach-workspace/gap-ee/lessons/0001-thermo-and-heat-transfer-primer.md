# 0001 · Thermo & Heat-Transfer Primer

> gap-ee week 1, day 1 · 45-60 min. Companion markdown for terminal viewing; the canonical
> interactive version is `0001-thermo-and-heat-transfer-primer.html`.

Three ideas before any tool makes sense: how heat moves, why steam carries so much energy,
and the °C/bar(g)/kJ unit system.

## 1. Three ways heat moves

- **Conduction** — through solids: `Q = k·A·ΔT/L`. Boiler shells, pipe walls, insulation.
  Fibreglass k is ~20× lower than steel — that's why insulation works.
- **Convection** — moving fluid: `Q = h·A·ΔT`. Condensing steam on a jacket; forced beats
  natural convection 5–10× on `h`.
- **Radiation** — no medium, scales with T⁴. Matters for bare surfaces at 100°C+.

Plant work uses tools that solve these; your job is recognising which mechanism a measure
targets (insulation → conduction+radiation; excess-air control → stack losses).

## 2. Sensible vs. latent heat

- Sensible heat changes temperature; latent heat changes phase at constant temperature.
- Water: c_p ≈ 4.186 kJ/kg·°C, h_fg(100°C) ≈ 2257 kJ/kg.

Worked example — 1000 kg water, 20°C → 100°C, then vaporised:

```
Sensible:  1000 kg × 4.186 kJ/kg·°C × 80°C = 334,880 kJ
Latent:    1000 kg × 2257 kJ/kg            = 2,257,000 kJ
Ratio:     2,257,000 / 334,880 ≈ 6.7×
```

Vaporising costs **~6.7× more** than heating to boiling. This one ratio explains:

1. Why steam transports industrial heat — 2257 kJ per kg delivered at constant temperature.
2. Why condensate return tops the savings list (lesson 0003).
3. Why dryers/stenters are hungry (latent duty all day).
4. Why a 60–95°C dye-house loop is the cheap, low-lift target for a heat pump.

## 3. Units: °C / bar(g) / kJ

VN plant data arrives in tonnes steam/h, bar(g), °C, kJ → MEASUR's first setting is
**"Set units to Metric"** (`ee-heat/tools/measur/VN-settings-card.md`), because hand-unit
conversion is where transcription errors get made.

- bar(g) = gauge; 10 bar(g) ≈ 11 bar abs ≈ 184°C saturation.
- **1 MMBtu = 293.071 kWh** (used in every later lesson); 1 GJ = 0.9478 MMBtu.
- Consistency check across tools: $5.30/MMBtu ÷ 1.055 GJ/MMBtu ≈ $5.02/GJ — same coal price,
  two dialects.

## Quiz (6 questions)

1. Insulation primarily attacks… → **conduction + surface radiation** (not internal steam
   convection).
2. Latent cost for the worked example → **~6.7× more** (2,257,000 kJ vs 334,880 kJ).
3. Condensing steam transfers latent heat at → **constant temperature** until fully condensed.
4. Why Metric first → **plant data arrives metric; avoids transcription errors**, not precision.
5. $5.30/MMBtu vs $5.02/GJ → **consistent** ($5.30 ÷ 1.055 ≈ $5.02).
6. Dye-house loop beats steam header for a heat pump → **smaller temperature lift ⇒ higher
   achievable COP**.

## Primary source

U.S. DOE AMO/ITP, *Improving Steam System Performance: A Sourcebook for Industry*, 2nd ed. —
https://www.energy.gov/sites/prod/files/2014/05/f15/steamsourcebook.pdf (free PDF, §1 basics).
Local companion: `C:\Users\tukum\Downloads\ee-heat\tools\measur\VN-settings-card.md`.
