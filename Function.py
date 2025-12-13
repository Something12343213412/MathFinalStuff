# base class for which all other types will be based on
class Function:
    def __init__(self):
        pass

    def evaluate(self, x):
        return 0

    def to_string(self):
        return "empty"

    def take_integral(self):
        return self

    def take_derivative(self):
        return self

    def multiply(self, other=None):
        return self

    def add(self, other=None):
        return self


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
    def multiply(self, other: Function=None):
        left = MultipliedFunction(self.left, other)
        right = MultipliedFunction(self.right, other)
        return AddedFunction(left, right)

    def divide(self, other: Function=None):



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
        left = MultipliedFunction(self.left.take_derivative(), self.right)
        right = MultipliedFunction(self.left, self.right.take_derivative())
        # combining both with new multiplied function
        return MultipliedFunction(left, right)


# here in the file to avoid circular imports, hopefully works :)
from Polynomial import Polynomial
# A function raised to a real number power
class RealExponentFunction(Function):
    def __init__(self, inside:Function, exponent:float):
        super().__init__()
        self.inside = inside
        self.exponent = exponent

    def evaluate(self, x):
        # not sure on limits of ** function, gonna find out lol
        return self.inside.evaluate(x)**x

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

# can't just do inverse since can't just mess with exponents as haven't built infrastructure yet
#class DividedFunction(Function):
