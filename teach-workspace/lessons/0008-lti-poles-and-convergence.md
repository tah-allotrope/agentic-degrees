# 0008 · LTI Systems, Poles and Convergence — notes

EE track · 6.01SC Ch.5 §5.4–5.5 · week 2 · ~30 min

## What this lesson covers
- System function H(R)=Y/X as rational function; feedback creates denominator.
- Compositions as algebra: sum adds, cascade multiplies, feedback → Black's formula.
- Poles as bases of geometric modes in unit-sample response.
- Convergence: |p|<1 decays, |p|>1 diverges; dominant pole; complex → ringing.
- Worked numbers: 0.9ⁿ vs 1.1ⁿ, dominant-pole ratio at n=10.

## Why this lesson exists
Bridge from notation (0007) to analysis: reading H to predict behavior without simulation.
Mission link: BESS/ECS feedback stability is a pole-location question.

## Quiz answers
1. Feedback puts polynomial in denominator. 2. H=1/(1−0.9R) → 0.9ⁿ. 3. |p|<1 decays. 4. 0.9 dominates 0.7.
