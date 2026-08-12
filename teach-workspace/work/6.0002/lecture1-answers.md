# 6.0002 Lecture 1 — Optimization and the Knapsack Problem: answers

Source: `MIT6_0002F16_lec1.pdf` (deck) and `Lecture1.zip → lecture1.py`.

> The shipped `Lecture 1 Questions.txt` contains only three Google Form links
> (`goo.gl/forms/...`) that no longer resolve, so the in-lecture questions were
> reconstructed from the deck and `lecture1.py` and answered here. The three
> questions the deck poses are the classic knapsack checks.

## Question 1 — Run the greedy menu allocations and compare

The shipped `lecture1.py` builds a menu of 8 foods (note: `names` has 9 entries
but `values`/`calories` have 8, so `buildMenu` over `range(len(values))` drops
`'cake'`). Allocating a 1000-calorie knapsack by the three greedy key functions:

| Strategy | Total value | Items taken |
|---|---|---|
| Greedy by value | **424.0** | burger, pizza, beer, wine, apple |
| Greedy by cost | **413.0** | apple, wine, cola, beer, donut, pizza |
| Greedy by density | **413.0** | wine, beer, cola, apple, pizza, donut |

The three strategies pick different item sets and achieve different totals, so
the choice of `keyFunction` materially changes the answer. Greedy-by-value wins
on this menu, but that is coincidence, not a guarantee.

## Question 2 — Why is greedy not guaranteed optimal?

Greedy picks items in a fixed priority order and takes an item whenever it fits,
never revisiting a decision. That is locally greedy: it can lock out a high-value
combination. Clean counterexample: capacity 10, one item worth 100 at cost 9, and
two items worth 60 at cost 5 each. Greedy-by-value takes the 100 (9 used, 1 left)
and is stuck at 100; the optimum is both 60s for 120. The only way to *guarantee*
the optimum is exhaustive search over all combinations (brute force / dynamic
programming), which is exponentially expensive — that trade-off is the point of
the lecture and of Problem Set 1's cow-transport problem.

## Question 3 — What would brute force find here?

Exhaustive search over the 8-food menu would consider all `2^8 = 256` subsets,
keep those within 1000 calories, and return the maximum-value one — guaranteed at
or above the best greedy result (which, on this data, is 424.0). The cost is
obvious: exhaustive enumeration grows as `2^n`, which is why PS1 pairs a greedy
solution with a brute-force check.

## Takeaway

Greedy is fast (`O(n log n)` from the sort) and usually good, never optimal.
When the answer must be exact, enumerate — and accept exponential cost. This is
the exact structure the week-2/3 graph and 6.0002 problem sets build on.
