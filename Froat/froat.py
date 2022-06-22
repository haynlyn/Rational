from Rational.rational import Rational

class Froat(float, Rational):
    # Add logic to capture user-added info on whether the float is terminating.
    ## If not, then capture position from last digit that repetition starts.
    ## If not applicable, then float is irrational and an error or something
        # should be thrown.
    def __init__(self, f):
        self.float = float(f)

    @property
    def as_rational(self):
        p, f = 0, self.float
        while f//1 != f:
            f *= 10
            p += 1
        return Rational(int(f), int(10**p))

    def __add__(self, other):
        if isinstance(other, float) | isinstance(other, int):
            return Froat(self.float + other)
        elif isinstance(other, Rational):
            rnum, rden = other.num, other.den
            return Froat(self + (rnum/rden))

    def __mul__(self, other):
        if isinstance(other, float) | isinstance(other, int):
            return Froat(self.float * other)
        elif isinstance(other, Rational):
            rnum, rden = other.num, other.den
            return Froat(self * (rnum/rden))

    def __sub__(self, other):
        return self + (-other)

    def __radd__(self, other):
        if isinstance(self, float) | isinstance(self, int):
            return Froat(self + other.float)
        elif isinstance(self, Rational):
            rnum, rden = self.num, self.den
            return Froat(other + (rnum/rden))

