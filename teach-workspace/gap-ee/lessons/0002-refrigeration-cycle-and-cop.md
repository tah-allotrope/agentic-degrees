# 0002 · Refrigeration Cycle & COP

> gap-ee week 1, days 1-2 · 45-60 min. Companion markdown; canonical interactive version is
> `0002-refrigeration-cycle-and-cop.html`.

## 1. The four stages (vapor-compression cycle)

1. **Evaporator** — refrigerant boils below source temp, absorbs heat from the 45°C
   wastewater.
2. **Compressor** — electrical work raises pressure/saturation temperature. The only place
   work enters (the electricity bill lives here).
3. **Condenser** — vapour condenses, delivering latent heat to the 95°C sink loop.
4. **Expansion valve** — pressure drop, flash cooling, repeat.

Refrigerant = energy taxi; R1234ze(Z) fits a ~95°C sink without extreme pressures.

## 2. COP defined

```
COP = Q_heat_delivered / W_electrical_input
```

- Resistance heater: COP = 1.0 exactly — that's the floor, not the benchmark.
- COP 3.11 → each kWh buys 3.11 kWh heat; 2.11 kWh lifted free from the waste stream.
- Not "311% efficient" — heat is *moved*, not created (first law intact).

## 3. Ideal vs actual

```
COP_ideal  = T_sink / (T_sink − T_source)      [Kelvin]
COP_actual = η_II × COP_ideal                  [η_II = second-law efficiency]
```

Worked example — dye-house case (45°C → 95°C):

```
T_source = 318.15 K, T_sink = 368.15 K
Pure Carnot: 368.15 / 50 = 7.36
Tool's ideal (real refrigerant + approach temps): 6.22
Actual at η_II = 0.50: 0.5 × 6.22 = 3.11   ← corroborated finding (ee-heat/tools/README.md)
```

Instincts: smaller lift ⇒ much higher COP (halve lift ≈ double ideal COP); vendors run
~40–60% second-law efficiency and that spread can decide whether breakeven is cleared.

## Quiz (6 questions)

1. Absorbs heat from source → **evaporator**.
2. COP definition → **heat delivered / electrical work input**.
3. Resistance heater COP → **exactly 1.0**.
4. 0.5 × 6.22 → **3.11** (the capstone's ASHPWaterHeater cop).
5. Colder source / bigger lift → **ideal COP decreases**.
6. Why not "311% efficient" → **heat moved, not created**; second law lives in η_II.

## Primary sources

- LibreTexts Eng. Thermodynamics §6.03 Refrigerator & heat pump:
  https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Introduction_to_Engineering_Thermodynamics_(Yan)/06%3A_Entropy_and_the_Second_Law_of_Thermodynamics/6.03%3A_Refrigerator_and_heat_pump
- BCcampus Thermo §6.4 Carnot cycles: https://pressbooks.bccampus.ca/thermo1/chapter/6-4-carnot-cycles/
- Finding to verify: `C:\Users\tukum\Downloads\ee-heat\tools\README.md` §3.
