# 0007 · Signals & Systems, Difference Equations

*EE track · 6.01SC Ch.5 (§5.1–5.3) · ~30 min · [mission](../MISSION.md)*

**Why this matters:** a grid inverter, a battery charge controller, a motor turning a head — all are
described by one line like `y[n] = 0.5·y[n−1] + x[n]`. Reading that line and translating it to a block
diagram and back is exactly how you reason about a BESS controller without building it.

## 1 · Signals, systems, sampling

- **Signal** = function of a discrete index `n`: capital `X` = whole signal, lowercase `x[n]` = sample.
- **System** transduces input signal `X` into output signal `Y` (both infinite sequences).
- **Sampling**: `x[n] = x(nT)`; `T` = time between samples.

## 2 · Primitive signal + three operations

- **Unit sample** `δ[n]` = 1 at `n=0`, else 0.
- **Scale** `c·X`, **Delay** `R X` (= `x[n−1]`), **Add** `X1 + X2`.
- Compose: `3Δ + 4RΔ − 2R²Δ` has values `[3, 4, −2]` at steps `0,1,2`.

## 3 · Operator equation ↔ difference equation

- Operator equation relates whole signals: `Y = X − RX = (1 − R)X`.
- Difference equation relates samples, holds for every `n`: `y[n] = x[n] − x[n−1]`.
- Unit-sample response: `y[0]=1, y[1]=−1, y[2]=0, …`.

## 4 · Block diagram ↔ state machine

- Primitives: **delay** (rectangle), **gain** (triangle, number), **adder** (circle, `+`).
- `Y = X − RX` as an SM — state = previous input:

```python
class Diff(SM):
    def start_state(self): return 0          # x[-1]
    def get_next_values(self, state, inp):
        return (inp, inp - state)
```

All four representations describe the same system.

## 5 · Feedforward = polynomial algebra

- Feedforward: `Y = ΦX`, `Φ` a polynomial in `R` (no dependence on its own past).
- **Cascade = multiply** (`Φ2·Φ1`); **Parallel = add** (`Φ1 + Φ2`); distributive law holds.
- **Transient in → transient out.** Persistent behaviour needs feedback (next lesson).

## Quiz

1. **Capital X denotes?** a. **entire signal sequence** · b. single input sample · c. delay operator · d. sampling period
2. **Shifts a signal later in time?** a. **delay by one sample** · b. scale by a constant · c. add two signals · d. advance by one sample
3. **A feedforward system is always?** a. **a polynomial in R** · b. ratio of polynomials · c. geometric series · d. scalar constant
4. **Transient input into feedforward system?** a. **transient output** · b. persistent output · c. alternating output · d. constant output

Answers in bold. Misses → re-read §2–3, §5.

**Primary source:** 6.01SC Ch.5 (§5.1–5.3) `.../01-intro-to-eecs-1-6.01SC/other/MIT6_01SCS11_chap05.pdf`;
Unit 2 videos in the 6.01SC YouTube playlist. Then the
[reference card](../reference/difference-equations-and-poles.html) and `hw2.pdf` problems 1–9.

**Try:** translate `Y = 2X − 0.5·R·Y` into a difference equation and block diagram — check with the agent.
