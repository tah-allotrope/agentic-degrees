# 0009 · Graph Models and Shortest Paths — notes

SE track · 6.0002 Lec.2–3 · week 2 · ~30 min

## What this lesson covers
- Graph model G=(V,E): directed/undirected, weighted/unweighted, path cost as sum.
- Representations: adjacency list (dict of neighbor lists) vs matrix; sparse vs dense.
- BFS for uniform-cost shortest path (O(V+E), queue, visited).
- Dijkstra for weighted non-negative (dist dict, relaxation, O((V+E) log V)).
- Worked feeder example: A–B–D (cost 8) beats A–C–D (cost 15) — BFS can mis-pick.

## Why this lesson exists
Graph model is the reusable SE abstraction for routing, networks, grids — directly maps to feeders/substations.
Week-1 dict skills are the implementation (adjacency list = dict of lists).

## Quiz answers
1. Weighted = number on each edge. 2. Dict node→neighbor list. 3. BFS needs equal cost. 4. Relaxation updates dist[v] if via u cheaper.
