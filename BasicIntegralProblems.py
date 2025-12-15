from FunctionOperations import Polynomial
from time import time
from random import randint
from Trig import *

# Applying power rule to 3 cases, just polynomial, polynomial times a factor, polynomial divided by a number
class BasicPowerRule:
    def __init__(self, num_terms=3):
        self.base_polynomial = Polynomial(num_terms)
        self.time = 0

    # basic polynomial integral
    def question_type_1(self):
        # removing possible / 0 errors
        self.base_polynomial.remove_power(-1)
        print(f"Take the integral of {self.base_polynomial.to_string()}")
        self.time = time()
        input("Press enter when finished")
        self.time = time() - self.time
        if input(f"Answer was {self.base_polynomial.take_integral().to_string()} + C, Where you correct (y/n)") == "y":
            return True, self.time
        else:
            return False, self.time

    # Polynomial / by some exponent of x
    def question_type_2(self):
        # generating divisor
        divisor = randint(-5, 5)
        # 0 case
        if divisor == 0:
            divisor = randint(1, 5)

        divisor /= 2  # want to include sqrts

        # removing possible / 0 errors, checks for anything that will be 0
        self.base_polynomial.remove_power(divisor - 1)

        # code similar to that of type 1
        print(f"Take the integral of ({self.base_polynomial.to_string()}) / x^{divisor}")
        self.base_polynomial.divide_by_x(divisor)
        self.time = time()
        input("Press enter when finished")
        self.time = time() - self.time
        if input(f"Answer was {self.base_polynomial.take_integral().to_string()} + C, Where you correct (y/n)") == "y":
            return True, self.time
        else:
            return False, self.time

    # Polynomial multiplied by a factor
    def question_type_3(self):
        coef = randint(-5, 5)
        if coef == 0:
            coef = randint(1, 5)
        factor = [coef, randint(-6, 6)]

        # remove -1 errors
        self.base_polynomial.remove_power(-2)
        self.base_polynomial.remove_power(-1)
        
        print(f"Take the integral of ({self.base_polynomial.to_string()})({factor[0]}x + {factor[1]})")
        new_poly = self.base_polynomial.multiply_factor(factor)
        self.time = time()
        input("Press enter when finished")
        self.time = time() - self.time
        print(f"Polynomial before integral = {new_poly.to_string()}")
        if input(f"Answer was {new_poly.take_integral().to_string()} + C, Where you correct (y/n)") == "y":
            return True, self.time
        else:
            return False, self.time

    def ask_question(self):
        question_num = randint(1, 3)
        # was considering creating an array of question nums but that would make it weirder if a polynomial ever changed values
        if question_num == 1:
            return self.question_type_1()
        elif question_num == 2:
            return self.question_type_2()
        else:
            return self.question_type_3()


#just basic trig
class BasicTrig:
    def __init__(self, trig_func=None):
        if trig_func is None:
            trig_func = choice(trig_integral_functions)()
        self.time = 0
        self.trig_func = trig_func

    def ask_question(self):
        # asking to multiply two polynomials then include a trig func
        left = Polynomial(2)
        right = Polynomial(2)
        poly = left.multiply(right)
        full_func = AddedFunction(poly, self.trig_func)
        print(f"take the integral ({left.to_string()})({right.to_string()})+{self.trig_func.to_string()}")
        self.time = time()
        input("Press enter when finished")
        self.time = time() - self.time
        print(f"Function before integral = {full_func.to_string()}")
        if input(f"Answer was {full_func.take_integral().to_string()} + C, Where you correct (y/n)") == "y":
            return True, self.time
        else:
            return False, self.time

    def question_simple(self):
        poly = Polynomial(2)
        full_func = AddedFunction(poly, self.trig_func)
        print(f"take the integral ({poly.to_string()})+{self.trig_func.to_string()}")
        self.time = time()
        input("Press enter when finished")
        self.time = time() - self.time
        if input(f"Answer was {full_func.take_integral().to_string()} + C, Where you correct (y/n)") == "y":
            return True, self.time
        else:
            return False, self.time
