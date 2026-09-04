# 0014 · Graph Optimization Problems — notes

SE track · 6.0002 Lec.3 · week 3 · ~30 min

## What this lesson covers
- Constrained shortest path: loss + price + budget B.
- Greedy trap: A–B first step overspends (8>6), kills feasibility.
- Brute force enumerate+filter: optimal at exponential cost.
- DP on (node, spend): pseudo-polynomial V×B.
- Worked: B=6 → only A–C–D feasible, loss 10 (vs unconstrained 6).

## Why this lesson exists
Constrained sequel to 0009; knapsack greedy-vs-optimal moral on graphs.
Mission link: cheapest feeder upgrade under capex cap. Leads into PS2.

## Quiz answers
1. Limits on cost/visits constrain. 2. Local picks violate budget.
3. Brute force optimal, exponential. 4. Overlapping subproblems memoized.

## Try it
Recompute optimum at B=12 by hand; check whether greedy works now.
