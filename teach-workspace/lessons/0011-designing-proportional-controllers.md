# 0011 · Designing Proportional Controllers — notes

EE track · 6.01SC Ch.5 · week 3 · ~30 min

## What this lesson covers
- Control law u = K·e; closed loop y/r = PK/(1+PK).
- Stability: pole (1−K), |1−K|<1 ⟺ 0<K<2; K=1 deadbeat.
- Steady-state error 1/(1+PK); finite gain leaves residue.
- Worked: K=0.5 monotonic err 0.667 vs K=1.5 ringing err 0.400.
- Tuning protocol: raise K to overshoot limit, keep margin, accept residue.

## Why this lesson exists
First controller design + review skill; 0010 specs judge it.
Mission link: BESS charge loop starts as P-control.

## Quiz answers
1. Command = gain × error. 2. Stable when gain magnitude below one.
3. Higher gain cuts error, risks ringing. 4. Drive vanishes at zero error.

## Try it
P=1, r=1, K=1: y[∞], error, first three outputs.
