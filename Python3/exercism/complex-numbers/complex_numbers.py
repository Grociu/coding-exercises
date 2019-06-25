import math


class ComplexNumber(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        return ComplexNumber(
            self.real + other.real,
            self.imaginary + other.imaginary
            )

    def __mul__(self, other):
        return ComplexNumber(
            self.real * other.real - self.imaginary * other.imaginary,
            self.real * other.imaginary + other.real * self.imaginary
            )

    def __sub__(self, other):
        return ComplexNumber(
            self.real - other.real,
            self.imaginary - other.imaginary
            )

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        real_part = self.real * other.real + self.imaginary * other.imaginary
        imag_part = self.imaginary * other.real - self.real * other.imaginary
        return ComplexNumber(
            real_part / denominator,
            imag_part / denominator
        )

    def __abs__(self):
        return (self.real ** 2 + self.imaginary ** 2) ** 0.5

    def conjugate(self):
        return ComplexNumber(
            self.real,
            self.imaginary * -1
        )

    def exp(self):
        return ComplexNumber(math.exp(self.real), 0) * ComplexNumber(
            math.cos(self.imaginary),
            math.sin(self.imaginary)
            )
