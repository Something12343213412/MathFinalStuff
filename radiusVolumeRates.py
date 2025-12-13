#problem type of given radius or edge of something find area
from Polynomial import Polynomial
from random import randint
from time import time

class SphereRate:
    def __init__(self):
        self.time = 0
        self.Equation = Polynomial(1, [4], [2])
        self.radius = randint(1, 20)
        # rate of change of the radius
        self.dr = randint(-5, 5)
        # 0 case
        if self.dr == 0:
            self.dr = randint(1,5)

    def get_answer(self):
        return self.Equation.evaluate(self.radius) * self.dr

    # asks a question and returns a list of whether user got question right and the time it took
    def ask_question(self):
        print(f"The radius of a sphere increases at {self.dr} in/s"
              f" \n What is the rate of change of the volume when r = {self.radius}")
        start = time()
        answer = input(" Leave answer without pi ex:4 instead of 4pi ")
        end = time()
        self.time = end-start
        if float(answer) == float(self.get_answer()):
            print(f"correct, answer was {self.get_answer()}")
            return True, self.time
        else:
            print(f"wrong, answer was {self.get_answer()}")
            return False, self.time


