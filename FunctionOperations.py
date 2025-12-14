# file exists to avoid circular imports lmao
from Polynomial import Polynomial
from Function import Function


#when one needs to add two functions
class AddedFunction(Function):
    def __init__(self, left: Function, right: Function):
        super().__init__()
        self.left = left
        self.right = right

    def evaluate(self, x):
        return self.left.evaluate(x) + self.right.evaluate(x)

    def to_string(self):
        return f"({self.left.to_string()} + {self.right.to_string()})"

    # just separates it into two integrals
    def take_integral(self):
        return AddedFunction(self.left.take_integral(), self.right.take_integral())

    # just takes two separate derivatives
    def take_derivative(self):
        return AddedFunction(self.left.take_derivative(), self.right.take_derivative())

    # creates an added function of new multiplied Functions
    def multiply(self, other: Function = None):
        left = MultipliedFunction(self.left, other)
        right = MultipliedFunction(self.right, other)
        return AddedFunction(left, right)

    def divide(self, other: Function = None):
        left = MultipliedFunction(self.left, RealExponentFunction(other, -1))
        right = MultipliedFunction(self.right, RealExponentFunction(other, -1))
        return left, right

    def add(self, other=None):
        return AddedFunction(self, other)

    def subtract(self, other=None):
        return AddedFunction(self, MultipliedFunction(Polynomial(1, [-1], [0]), other))


# Exist when one needs to multiply two functions
class MultipliedFunction(Function):
    def __init__(self, left: Function, right: Function):
        super().__init__()
        self.left = left
        self.right = right

    def evaluate(self, x):
        return self.left.evaluate(x)*self.right.evaluate(x)

    def to_string(self):
        return f"({self.left.to_string()})({self.right.to_string()})"

    # don't even try lmao
    def take_integral(self):
        return None

    def take_derivative(self):
        #create new left as dv*u + v*du
        #print(f"left before is {self.left.to_string()}")
        left = MultipliedFunction(self.left.take_derivative(), self.right)
        right = MultipliedFunction(self.left, self.right.take_derivative())
        #print(f"Left is {left.to_string()}, right is {right.to_string()}")
        # combining both with new multiplied function
        return AddedFunction(left, right)

    def add(self, other=None):
        return AddedFunction(self, other)

    def subtract(self, other=None):
        return AddedFunction(self, MultipliedFunction(Polynomial(1,[-1],[0]), other))

    def multiply(self, other=None):
        return MultipliedFunction(self, other)

    def divide(self, other=None):
        return self.multiply(RealExponentFunction(other, -1))

# A function raised to a real number power
class RealExponentFunction(Function):
    def __init__(self, inside:Function, exponent: float):
        super().__init__()
        self.inside = inside
        self.exponent = exponent

    def evaluate(self, x):
        return self.inside.evaluate(x)**self.exponent

    def to_string(self):
        return f"({self.inside.to_string()})^{self.exponent}"

    # assumes form of f(u)du, very restricted
    def take_integral(self):
        # adding 1 to the exponent
        new_exp = self.exponent+1
        # creates exponent^-1 in the form of a polynomial
        coef = Polynomial(1, [new_exp**(-1)], [0])
        # takes the original function and multiplies it by the coef found earlier
        inside = MultipliedFunction(self.inside, coef)
        # return the function with the nex exp
        return RealExponentFunction(inside, new_exp)

    # assumes d/dx[f(g(x))] = df(g(x))*dg(x), could be infinite composition
    def take_derivative(self):
        # d/dx x^n = nx^(...)
        coef = Polynomial(1, [self.exponent], [0])
        # d/dx x^n = nx^(n-1)
        new_exp = self.exponent-1
        # d/dx f(x)^n = nf(x)^...*...
        inside = MultipliedFunction(self.inside, coef)
        # d/dx f(x)^n = nf(x)^(n-1)*...
        left = RealExponentFunction(inside, new_exp)
        # d/dx f(x)^n = ...*d/dx f(x)
        right = self.inside.take_derivative()
        # d/dx f(x)^n = nf(x)^(n-1)*df(x)
        return MultipliedFunction(left, right)

    def add(self, other=None):
        return AddedFunction(self, other)

    def subtract(self, other=None):
        return AddedFunction(self, MultipliedFunction(Polynomial(1,[-1],[0]), other))

    def multiply(self, other=None):
        return MultipliedFunction(self, other)

    def divide(self, other=None):
        return self.multiply(RealExponentFunction(other, -1))
