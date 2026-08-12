# 6.01 HW1 — Symbolic Calculator: solution notes

Source: `mit-ocw-curriculum/electrical-engineering/01-intro-to-eecs-1-6.01SC/other/MIT6_01SCS11_hw1.pdf`
(handout) and `hw1.zip → hw1/hw1Work.py` (skeleton).

## What was built

A fully parenthesized symbolic calculator in the two phases the handout describes:

1. **Parse** (`tokenize` + `parse`) — character string → token list → syntax tree.
2. **Evaluate** (`.eval` lazy / `.eval_eager`) — syntax tree → value, with an
   environment (a Python `dict`) carrying variable bindings.

Classes: `Number`, `Variable`, and the `BinaryOp` family (`Sum`, `Prod`, `Quot`,
`Diff`, `Assign`). `BinaryOp` holds the shared `__init__`/`__str__`; each subclass
declares only its `opStr` and the operator. All numbers are stored as floats.

## Design decisions

- **Recursive-descent parser.** `parse(tokens)` nests a `parseExp(index)` that
  handles exactly the three grammar cases: a number, a variable, or
  `( expression op expression )`. It returns `(tree, nextIndex)` pairs so nested
  expressions are consumed without backtracking.
- **Two evaluators.** Eager `eval_eager` (Step 3) demands both children be
  numbers. Lazy `eval` (Step 7) partially evaluates: if both children resolve to
  numbers it computes, otherwise it rebuilds the operator node with the
  simplified children (`self.__class__(left_value, right_value)`).
- **`lib601` substitution (ASM-006).** The skeleton did `import lib601.sm as sm`.
  `lib601` is not in this repository, so `hw1Work.py` imports the workspace's own
  reimplementation at `work/6.01SC/lib/sm.py` (a `sys.path` shim resolves it).
  Nothing else from the skeleton's environment is missing.

## Verified behaviour (all match the handout transcripts)

- `tokenize` passes all 8 handout cases, including the unspaced
  `'(fred+george)'` and the `'**-)('` run of separators.
- `parse` reproduces `Sum(Var(fred), Var(george))`,
  `Quot(Prod(Var(a), Var(b)), Diff(Var(cee), Var(doh)))`, and
  `Assign(Var(a), Prod(Num(3.0), Num(5.0)))`.
- Eager `testEval` → `5.0, 2.0, 4.0, 7.0, 3.0, 7.0, {'a': 7.0, 'b': 2.0, 'c': 4.0}`.
- `calcTest(testExprs)` reproduces the handout transcript exactly (`(2 + 5) →
  7.0`; `(z = 6)` → `None, {'z': 6.0}`; `z` → `6.0`; `(w = (z + 1))` → `None`;
  `w` → `7.0`).
- Lazy `testLazyEval` → `Sum(Var(b), Var(c))`, `Sum(2.0, Var(c))`, `6.0`.
- `calcTest(lazyTestExprs)` reproduces the handout's partial-evaluation chain
  ending at `24.0` (and `14.0` after `(d = 2)`).

Run it: `python teach-workspace/work/6.01SC/hw1/hw1Work.py`.

## Extension chosen: tokenizer as a state machine

The handout offers two extensions (tokenizer-by-state-machine or lazy partial
evaluation). **Both were implemented**: lazy evaluation is the default `.eval`,
and the extension chosen for submission is the state-machine `Tokenizer`
(Steps 5–6), which ties directly into the Unit-1 `SM` abstraction.

`Tokenizer` is an `SM` whose state is the pending token string. Each input
character either extends the word (output `''`), or terminates it (output the
completed token). A separator or space *terminates and is itself held for the
next step*, which is why a trailing space must be appended to the input: the last
token has no terminating character of its own. `tokenizeBySM` runs the machine
with a trailing space and drops the empty outputs.

**Check Yourself 1.** *Why append a space?* The machine emits a token only when
it sees the character that ends it. The final token of the input has no following
character, so without the appended space it would stay stuck in the machine's
state and never be emitted.

**Check Yourself 1.** *Compare the two tokenizers.* The plain `tokenize` is a
direct scan: it builds the token list immediately and reads top-to-bottom. The
`Tokenizer` SM models the same process one step at a time, keeping the pending
word in its state and emitting one step late; it is composable (can be cascaded
with other machines) and demonstrates why state machines suit character-stream
processing. They produce identical token lists.

**Check Yourself 2.** *What happens with `(a = 5)`, `(a = (a + 1))`, `a`?*
Eager: `a` binds to `5.0`, then to `6.0`; `a` evaluates to `6.0`. Lazy: `(a = (a
+ 1))` stores the unevaluated tree `Sum(Var(a), Num(1.0))`, and evaluating `a`
re-enters `a`'s own value — infinite recursion. Lazy evaluation handles
forward references but not self-reference.
