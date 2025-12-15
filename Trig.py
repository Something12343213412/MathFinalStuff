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
        return self.coef*tan(self.inside.evaluate(x))

    def to_string(self):
        if not self.coef == 1:
            return f"[{self.coef}tan({self.inside.to_string()})]"
        return f"tan({self.inside.to_string()})"

    # add ln support later if you feel like it
    def take_integral(self):
        #return Sin(coef=self.coef, inside=self.inside)
        return None

    def take_derivative(self):
        inside = MultiplyScalar(-self.coef**2, SecSquared(inside=self.inside))
        #checks if it is just multiplying by 1
        #print(self.inside.take_derivative().to_string())
        if self.inside.take_derivative().to_string() == "1" or self.inside.take_derivative().to_string() == "":
            return inside
        return MultipliedFunction(inside, self.inside.take_derivative())

class Csc(Function):
    def __init__(self, inside: Function = Polynomial(1, [1], [1]), coef=1):
        super().__init__()
        self.coef = coef
        self.inside = inside

    def evaluate(self, x):
        return self.coef/sin(self.inside.evaluate(x))

    def to_string(self):
        if not self.coef == 1:
            return f"[{self.coef}csc({self.inside.to_string()})]"
        return f"csc({self.inside.to_string()})"

    # add ln support later if you feel like it
    def take_integral(self):
        #return Sin(coef=self.coef, inside=self.inside)
        return None

    def take_derivative(self):
        csc_out = deepcopy(self)
        # flip sign
        csc_out.coef *= -1
        #checks if it is just multiplying by 1
        if self.inside.take_derivative().to_string() == "":
            return MultipliedFunction(csc_out, Cot(self.inside))
        return MultipliedFunction(MultipliedFunction(csc_out, Cot(self.inside)), self.inside.take_derivative())

class Sec(Function):
    def __init__(self, inside: Function = Polynomial(1, [1], [1]), coef=1):
        super().__init__()
        self.coef = coef
        self.inside = inside

    def evaluate(self, x):
        return self.coef/cos(self.inside.evaluate(x))

    def to_string(self):
        if not self.coef == 1:
            return f"[{self.coef}sec({self.inside.to_string()})]"
        return f"sec({self.inside.to_string()})"

    # add ln support later if you feel like it
    def take_integral(self):
        #return Sin(coef=self.coef, inside=self.inside)
        return None

    # returns -cos(u) * du
    def take_derivative(self):
        sec_out = deepcopy(self)
        # checks if it is just multiplying by 1
        if self.inside.take_derivative().to_string() == "":
            return MultipliedFunction(sec_out, Tan(self.inside))
        return MultipliedFunction(MultipliedFunction(sec_out, Tan(self.inside)), self.inside.take_derivative())

class Cot(Function):
    def __init__(self, inside: Function = Polynomial(1, [1], [1]), coef=1):
        super().__init__()
        self.coef = coef
        self.inside = inside

    def evaluate(self, x):
        return self.coef*tan(self.inside.evaluate(x))**-1

    def to_string(self):
        if not self.coef == 1:
            return f"[{self.coef}cot({self.inside.to_string()})]"
        return f"cot({self.inside.to_string()})"

    # add ln support later if you feel like it
    def take_integral(self):
        #return Sin(coef=self.coef, inside=self.inside)
        return None

    # returns -cos(u) * du
    def take_derivative(self):
        inside = MultiplyScalar(-self.coef**2, CscSquared(inside=self.inside))
        #checks if it is just multiplying by 1
        if self.inside.take_derivative().to_string() == "1" or self.inside.take_derivative().to_string() == "":
            return inside
        return MultipliedFunction(inside, self.inside.take_derivative())

# area for special / specific classes due to easy integral rules
class SecSquared(RealExponentFunction):
    def __init__(self, inside: Function = Polynomial(1, [1], [1])):
        inside = Sec(inside)
        super().__init__(inside=inside, exponent=2)

    def take_integral(self):
        return Tan(inside=self.inside.inside)


class CscSquared(RealExponentFunction):
    def __init__(self, inside: Function = Polynomial(1, [1], [1])):
        inside = Csc(inside)
        super().__init__(inside=inside, exponent=2)

    def take_integral(self):
        return Cot(inside=self.inside, coef=-1)


class SecTan():
    pass