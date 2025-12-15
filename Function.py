
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

    """ could use numpy but fuck you, I don't want to be efficient right now and you can't stop me
    also don't want to create a dependency on another library but if it actually becomes an issue a numpy
    implementation would be very easy """
    def find_definite_integral(self, a, b):
        total = 0
        sign = 1
        percentage_distance = .0001  # just pretend we take the num mult by 100 and add % sign
        if a > b:
            # swap around
            b, a = a, b
            sign = -1

        dx = (b - a) * percentage_distance
        while a < b:
            total += self.evaluate(a) * percentage_distance
            a += dx

        return sign * total/10  # do not ask me why the /10 is needed, it is god's will ig

    def take_derivative(self):
        return self

    def raise_exp(self, num=None):
        return self

    def multiply(self, other=None):
        return self

    def divide(self, other=None):
        return self

    def add(self, other=None):
        return self

    def subtract(self, other=None):
        return self

