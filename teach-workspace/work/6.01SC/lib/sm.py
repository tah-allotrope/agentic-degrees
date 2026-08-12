"""State-machine base class and combinators, reimplemented without lib601.

This is the 6.01 `sm` module contract (plan PHASE-02 function signatures), usable
standalone so hw1's Tokenizer extension and the week-4 capstone can import it:

    from lib.sm import SM, Delay, Accumulator, Cascade

Contract:
    class SM:
        def start_state(self) -> object
        def get_next_values(self, state, inp) -> (next_state, output)
        def transduce(self, inputs: list) -> list

`start_state` is a *method* returning the machine's initial state (so every call
to transduce starts clean); `get_next_values` is the heart of the machine.
"""


class SM:
    def start_state(self):
        raise NotImplementedError

    def get_next_values(self, state, inp):
        raise NotImplementedError

    def transduce(self, inputs):
        """Feed every input through the machine and return the output sequence."""
        state = self.start_state()
        outputs = []
        for inp in inputs:
            state, output = self.get_next_values(state, inp)
            outputs.append(output)
        return outputs


class Cascade(SM):
    """Feed machine1's output into machine2. State = (state1, state2)."""

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def start_state(self):
        return (self.m1.start_state(), self.m2.start_state())

    def get_next_values(self, state, inp):
        s1, s2 = state
        s1, o1 = self.m1.get_next_values(s1, inp)
        s2, o2 = self.m2.get_next_values(s2, o1)
        return ((s1, s2), o2)


class Parallel(SM):
    """Run two machines on the same input; output is the pair of outputs."""

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def start_state(self):
        return (self.m1.start_state(), self.m2.start_state())

    def get_next_values(self, state, inp):
        s1, s2 = state
        s1, o1 = self.m1.get_next_values(s1, inp)
        s2, o2 = self.m2.get_next_values(s2, inp)
        return ((s1, s2), (o1, o2))


class Feedback(SM):
    """Wire a machine's output back into its own input (state = machine state).

    The machine must have a method `feedback_init(inp)` returning the initial
    feedback value; by default the first input is passed through unchanged.
    """

    def __init__(self, m):
        self.m = m

    def start_state(self):
        return self.m.start_state()

    def feedback_init(self, inp):
        return inp

    def get_next_values(self, state, inp):
        fb = self._feedback
        s, o = self.m.get_next_values(state, fb)
        return (s, o)

    def transduce(self, inputs):
        state = self.start_state()
        outputs = []
        for inp in inputs:
            self._feedback = self.feedback_init(inp)
            state, output = self.get_next_values(state, inp)
            outputs.append(output)
        return outputs


class Delay(SM):
    """Emit the previous input (initial value first), then hold the newest."""

    def __init__(self, initial):
        self._initial = initial

    def start_state(self):
        return self._initial

    def get_next_values(self, state, inp):
        return (inp, state)


class Accumulator(SM):
    """Sum the inputs seen so far; output the running total."""

    def __init__(self, initial=0.0):
        self._initial = initial

    def start_state(self):
        return self._initial

    def get_next_values(self, state, inp):
        total = state + inp
        return (total, total)
