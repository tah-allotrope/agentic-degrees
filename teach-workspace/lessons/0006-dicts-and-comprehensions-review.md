# 0006 · Dicts & Comprehensions Review

SE-track week-1 open item · diagnostic re-sit prep · 10-15 minutes · recall first, then check ·
[mission](../MISSION.md)

Week 1 has exactly one open checklist item: the Python diagnostic re-sit — a clean 7/8+ after the
primer is the entry ticket to 6.0002. The cold run scored 8/10 (record 0001) and the two misses
were dictionaries and list comprehensions. This lesson re-teaches exactly those two topics with
worked numeric examples, then gives you a fresh practice quiz at diagnostic difficulty before you
re-sit [0002 the diagnostic](0002-python-diagnostic.html).

**Mission link.** A battery controller's operating state is a dict — asset name → power — and the
two operations you missed are the two you use most: lookup-and-update (`d[k] = v`) and size
(`len(d)`). Comprehensions are how 6.0002 builds model inputs from raw data in one line instead of
a six-line loop.

## 1. Dictionaries: the two operations you missed

A dict maps keys to values. `d[k]` reads, `d[k] = v` writes — and the write is how you *both* add
a new pair and update an existing one. `len(d)` counts key-value pairs, not values. That is the
exact miss from the cold run:

```python
d = {'a': 1}
d['b'] = 2
len(d)               # 2 — two pairs now, not the value 2
d['a'] = 5           # update in place: still 2 pairs
len(d)               # 2 — assignment to an existing key never grows the dict
```

Three rules that cover the whole diagnostic:

- `d[k]` raises `KeyError` when `k` is absent; use `d.get(k, default)` to get a fallback instead.
- `k in d` tests key membership (fast — hashed, not a scan).
- Iterating a dict yields keys by default; use `d.items()` to unpack key and value together.

```python
plant = {'pv': 5, 'grid': 10}        # kW available
plant['bess'] = 4                    # add a pair
plant['grid'] = 8                    # update a pair
len(plant)                           # 3
plant.get('wind', 0)                 # 0 — no KeyError
for name, kw in plant.items():
    print(name, kw)                  # pv 5 / grid 8 / bess 4
```

## 2. Comprehensions: read them left-to-right as a sentence

A list comprehension is one expression that builds a whole list: `[expr for var in iterable]`.
Read it as "for each var in iterable, produce expr". The second diagnostic miss was
`[x * 2 for x in range(3)]` — unfold it by hand: `range(3)` yields 0, 1, 2; doubling gives
0, 2, 4:

```python
[x * 2 for x in range(3)]          # [0, 2, 4]
[x ** 2 for x in range(4)]          # [0, 1, 4, 9]
[len(s) for s in ['pv', 'bess', 'grid']]   # [2, 4, 4]
```

Add `if cond` after the loop to filter — "for each var, if cond, produce expr":

```python
[x for x in range(6) if x % 2 == 1]    # [1, 3, 5] — odds only
[x * 10 for x in range(4) if x != 0]   # [10, 20, 30]
```

The same shape builds dicts with `{key: value for ...}` — the one-line way to make a lookup
table, which is what 6.0002's problem sets reach for:

```python
{k: k * k for k in range(3)}        # {0: 0, 1: 1, 2: 4}
```

## 3. Re-sit protocol

1. If anything above felt thin, re-read primer 0001 §2 ("Lists, dicts, and mutation") and §3
   ("Comprehensions") — [0001 the primer](0001-python-essentials-primer.html).
2. Open [0002 the diagnostic](0002-python-diagnostic.html) and answer all 8 questions from
   memory — no notes, no running code.
3. Score 7/8 or better → the week-1 checkbox closes; the agent finalizes learning record 0001 and
   ticks the PROGRESS.md item. Score 6/8 or below → repeat the primer, then re-sit once more.
4. Either way, record the score and date in learning record 0001 (it is still marked
   "provisional").

## Practice quiz (same difficulty, different questions)

1. After `d = {'a': 1}` then `d['b'] = 2`, what does `len(d)` return?
   a. 1  b. 3  c. **2**  d. 4
   — `d['b'] = 2` adds one pair; len counts pairs, never values → 2.

2. With `d = {'x': 10}`, what does `d.get('y', 0)` return?
   a. 10  b. **0**  c. Error  d. None
   — `get` returns the fallback when the key is absent → 0 (bracket lookup would KeyError).

3. After `d = {'k': 1}` then `d['k'] = 2`, what does `d['k']` return?
   a. One  b. Error  c. None  d. **Two**
   — assignment to an existing key updates it → 2; len unchanged.

4. What does `for k, v in d.items(): print(k, v)` on `{'a': 1, 'b': 2}` print?
   a. **a 1 b 2**  b. a b 1 2  c. 1 a 2 b  d. a 1 b 1
   — items() yields (key, value) pairs; unpacked k, v prints key then value.

5. What does `[x ** 2 for x in range(4)]` evaluate to?
   a. [1, 4, 9, 16]  b. [0, 1, 2, 3]  c. [0, 4, 16, 36]  d. **[0, 1, 4, 9]**
   — range(4) = 0,1,2,3; squares = 0,1,4,9.

6. What does `[x for x in range(6) if x % 2 == 1]` evaluate to?
   a. **[1, 3, 5]**  b. [0, 2, 4]  c. [1, 2, 3]  d. [0, 1, 3]
   — filter keeps odd values 1,3,5.

7. What does `[len(w) for w in ['go', 'bess', 'grid']]` evaluate to?
   a. [1, 3, 3]  b. [2, 3, 4]  c. **[2, 4, 4]**  d. [4, 4, 2]
   — lengths in input order: 2, 4, 4.

8. What does `{k: k * k for k in range(3)}` evaluate to?
   a. {0: 0, 1: 1, 2: 2}  b. **{0: 0, 1: 1, 2: 4}**  c. {0: 1, 1: 2, 2: 4}  d. {1: 0, 2: 1, 4: 2}
   — keys 0,1,2 map to squares 0,1,4.

**Primary source:** MIT 6.01SC Ch.2 "Learning to Program in Python" —
`mit-ocw-curriculum/electrical-engineering/01-intro-to-eecs-1-6.01SC/other/MIT6_01SCS11_chap02.pdf`.
Dictionaries and comprehensions: 6.0001 Lecture 6, "Recursion and Dictionaries"
(https://www.youtube.com/watch?v=WPSeyjX1-4s, 6.0001 playlist).

Scored 7/8 or better? Tell the agent — it closes the week-1 checkbox, finalizes record 0001, and
updates PROGRESS.md. Missed any? Ask it to re-teach that item before you sit 0002.
