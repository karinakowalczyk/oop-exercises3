from numbers import Number, Integral
import numpy as np


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other


    def __sub__(self, other): # implements self - other

        if isinstance (other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            print(common)
            coefs = tuple(a-b for a, b in zip(self.coefficients, 
                                                other.coefficients) )
            print("coefs", coefs)
            coefs += self.coefficients[common:] + tuple(-c for c in other.coefficients[common:])
            print("coefs", coefs)
            return Polynomial(coefs)

        if isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,) + self.coefficients[1:])

    def __rsub__(self, other): #defines other - self
        diff_polyn = self - other
        new_coeffs = diff_polyn.coefficients
        new_coeffs *= -1
        return Polynomial(new_coeffs)

    def __mul__(self, other):
        if isinstance(other, Polynomial):
            coefs_self = np.array(self.coefficients)
            coefs_other = np.array(other.coefficients)
            new_coefs = np.zeros(self.degree() + other.degree() + 1)
            for i in range(len(coefs_self)):
                for j in range(len(coefs_other)):
                    new_coefs[i+j] += coefs_self[i]*coefs_other[j]
            return Polynomial(tuple(new_coefs))
        
        if isinstance(other, Number):
            return Polynomial(tuple(other* a for a in self.coefficients))

    def __rmul__(self, other):
        return self*other

    def __pow__(self, n):
        if isinstance(n, Integral):
            power = self
            for i in range(n-1):
                power*=self
            return power
        else: 
            return NotImplemented
    
    def __call__(self, x):
        res = 0
        coefs = np.array(self.coefficients)
        for i in range(len(coefs)):
            res += coefs[i]* x**i
        return res

    def dx(self):
        coefs = np.array(self.coefficients)
        
        if len(coefs)==1:
            dev_coefs = np.zeros(1)
        else:
            dev_coefs = np.zeros(len(coefs)-1)
            for i in range(1,len(coefs)):
                dev_coefs[i-1] = i*coefs[i]
                print('derivateive',dev_coefs)
        return Polynomial(tuple(dev_coefs))

def derivative(P):
    return P.dx()

            

