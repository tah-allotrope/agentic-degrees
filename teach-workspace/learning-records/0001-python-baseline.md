# 0001 — Python baseline established

**Status:** provisional — re-sit the diagnostic in lesson `0002-python-diagnostic` at week 0 and
update this record if the score changes.

The Phase-0 diagnostic (lesson `0002-python-diagnostic`) was taken cold during the scaffold:
**8 / 10**. The two missed questions were on dict operations (`len(d)` after adding a key) and on
list comprehension output (`[x * 2 for x in range(3)]`). Functions, scope, aliasing, iteration,
tuple unpacking, recursion, and the style rules were solid.

**Evidence:** diagnostic `section.quiz` results for lesson 0002; missed items were on dicts and on
comprehensions.

**Implications:** the software track cannot assume dicts or comprehensions are fluent. The rule for
6.0002 lessons is that dict and comprehension refreshers are embedded inside the first 6.0002 lesson
that needs them — concretely, the PS1 lesson (`greedy-vs-optimal-knapsack`) re-teaches dict iteration
and comprehension syntax before they are required, rather than assuming them.
