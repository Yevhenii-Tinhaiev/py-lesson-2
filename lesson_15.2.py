from math import gcd

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Denominator cannot be zero.")
        self.a = a
        self.b = b

    def _lcm(self, x, y):
        return abs(x * y) // gcd(x, y)

    def _normalize(self, a, b):
        common = gcd(a, b)
        return a // common, b // common

    def __add__(self, other):
        lcm = self._lcm(self.b, other.b)
        a1 = self.a * (lcm // self.b)
        a2 = other.a * (lcm // other.b)
        return Fraction(a1 + a2, lcm)

    def __sub__(self, other):
        lcm = self._lcm(self.b, other.b)
        a1 = self.a * (lcm // self.b)
        a2 = other.a * (lcm // other.b)
        return Fraction(a1 - a2, lcm)

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __eq__(self, other):
        a1, b1 = self._normalize(self.a, self.b)
        a2, b2 = self._normalize(other.a, other.b)
        return a1 == a2 and b1 == b2

    def __lt__(self, other):
        return self.a * other.b < other.a * self.b

    def __gt__(self, other):
        return self.a * other.b > other.a * self.b

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"
