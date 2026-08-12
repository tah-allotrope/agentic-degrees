# GLOSSARY — canonical language of this workspace

> Terms are used consistently in every lesson and reference. New terms are added as they
> appear; never redefine an existing one.

## Python
- **Binding**: the association of a name with an object in a namespace; `x = 5` binds `x` to
  the integer object `5`. Rebinding points the name at a different object.
- **Object**: everything in Python is an object — data + methods, with a type.
- **Scope**: the region where a name is visible. Function bodies get their own local scope;
  names bound there are not visible outside.
- **List**: ordered, *mutable* collection `[1, 2, 3]` — can append/assign.
- **Tuple**: ordered, *immutable* collection `(1, 2, 3)`.
- **Dictionary (dict)**: unordered *key → value* mapping `{"a": 1}`; lookup by key.
- **Comprehension**: compact collection-builder expression, e.g. `[x*2 for x in range(3)]`.
- **Iteration**: `for`/`while` loops; `range(a, b)` yields `a, a+1, ..., b-1`.

## 6.01SC / systems
- **State machine**: a model of a discrete system: states `S`, inputs `I`, outputs `O`,
  transition function `S×I → S`, output function `S → O` (or `S×I → O`); starts in
  `startState`.
- **State**: the memory of a system — everything needed to predict its future behavior from
  the current input alone.
- **Transition function**: maps (current state, input) → next state.
- **Output function**: maps (current state, input) → output.
- **LTI** (later): linear, time-invariant system — the backbone of signals & systems.
- **Signal** (later): a function of time; the unit of analysis in chapter 5.

## Study mechanics
- **Retrieval practice**: recalling from memory instead of re-reading; builds storage strength.
- **Spacing**: distributing practice over time; the opposite of cramming.
- **ZPD**: zone of proximal development — work that is challenging but achievable.
- **Learning record**: `learning-records/NNNN-name.md`; captures a non-obvious lesson learned,
  or a revision to what was previously recorded.
