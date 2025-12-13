from Polynomial import Polynomial
from time import time

class FindCriticalNumbers:
    def __init__(self, num_terms):
        self.time = 0
        self.polynomial, self.factors = Polynomial.generate_factorable(num_terms)
        # integrating, doesn't change the math of the critical numbers or factors
        self.polynomial.take_integral()
        self.critical_nums = []
        # finding critical numbers based on factors
        for i in self.factors:
            self.critical_nums.append(f"{-1*i[1]}/{i[0]}")

    def get_info(self):
        print(self.polynomial.to_string())
        print(self.factors)
        print(self.critical_nums)

    def ask_question(self):
        #print(f" Find the critical numbers of {self.polynomial.to_string()}")
        start = time()
        answer = input(f" Find the critical numbers of {self.polynomial.to_string()}")
        end = time()
        self.time = end-start
        print(f"answer was x = {self.critical_nums}")
        return True, self.time

class FindInflection(FindCriticalNumbers):
    def __init__(self, num_terms):
        super().__init__(num_terms)
        self.polynomial.take_integral()

    def ask_question(self):
        start = time()
        answer = input(f" Find the points of inflection for {self.polynomial.to_string()}")
        end = time()
        self.time = end - start
        print(f"answer was x = {self.critical_nums}")
        return True, self.time
