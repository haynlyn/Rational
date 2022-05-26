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
        elif isinstance(num, Rational) and isinstance(den, Rational):
            #print("Rat/Rat")
            self.num = num.num * den.den
            self.den = num.den * den.num
        elif isinstance(num, Rational):
            #print('Rat/int')
            self = num/den
        elif isinstance(den, Rational):
            #print('int/Rat')
            self = num/den
        else:
            raise ValueError("numerator and denominator need to be integers or Rationals")

    """def __gcd_nd(self):
        g = 1
        n, d = self.num, self.den
        if n==d:
            return n
        sqn, sqd = n**.5, d**.5
        for i in range(2, int(min(sqn, sqd))+1):
            if n%i == 0 and d%i == 0 and i > g:
                g = i
                jn, jd = n//i, d//i
                if d%jn == 0 and jn > g:
                    g = jn
                if n%jd == 0 and jd > g:
                    g = jd
        return g"""

    def __mul__(self, other):
        #print("self: {}\tother: {}".format(self, other))
        if isinstance(other, Rational):
            return Rational(self.num * other.num, self.den * other.den)
        elif isinstance(other, int):
            return self.__mul__(Rational(other, 1))
        else:
            return NotImplemented

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

    def __eq__(self, other):
        if isinstance(other, Rational):
            sself = self.simplify()
            sother = other.simplify()
            return sself.num * sother.den == sself.den * sother.num
        elif isinstance(other, int):
            return self.__eq__(Rational(other, 1))
        else:
            return NotImplemented

    def simplify(self):
        g = gcd(self.num, self.den)
        #g = self.__gcd_nd()
        return Rational(self.num//g, self.den//g)

    def is_simplified(self):
        # check if self is already expressed as simplified-self
        pass

    def remainder(self):
        # return num % den
        pass

    def fractional_part(self):
        # same as remainder()
        pass

    def whole_part(self):
        # return num//den
        pass

    def parts(self):
        #return some representation of (whole_part(), fractional_part())
        pass
