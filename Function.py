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

