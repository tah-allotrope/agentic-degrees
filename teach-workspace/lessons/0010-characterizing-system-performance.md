# 0010 · Characterizing System Performance — notes

EE track · 6.01SC Ch.5 · week 3 · ~30 min

## What this lesson covers
- Step-response landmarks: rise time (10→90%), overshoot (%), settling (±5% band).
- Steady-state error for unit step.
- Dominant-pole settling estimate n ≈ ln(0.05)/ln|p| (p=0.8 → ~14 steps).
- Worked comparison: fast-ringing tuning A settles later than slow-clean B.
- Moral: report all three metrics; any single one misleads.

## Why this lesson exists
Gives acceptance criteria for controllers before designing one (0011).
Mission link: BESS controller spec — speed vs overvoltage-trip overshoot.

## Quiz answers
1. Rise time = response climb interval. 2. Overshoot = peak excess over final.
3. Settling = last entry into error band. 4. Trio needed; speed/ringing/precision conflict.

## Try it
Compute y[3], y[14] for y[n]=1−0.8ⁿ; state rise vs settling.
