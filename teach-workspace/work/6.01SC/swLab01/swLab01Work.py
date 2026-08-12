"""6.01 swLab01 — completed work file (Python 3).

Part 1: fib(n), the nth Fibonacci number.
Part 2: class V2, a two-dimensional vector.

The swLab01 handout is not in the download, so two conventions are chosen and
documented in solution.md:
  - fib uses the standard base fib(0) = 0, fib(1) = 1.
  - V2 implements the operations a 6.01 vector class needs: add, subtract,
    scalar multiply (both orders), dot product, norm, and value equality.

Run the self-check:
    python swLab01Work.py
"""


def fib(n):
    """Return the nth Fibonacci number: fib(0) = 0, fib(1) = 1."""
    if n < 0:
        raise ValueError("fib is defined for n >= 0")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


class V2:
    """A two-dimensional vector with the arithmetic a 6.01 model needs."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "V2(" + str(self.x) + ", " + str(self.y) + ")"

    __repr__ = __str__

    def __add__(self, other):
        return V2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return V2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """Dot product when other is a V2; scalar multiplication otherwise."""
        if isinstance(other, V2):
            return self.x * other.x + self.y * other.y
        return V2(self.x * other, self.y * other)

    def __rmul__(self, other):
        # other * v  (e.g. 3 * v) — same scalar multiplication as __mul__
        return self * other

    def norm(self):
        """Euclidean magnitude of the vector."""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __eq__(self, other):
        return isinstance(other, V2) and self.x == other.x and self.y == other.y


def main():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(5) == 5
    assert fib(8) == 21
    print("fib: 0..8 ->", [fib(i) for i in range(9)])

    a = V2(3, 4)
    b = V2(1, 2)
    print("a           =", a)
    print("a + b       =", a + b)
    print("a - b       =", a - b)
    print("a * b (dot) =", a * b)
    print("3 * a       =", 3 * a)
    print("a * 3       =", a * 3)
    print("a.norm()    =", a.norm())
    assert a + b == V2(4, 6)
    assert a - b == V2(2, 2)
    assert a * b == 3 * 1 + 4 * 2
    assert 3 * a == V2(9, 12)
    assert a * 3 == V2(9, 12)
    assert a.norm() == 5.0
    assert a == V2(3, 4)
    print("all swLab01 self-checks passed")


if __name__ == "__main__":
    main()
