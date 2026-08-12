# 0002 — Lazy evaluation cannot handle self-reference; tokenizers emit one step late

Week 1's hw1 (symbolic calculator) produced two genuinely surprising results, both worth locking in.

First, lazy (partial) evaluation breaks on a self-referential assignment: `(a = 5)` then
`(a = (a + 1))` stores `Sum(Var(a), Num(1.0))` under `a`, and asking for `a` re-enters `a`'s own
value — infinite recursion (observed directly as `RecursionError`). Eager evaluation rebinds `a` to
`6.0` and is fine. So "evaluate only when needed" is powerful for forward references but cannot
defer self-reference.

Second, the state-machine tokenizer outputs a token only when it sees the character that *ends* the
token, so the final token of an input is emitted one step late — which is exactly why a trailing
space must be appended before `transduce`. This "output lags one step because termination is signaled
by the next character" pattern is the same reason `Delay` emits its initial value first.

**Evidence:** `work/6.01SC/hw1/hw1Work.py` reproduces the handout's eager and lazy transcripts
exactly, including the `calcTest(lazyTestExprs)` chain ending at `24.0` and `14.0`; the
self-reference recursion was hit live during testing; `lib/sm.py` passes the plan's Delay/Accumulator
specs and `Cascade(Delay(0), Accumulator(0)).transduce([1,2,3]) == [0,1,3]`.

**Implications:** when the capstone composes controllers, avoid state-machine formulations that wire
a variable back into itself without a `Delay`; a feedback loop without a delay unit is the same
self-reference trap. Teach the "output lags termination by one step" idea explicitly when 6.002's
unit-sample response arrives in week 2 — it is the same phenomenon.
