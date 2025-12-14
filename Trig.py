from FunctionOperations import *
from math import sin, cos, tan

class Sin(BasicFuncOperations):
    # base inside will be just x
    def __init__(self, inside: Function = Polynomial(1, [1], [1]), coef=1):
        super().__init__()
        self.coef = coef
        self.inside = inside

    def evaluate(self, x):
        return self.coef*sin(self.inside.evaluate(x))

    def to_string(self):
        if not self.coef == 1:
            return f"[{self.coef}sin({self.inside.to_string()})]"
        return f"sin({self.inside.to_string()})"

    # assumes in form of sin(u)du, shouldn't be used that much as integrals should be constructed from parts
    def take_integral(self):
        return Cos(coef=-self.coef, inside=self.inside)

    # returns -cos(u) * du
    def take_derivative(self):
        #checks if it is just multiplying by 1
        if self.inside.take_derivative().to_string() == "":
            return Cos(coef=self.coef, inside=self.inside)
        return MultipliedFunction(Cos(coef=self.coef, inside=self.inside), self.inside.take_derivative())


class Cos(Function):
    def __init__(self, inside: Function = Polynomial(1, [1], [1]), coef=1):
        super().__init__()
        self.coef = coef
        self.inside = inside

    def evaluate(self, x):
        return self.coef*cos(self.inside.evaluate(x))

    def to_string(self):
        if not self.coef == 1:
            return f"[{self.coef}cos({self.inside.to_string()})]"
        return f"cos({self.inside.to_string()})"

    def take_integral(self):
        return Sin(coef=self.coef, inside=self.inside)

    # returns -cos(u) * du
    def take_derivative(self):
        #checks if it is just multiplying by 1
        if self.inside.take_derivative().to_string() == "":
            return Sin(coef=-self.coef, inside=self.inside)
        return MultipliedFunction(Sin(coef=-self.coef, inside=self.inside), self.inside.take_derivative())

class Tan(Function):
    def __init__(self, inside: Function = Polynomial(1, [1], [1]), coef=1):
        super().__init__()
        self.coef = coef
        self.inside = inside

    def evaluate(self, x):
        return self.coef*cos(self.inside.evaluate(x))

    def to_string(self):
        if not self.coef == 1:
            return f"[{self.coef}cos({self.inside.to_string()})]"
        return f"cos({self.inside.to_string()})"

    # add ln support later if you feel like it
    def take_integral(self):
        #return Sin(coef=self.coef, inside=self.inside)
        return None

    # returns -cos(u) * du
    def take_derivative(self):
        #checks if it is just multiplying by 1
        if self.inside.take_derivative().to_string() == "":
            return Sin(coef=-self.coef, inside=self.inside)
        return MultipliedFunction(Sin(coef=-self.coef, inside=self.inside), self.inside.take_derivative())