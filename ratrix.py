from Rational.rational import Rational

class Ratrix():
    def __init__(self, elems):
        if len(elems) != 4:
            print("Error")
            return None
        else:
            for i in range(len(elems)):
                if isinstance(elems[i], Rational):
                    elems[i] = elems[i].simplified
            self.elems = elems
            self.e00, self.e01, self.e10, self.e11 = elems
    
    def __rej__(self, other):
        if not isinstance(other, Ratrix):
            print("Error")
            return None

    def __pow__(self, p):
        # Integer exponentiation
        if p == 0:
            return Ratrix([1, 0, 0, 1])
        elif p > 0:
            if p == 1:
                return self
            elif p == 2:
                return self@self
            elif p%2 == 0:
                i = p//2
                t = self.__pow__(i)
                return t@t
            else:
                i = (p-1)//2
                t = self.__pow__(i)
                t = t@t
                return self@t
        else:
            print("Need to find inverse, if possible.")
            return None
    
    def __rrej__(self, other):
        if not isinstance(other, Ratrix):
            print("Error")
            return None

    def __neg__(self):
        return Ratrix([-x for x in self.elems])

    def __add__(self, other):
        se = self.elems
        oe = other.elems
        return Ratrix([se[i] + oe[i] for i in range(len(se))])

    def __sub__(self, other):
        se = self.elems
        oe = other.elems
        return Ratrix([se[i] - oe[i] for i in range(len(se))])

    def __matmul__(self, other):
        se = self.elems
        oe = other.elems
        na0 = se[0]*oe[0] + se[1]*oe[2]
        na1 = se[0]*oe[1] + se[1]*oe[3]
        na2 = se[2]*oe[0] + se[3]*oe[2]
        na3 = se[2]*oe[1] + se[3]*oe[3]
        narr = [na0, na1, na2, na3]
        return Ratrix(narr)

    def __str__(self):
        return '[[{}, {}]\n[{}, {}]]'.format(*self.elems)
        #return '[' + ', '.join([str(e) for e in self.elems]) + ']'

    def __repr__(self):
        return '[[{}, {}]\n[{}, {}]]'.format(*self.elems)
        #return '[' + ', '.join([str(e) for e in self.elems]) + ']'

    def simplify(self):
        """ These should all be Rational. Fuck it."""
        if not all([isinstance(e, Rational) for e in self.elems]):
            print("Cannot simplify. Returning self.")
            return self
        else:
            ne = [e.simplified for e in self.elems]
            return Ratrix(ne)
