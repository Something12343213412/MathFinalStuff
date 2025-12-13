from Function import Function, MultipliedFunction
from Polynomial import Polynomial
from math import sin, cos, pi

class Sin(Function):
    # base inside will be just x
    def __init__(self, coef=1, inside: Function = Polynomial(1, [1], [1])):
        super().__init__()
        self.coef = coef
        self.inside = inside

    def evaluate(self, x):
        return sin(self.inside.evaluate(x))

    def to_string(self):
        return f"sin({self.inside.to_string()})"

    # assumes in form of sin(u)du, shouldn't be used that much as integrals should be constructed from parts
    def take_integral(self):
        return Cos(coef=self.coef, inside=self.inside)

    # returns -cos(u) * du
    def take_derivative(self):
        return MultipliedFunction(Cos(coef=-self.coef, inside=self.inside), self.inside.take_derivative())

    # exists to multiply functions
    def multiply(self, other: Function):
        return MultipliedFunction(self, other)

class Cos(Function):
    def __init__(self, coef=1, inside: Function = Polynomial(1, [1], [1])):
        super().__init__()
        self.inside = inside
