# 6.01 swLab01 — Software Lab 1: fib and V2: solution notes

Source: `mit-ocw-curriculum/electrical-engineering/01-intro-to-eecs-1-6.01SC/other/swLab01.zip →
swLab01/swLab01Work.py` (skeleton).

## What was built

Two pieces, per the skeleton:

1. `fib(n)` — the nth Fibonacci number, written recursively (the point of the lab
   is recursion).
2. `class V2` — a two-dimensional vector with the arithmetic a 6.01 model needs.

## Convention notes (the swLab01 handout is not in the download)

- **Fibonacci base.** The handout is not bundled, so `fib` uses the standard
  convention `fib(0) = 0`, `fib(1) = 1`. If the original lab used the
  rabbit-breeding convention (`fib(0) = 1`, `fib(1) = 1`), change only the two
  base-case returns; the recursion is unchanged.
- **V2 operations.** Implemented to the operations 6.01 vectors need:
  `__init__(x, y)`, `__str__`, `__add__`, `__sub__`, `__mul__` (dot product when
  the other operand is a `V2`, scalar multiplication otherwise), `__rmul__`
  (so `3 * v` works), `norm()` (Euclidean magnitude), and `__eq__` for value
  equality (so vectors compare by components, not identity).

## Why this lab matters

`V2` is the building block for the 6.01 robot and navigation models (positions,
velocities, heading errors). `fib` is the canonical warm-up for the recursive
reasoning the state-machine and search units then lean on.

## Verified behaviour

```
fib: 0..8 -> [0, 1, 1, 2, 3, 5, 8, 13, 21]
a = V2(3, 4);  b = V2(1, 2)
a + b  -> V2(4, 6)      a - b -> V2(2, 2)
a * b  -> 11 (dot)      3 * a -> V2(9, 12)   a * 3 -> V2(9, 12)
a.norm() -> 5.0
```

Run it: `python teach-workspace/work/6.01SC/swLab01/swLab01Work.py`.
