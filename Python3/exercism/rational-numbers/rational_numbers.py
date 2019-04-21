from __future__ import division

DIV_BY_ZERO = "Exception 001: Dividing by zero!"

def gcd(a,b):
    """
    Returns the greatest common denominator of two numbers. 
    The gcd will be a negative int, if the denominator is negative.
    When divided by the gcd, denom will be always positive so the minus sign
    is always with the numerator.
    This function exists in the math module, but I wanted to write it myself.
    Uses Euclid algorithm.
    """
    if b == 0:
        raise Exception(DIV_BY_ZERO)
    if a == 0:
        return b
    Euclid = [max(abs(a),abs(b)), min(abs(a),abs(b))]
    while Euclid[-2] % Euclid[-1] != 0:
        Euclid.append(Euclid[-2] % Euclid[-1])
    else:
        if b < 0:
            return -(Euclid[-1])
        return Euclid[-1]

class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer // gcd(numer,denom)
        self.denom = denom // gcd(numer,denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)
              
    def __add__(self, other):
        sum_numer = self.numer * other.denom + self.denom * other.numer
        sum_denom = self.denom * other.denom
        return Rational(sum_numer,sum_denom)

    def __sub__(self, other):
        sub_numer = self.numer * other.denom - self.denom * other.numer
        sub_denom = self.denom * other.denom
        return Rational(sub_numer,sub_denom)

    def __mul__(self, other):
        mul_numer = self.numer * other.numer
        mul_denom = self.denom * other.denom
        return Rational(mul_numer,mul_denom)

    def __truediv__(self, other):
        div_numer = self.numer * other.denom 
        div_denom = other.numer * self.denom
        if div_denom == 0:
            raise Exception(DIV_BY_ZERO) 
        return Rational(div_numer,div_denom)

    def __abs__(self):
        abs_numer = abs(self.numer)
        abs_denom = abs(self.denom)
        return Rational(abs_numer, abs_denom)

    def __pow__(self, power):
        if power >= 0:
            pow_numer = self.numer ** power
            pow_denom = self.denom ** power
        if power < 0:
            pow_numer = self.denom ** abs(power)
            pow_denom = self.numer ** abs(power)
        return Rational(pow_numer,pow_denom)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)