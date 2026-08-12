# 0005 · Greedy vs. Optimal Knapsack

*SE track · 6.0002 Lec.1 · ~25 min · [mission](../MISSION.md)*

**Why this matters:** sizing a BESS ("how many MWh fit in this budget to capture the most
revenue?") is a knapsack with a dollars constraint and a revenue objective. You need the *language*
of this lesson to argue why a spreadsheet's greedy pick may not be the best pick — and when the
exact answer is worth the exponential cost.

## 1 · What an optimization problem is

Two ingredients: an **objective function** to maximize or minimize (revenue, trip time, value) and
a **set of constraints** (budget, weight limit, deadline). Knapsack: given items with value and
cost, pick a subset within a cost limit maximizing total value.

## 2 · Greedy: pick the "best" next item

```python
def greedy(items, maxCost, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalCost = 0.0, 0.0
    for item in itemsCopy:
        if totalCost + item.getCost() <= maxCost:
            result.append(item)
            totalCost += item.getCost()
            totalValue += item.getValue()
    return (result, totalValue)
```

Sort by a key, then take whatever fits. The key changes the answer: with a 1000-calorie limit and
the lecture's menu — by **value** → 424.0, by **cost** → 413.0, by **density** → 413.0. Greedy-by-
value wins on *this* menu, but that is coincidence.

## 3 · Why greedy can miss the optimum

Greedy commits; it never changes its mind. Counterexample — capacity 10: one item worth 100 at
cost 9, two items worth 60 at cost 5 each. Greedy by value takes the 100 → 100 total; the optimum
is both 60s → 120. Greedy is fast (O(n log n)) and usually good, but *never guaranteed optimal*.

## 4 · Optimal: exhaustive enumeration

The only guarantee: consider every subset (2^n), keep those within the limit, return the best
value. Exponential — only for small n, which is exactly why PS1 (cow transport) asks for both and
compares.

> **The lesson to internalize:** "greedy" and "optimal" are different words. A greedy answer is a
> *claim about effort*; an optimal answer is a *claim about correctness*. Say which one you produced.

## Quiz

1. **What does an optimization problem consist of?**
   a. **Objective plus constraints** · b. Inputs plus outputs · c. Loops plus variables · d. Classes plus methods
2. **Greedy by value selects items in what order?**
   a. **Highest value first** · b. Lowest cost first · c. Random order first · d. Alphabetical order first
3. **Why can greedy miss the optimum?**
   a. **It never backtracks** · b. It always backtracks · c. It picks randomly · d. It sorts descending
4. **What guarantees the optimal knapsack?**
   a. **Exhaustive enumeration** · b. Greedy selection · c. Sorting items · d. Random sampling

Answers in bold. Misses → re-read §2-3.

**Primary source:** 6.0002 Lecture 1 deck
(`.../02-computation-data-science-6.0002/other/MIT6_0002F16_lec1.pdf`); runnable code in
`Lecture1.zip → lecture1.py`; video: youtube.com/watch?v=C1lhuz6pZC0. Then answer the Lecture 1
questions in `teach-workspace/work/6.0002/lecture1-answers.md`.

**Try:** run `lecture1.py` and convince yourself why each strategy differs — bring confusion to
the agent.
