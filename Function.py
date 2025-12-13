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


# can't just do inverse since can't just mess with exponents as haven't built infastructure yet
class DividedFunction(Function):
