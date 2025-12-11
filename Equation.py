# base class for which all other types will be based on
class Equation:
    def __init__(self):
        pass

    def evaluate(self, x):
        return 0

    def get_text(self):
        return "empty"

    def get_integral(self):
        return 0

    def get_derivative(self):
        return 0