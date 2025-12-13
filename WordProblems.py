from random import randint
from time import time

class FenceRiver:
    def __init__(self):
        self.time = 0
        self.x = randint(5,30)
        # y will always = 2x
        self.y = 2*self.x
        self.area = self.x*self.y

    def ask_question(self):
        print(f" A Farmer plans to fence a rectangular pasture adjacient to a river. The pasture must contain "
              f" \n {self.area} m^2, what are the dimensions that would lead to the least fencing required if one side, "
              f" \n y, was along a river?")
        start = time()
        answer = int(input("What is the x? ")), int(input("What is the y? "))
        end = time()
        self.time = end - start
        if answer == (self.x, self.y):
            print(f"Correct, your answer was {answer}, answer was {[self.x, self.y]}")
            return True, self.time
        else:
            print(f"wrong, your answer was {answer}, answer was {[self.x, self.y]}")
            return False, self.time

class FenceTwoSquares:
    def __init__(self):
        # the times 3 exists so that y will always be an integer
        self.x = randint(5, 10)*3
        self.y = int(4/3 * self.x)
        self.perimeter = 4*self.x + 3*self.y
        self.time = 0

    def ask_question(self):
        # visualization is hard so may want to reword later
        print(f" A rancher has {self.perimeter} ft of fencing to enclose 2 adjacent rectangular corals. What Dimensions "
              f" \n would lead to the greatest area if they share one border y?")
        start = time()
        answer = int(input("What is the x? ")), int(input("What is the y? "))
        end = time()
        self.time = end - start
        if answer == (self.x, self.y):
            print(f"Correct, your answer was {answer}, answer was {[self.x, self.y]}")
            return True, self.time
        else:
            print(f"wrong, your answer was {answer}, answer was {[self.x, self.y]}")
            return False, self.time

