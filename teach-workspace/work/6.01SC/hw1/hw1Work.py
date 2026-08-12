"""6.01 HW1: Symbolic Calculator — completed work file (Python 3).

Reimplemented standalone (ASM-006): the shipped skeleton imported `lib601.sm`,
which is not in this repository. The state-machine pieces here import `lib.sm`
from the workspace's own reimplementation of that module.

Run the tests:
    python hw1Work.py
"""

import operator
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from lib.sm import SM  # noqa: E402  (standalone replacement for lib601.sm)

# characters that are single-character tokens
seps = ["(", ")", "+", "-", "*", "/", "="]


class BinaryOp:
    opStr = "?"

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __str__(self):
        return self.opStr + "(" + str(self.left) + ", " + str(self.right) + ")"

    __repr__ = __str__

    def eval(self, env):
        """Lazy/partial evaluation (hw1 Step 7).

        Evaluate both children; if they are both numbers, compute the answer,
        otherwise rebuild the same operator node from the (simplified) children.
        """
        left_value = self.left.eval(env)
        right_value = self.right.eval(env)
        if isNum(left_value) and isNum(right_value):
            return self.op(left_value, right_value)
        return self.__class__(left_value, right_value)

    def eval_eager(self, env):
        """Eager evaluation: children must resolve to numbers."""
        return self.op(self.left.eval_eager(env), self.right.eval_eager(env))


class Sum(BinaryOp):
    opStr = "Sum"
    op = operator.add


class Prod(BinaryOp):
    opStr = "Prod"
    op = operator.mul


class Quot(BinaryOp):
    opStr = "Quot"
    op = operator.truediv


class Diff(BinaryOp):
    opStr = "Diff"
    op = operator.sub


class Assign(BinaryOp):
    opStr = "Assign"

    def eval(self, env):
        """Lazy assignment: store the unevaluated right-hand tree."""
        env[self.left.name] = self.right
        return None

    def eval_eager(self, env):
        """Eager assignment: store the evaluated numeric value."""
        env[self.left.name] = self.right.eval_eager(env)
        return None


class Number:
    def __init__(self, val):
        self.value = val

    def __str__(self):
        return "Num(" + str(self.value) + ")"

    __repr__ = __str__

    def eval(self, env):
        return self.value

    def eval_eager(self, env):
        return self.value


class Variable:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Var(" + self.name + ")"

    __repr__ = __str__

    def eval(self, env):
        if self.name in env:
            value = env[self.name]
            if isinstance(value, (Number, Variable, BinaryOp)):
                return value.eval(env)
            return value
        return self

    def eval_eager(self, env):
        return env[self.name]


# token is a string; returns True if it contains only digits
def numberTok(token):
    if not token:
        return False
    return all(char in "0123456789" for char in token)


# token is a string; returns True if its first character is a letter
def variableTok(token):
    return bool(token) and token[0].isalpha()


def isNum(thing):
    return type(thing) == int or type(thing) == float


def tokenize(input_string):
    """Split a fully parenthesized expression into a list of tokens."""
    tokens = []
    current = ""
    for char in input_string:
        if char == " ":
            if current:
                tokens.append(current)
                current = ""
        elif char in seps:
            if current:
                tokens.append(current)
                current = ""
            tokens.append(char)
        else:
            current += char
    if current:
        tokens.append(current)
    return tokens


def _makeOp(op, left, right):
    if op == "+":
        return Sum(left, right)
    if op == "-":
        return Diff(left, right)
    if op == "*":
        return Prod(left, right)
    if op == "/":
        return Quot(left, right)
    if op == "=":
        return Assign(left, right)
    raise ValueError("unknown operator " + repr(op))


def parse(tokens):
    """Recursive-descent parse of a token list into a syntax tree."""

    def parseExp(index):
        token = tokens[index]
        if numberTok(token):
            return (Number(float(token)), index + 1)
        if variableTok(token):
            return (Variable(token), index + 1)
        # must be "( expression op expression )"
        (leftTree, i) = parseExp(index + 1)
        op = tokens[i]
        (rightTree, i) = parseExp(i + 1)
        return (_makeOp(op, leftTree, rightTree), i + 1)

    (parsedExp, _) = parseExp(0)
    return parsedExp


class Tokenizer(SM):
    """State-machine tokenizer (hw1 extension, Step 5-6).

    One character per step; output is either the token that the step's
    character terminated, or "" when no token is ready yet.
    """

    def start_state(self):
        return ""

    def get_next_values(self, state, inp):
        if inp == " ":
            return ("", state)
        if inp in seps:
            return (inp, state)
        if state in seps or state == "":
            return (inp, state)
        return (state + inp, "")


def tokenizeBySM(input_string):
    """Tokenize using the state machine (hw1 Step 6)."""
    outputs = Tokenizer().transduce(input_string + " ")
    return [token for token in outputs if token != ""]


def calc():
    env = {}
    while True:
        try:
            e = input("% ")
        except EOFError:
            return
        print(parse(tokenize(e)).eval(env))
        print("   env =", env)


def calcTest(exprs, lazy=False):
    env = {}
    for e in exprs:
        print("%", e)
        tree = parse(tokenize(e))
        result = tree.eval(env) if lazy else tree.eval_eager(env)
        print(result)
        print("   env =", env)


def testTokenize():
    cases = [
        ("fred ", ["fred"]),
        ("777 ", ["777"]),
        ("777 hi 33 ", ["777", "hi", "33"]),
        ("**-)(", ["*", "*", "-", ")", "("]),
        ("( hi * ho )", ["(", "hi", "*", "ho", ")"]),
        ("(fred + george)", ["(", "fred", "+", "george", ")"]),
        ("(hi*ho)", ["(", "hi", "*", "ho", ")"]),
        ("( fred+george )", ["(", "fred", "+", "george", ")"]),
    ]
    for source, expected in cases:
        got = tokenize(source)
        status = "ok" if got == expected else "FAIL"
        print("%s tokenize(%r) -> %s" % (status, source, got))
    print("tokenizeBySM('(fred + george)') ->", tokenizeBySM("(fred + george)"))
    print("tokenizeBySM('**-)(') ->", tokenizeBySM("**-)("))


def testParse():
    cases = [
        (["a"], "Var(a)"),
        (["888"], "Num(888.0)"),
        (["(", "fred", "+", "george", ")"], "Sum(Var(fred), Var(george))"),
        (
            ["(", "(", "a", "*", "b", ")", "/", "(", "cee", "-", "doh", ")", ")"],
            "Quot(Prod(Var(a), Var(b)), Diff(Var(cee), Var(doh)))",
        ),
    ]
    for tokens, expected in cases:
        got = str(parse(tokens))
        status = "ok" if got == expected else "FAIL"
        print("%s parse(%s) -> %s" % (status, tokens, got))
    print("parse(tokenize('((a * b) / (cee - doh))')) ->",
          str(parse(tokenize("((a * b) / (cee - doh))"))))
    print("parse(tokenize('(a = (3 * 5))')) ->",
          str(parse(tokenize("(a = (3 * 5))"))))


def testEval():
    env = {}
    Assign(Variable("a"), Number(5.0)).eval_eager(env)
    print(Variable("a").eval_eager(env))              # 5.0
    env["b"] = 2.0
    print(Variable("b").eval_eager(env))              # 2.0
    env["c"] = 4.0
    print(Variable("c").eval_eager(env))              # 4.0
    print(Sum(Variable("a"), Variable("b")).eval_eager(env))            # 7.0
    print(Sum(Diff(Variable("a"), Variable("c")), Variable("b")).eval_eager(env))  # 3.0
    Assign(Variable("a"), Sum(Variable("a"), Variable("b"))).eval_eager(env)
    print(Variable("a").eval_eager(env))              # 7.0
    print(env)


def testLazyEval():
    env = {}
    Assign(Variable("a"), Sum(Variable("b"), Variable("c"))).eval(env)
    print(Variable("a").eval(env))              # Sum(Var(b), Var(c))
    env["b"] = Number(2.0)
    print(Variable("a").eval(env))              # Sum(2.0, Var(c))
    env["c"] = Number(4.0)
    print(Variable("a").eval(env))              # 6.0


testExprs = ["(2 + 5)", "(z = 6)", "z", "(w = (z + 1))", "w"]

lazyTestExprs = [
    "(a = (b + c))",
    "(b = ((d * e) / 2))",
    "a",
    "(d = 6)",
    "(e = 5)",
    "a",
    "(c = 9)",
    "a",
    "(d = 2)",
    "a",
]


def main():
    print("===== testTokenize =====")
    testTokenize()
    print("\n===== testParse =====")
    testParse()
    print("\n===== testEval (eager) =====")
    testEval()
    print("\n===== calcTest(testExprs, eager) =====")
    calcTest(testExprs)
    print("\n===== testLazyEval =====")
    testLazyEval()
    print("\n===== calcTest(lazyTestExprs, lazy) =====")
    calcTest(lazyTestExprs, lazy=True)


if __name__ == "__main__":
    main()
