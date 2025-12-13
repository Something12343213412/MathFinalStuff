# base class for which all other types will be based on
# realize a bad name but too late now lmao
class Equation:
    def __init__(self):
        pass

    def evaluate(self, x):
        return 0

    def to_string(self):
        return "empty"

    def take_integral(self):
        return 0

    def take_derivative(self):
        return 0