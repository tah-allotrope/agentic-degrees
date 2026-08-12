# 0004 · Object-Oriented Models for Engineering

*EE track · 6.01SC Ch.3 §3.8 · ~25 min · [mission](../MISSION.md)*

**Why this matters:** a BESS sizing tool is an object model — a `Cell` knows its chemistry,
capacity, and internal resistance; a `BatteryPack` composes cells; a `Feeder` aggregates loads.
"The `Cell` object exposes `get_state_of_charge()`" is how these systems are described. The state
machine (0003) says *how* a controller behaves; the object model says *how you represent* the thing
being controlled.

## 1 · The idea: data plus the procedures that use it

Plain data and the functions that work on it drift apart as a program grows. OOP groups them: a
**class** is the template, an **instance** is a concrete object built from it, and **attributes**
(`self.dim`) hold the instance's own data — the "abstraction" of the PCAP framework: callers use
the object without seeing its guts.

## 2 · The Python shape: `__init__`, `self`, methods

```python
class Square:
    def __init__(self, initialDim):
        self.dim = initialDim
    def getArea(self):
        return self.dim * self.dim
    def setArea(self, area):
        self.dim = area ** 0.5
    def __str__(self):
        return "Square of dim " + str(self.dim)

s = Square(6)
s.getArea()        # 36
Square.getArea(s)  # 36 — s is just the first argument
s.setArea(100)
s.dim              # 10.0
print(s)           # "Square of dim 10.0"
```

Debugging notes: `__init__` runs at construction; every method takes `self` first (forgetting it
gives the "add is not defined" error); `__str__` makes objects print nicely — *the* debugging aid.

## 3 · Inheritance: override the parts that differ

```python
class Account:
    def __init__(self, initialBalance):
        self.currentBalance = initialBalance
    def balance(self):
        return self.currentBalance
    def deposit(self, amount):
        self.currentBalance = self.currentBalance + amount
    def creditLimit(self):
        return min(self.currentBalance * 0.5, 10000000)

class PremierAccount(Account):
    def creditLimit(self):
        return min(self.currentBalance * 1.5, 10000000)

b = PremierAccount(1000)
b.creditLimit()  # 1500.0
b.deposit(500)   # inherited — works without redefinition
b.balance()      # 1500.0
```

Each instance knows its own class, so `creditLimit()` dispatches to the right implementation with
no `if` anywhere — **polymorphism**. A grid model holds a mixed list of objects and asks each for
its behavior.

## 4 · Composition: objects inside objects

An object whose attributes are other objects is a **compositional data type** — a pack contains
cells, a feeder contains loads. Same idea as HW1's syntax trees; the backbone of every sizing and
simulation model.

## Quiz

1. **What does a class group together?**
   a. **Data and its procedures** · b. Files and their names · c. Inputs and their types · d. Loops and their counts
2. **Which keyword names the instance inside a method?**
   a. **self** · b. class · c. this · d. init
3. **What does `s.getArea()` pass as the first argument?**
   a. **The instance s** · b. The class type · c. The area value · d. The module name
4. **What does a subclass inherit?**
   a. **All parent methods** · b. Only new methods · c. The local scope · d. The module state

Answers in bold. Misses → re-read §2-3.

**Primary source:** 6.01SC Ch.3 §3.8 "Object-Oriented Programming Examples"
(`.../01-intro-to-eecs-1-6.01SC/other/MIT6_01SCS11_chap03.pdf`); 6.01SC playlist Unit 1 lectures.
Then do `swLab01` (the `V2` vector class) under `teach-workspace/work/6.01SC/swLab01/`.

**Try:** model something you own with classes — a battery cell and a pack — and bring questions
to the agent.
