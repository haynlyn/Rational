from math import gcd

class Rational():
    def __init__(self, num, den):
        #print(num, den)
        if den == 0:
            raise ZeroDivisionError("cannot have denominator of zero")
        elif isinstance(num, int) and isinstance(den, int):
            #print("int/int")
            self.num = num
            self.den = den
        elif isinstance(num, Rational) or isinstance(den, Rational):
            rat = num/den
            self.num, self.den = rat.num, rat.den
        else:
            raise ValueError("numerator and denominator need to be integers or Rationals")
        if self.den < 0:
            self.num *= -1
            self.den *= -1
        self.whole_part = self.num // self.den
        self.remainder = self.num % self.den
        self.fractional_part = Rational(self.num % self.den, self.den) if self.num >= self.den else self
        self.as_float = self.num / self.den

    def __mul__(self, other):
        #print("self: {}\tother: {}".format(self, other))
        if isinstance(other, Rational):
            return Rational(self.num * other.num, self.den * other.den)
        elif isinstance(other, int):
            return self.__mul__(Rational(other, 1))
        else:
            return NotImplemented

    def __pow__(self, p):
        # Integer exponentiation
        if p == 0:
            return Rational(1, 1)
        elif p > 0:
            if p == 1:
                return self
            elif p==2:
                return self * self
            elif p%2==0:
                i = p//2
                t = self.__pow__(i)
                return t*t
            else:
                i = (p-1)//2
                t = self.__pow__(i)
                return self * t * t
        else:
            t = 1/self
            return t.__pow__(-p)

    def __rmul__(self, other):
        #print("self: {}\tother: {}".format(self, other))
        if isinstance(other, int):
            return Rational(other, 1) * self
        else:
            return NotImplemented
    
    def __neg__(self):
        return Rational(-self.num, self.den)

    def __truediv__(self, other):
        #print("self: {}\tother: {}".format(self, other))
        if isinstance(other, Rational):
            return self * Rational(other.den, other.num)
        elif isinstance(other, int):
            return self * Rational(1, other)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        #print("self: {}\tother: {}".format(self, other))
        if isinstance(other, Rational):
            return Rational(other.den, other.num) / self
        elif isinstance(other, int):
            return Rational(other, 1) / self
        else:
            return NotImplemented

    def __add__(self, other):
        #print("self: {}\tother: {}".format(self, other))
        if isinstance(other, Rational):
            nden = self.den * other.den
            nnum = self.den * other.num + self.num * other.den
            return Rational(nnum, nden)
        elif isinstance(other, int):
            return self + Rational(other, 1)
        else:
            return NotImplemented

    def __radd__(self, other):
        #print("self: {}\tother: {}".format(self, other))
        if isinstance(other, int):
            return Rational(other, 1) + self
        else:
            return NotImplemented

    def __sub__(self, other):
        #print("self: {}\tother: {}".format(self, other))
        if isinstance(other, Rational):
            return self + Rational(-other.num, other.den)
        elif isinstance(other, int):
            return self + Rational(-other, 1)
        else:
            return NotImplemented

    def __rsub__(self, other):
        #print("self: {}\tother: {}".format(self, other))
        if isinstance(other, int):
            return Rational(other, 1) - self
        else:
            return NotImplemented

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __repr__(self):
        return "{}/{}".format(self.num, self.den)

    # Comparison operators: BEGIN

    def __eq__(self, other):
        if isinstance(other, Rational):
            return (self - other).simplified.num == 0
        elif isinstance(other, int):
            return self.__eq__(Rational(other, 1))
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rational):
            t = (self - other).simplified
            return t.num < 0
        elif isinstance(other, int):
            return self.__lt__(Rational(other, 1))
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rational):
            t = (self - other).simplified
            return t.num > 0
        elif isinstance(other, int):
            return self.__gt__(Rational(other, 1))
        else:
            return NotImplemented

    def __ne__(self, other):
        return not (self == other)

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)

    # Comparison operators: END

    @property
    def simplified(self):
        g = gcd(self.num, self.den)
        #g = self.__gcd_nd()
        return Rational(self.num//g, self.den//g)

    def is_simplified(self):
        # check if self is already expressed as simplified-self
        sp = (self.num, self.den)
        ss = self.simplified
        ssp = (ss.num, ss.den)
        return sp == ssp

    '''
    def remainder(self):
        return self.num % self.den

    def fractional_part(self):
        return self.num % self.den

    def whole_part(self):
        return self.num // self.den
    '''

    def parts(self):
        return (self.whole_part, self.remainder, self.den)

    @property
    def invm(self):
        return 1/self

    @property
    def inva(self):
        return -self
