from Equation import Equation
from random import randint, choice
from math import exp

# possible exponents that can be chosen, more positive which means more likely a positive number will be gotten
exponent_list = [4, 3.5, 3, 2.5, 2, 1.5, 1, .5, 0, -.5, -1, -1.5, -2]

class Polynomial(Equation):
    def __init__(self, num_terms: int, coefficients=None, exponents=None):
        self.terms = []
        super().__init__()
        # if no input given generate random coefficient
        if coefficients is None:
            coefficients = []
            for i in range(0, num_terms):
                coef = randint(-4, 4)
                if coef == 0:
                    # force generate positive if 0 case
                    coef = randint(1,4)
                coefficients.append(coef)

        if exponents is None:
            exponents = []
            # creating temp list so we can remove terms
            temp_exp_list = exponent_list
            for i in range(0, num_terms):
                exp_chosen = choice(temp_exp_list)
                # so we don't get repeats
                temp_exp_list.remove(exp_chosen)
                exponents.append(exp_chosen)

        for i in range(0, num_terms):
            # append an array with first index of coefficient and second of exponent
            self.terms.append([coefficients[i], exponents[i]])

        # sort by order
        self.terms.sort(key=lambda term: term[1], reverse=True)

    def take_out_zeros_coef(self):
        for i in self.terms:
            if i[0] == 0:
                self.terms.remove(i)

    def to_string(self):
        # sort by order
        self.terms.sort(key=lambda term: term[1], reverse=True)
        output = ""
        # probably could make more efficient using something like join but oh well
        for i in self.terms:
            # don't put + sign if at the end
            if self.terms.index(i) == len(self.terms)-1:
                # checking if exp is 0
                if i[1] == 0:
                    output = output + f" {i[0]}"
                else:
                    output = output + f" {i[0]}x^{i[1]}"
            else:
                if i[1] == 0:
                    output = output + f" {i[0]} +"
                else:
                    output = output + f" {i[0]}x^{i[1]} +"

        return output

    def take_derivative(self):
        # removing zeros beforehand so no issues will happen with .length
        for i in self.terms:
            if i[1] == 0:
                self.terms.remove(i)

        for i in range(0, len(self.terms)):
            # separating for readability
            term = self.terms[i]
            new_coef = term[0] * (term[1])
            new_exp = term[1] - 1
            self.terms[i] = [new_coef, new_exp]

        return self

    # exists to have a tool to prevent /0 errors that come from the exponent of -1
    # ln solution will be in a different type of poly
    def remove_power(self, power):
        for i in self.terms:
            if i[1] == power:
                self.terms.remove(i)

    def take_integral(self, c=None):
        output = ""
        for i in range(0, len(self.terms)):
            term = self.terms[i]
            new_coef = term[0] / (term[1]+1)
            new_exp = term[1] + 1
            self.terms[i] = [new_coef, new_exp]

        if c is not None:
            self.terms.append([c, 0])

        return self

    def evaluate(self, x):
        output = 0
        for i in self.terms:
            output += i[0]*(x**i[1])
        return output

    # multiplies a factor to the polynomial. Factor format [ceof x, + num]
    def multiply(self, factor=[5, 3]):
        new_terms = []
        # Loops through each term
        for i in self.terms:
            new_coef = i[0]*factor[0]
            new_exp = i[1] + 1
            new_terms.append([new_coef, new_exp])
            # next term
            new_coef = i[0]*factor[1]
            new_exp = i[1]
            new_terms.append([new_coef, new_exp])
            # having list be long just to account for any possible issues that could come
            new_poly = Polynomial(len(new_terms), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            new_poly.terms = new_terms
        return new_poly

    # takes in a number and decreases each number by that
    def divide_by_x(self, number):
        # I think looping through an array directly would cause me to not be able to change the memory so doing this
        for i in range(0, len(self.terms)):
            self.terms[i][1] -= number

    @staticmethod
    def generate_factorable(num_factors):
        factors = []
        # polynomial of coef 1 and exp 0, just 1
        new_poly = Polynomial(1, [1], [0])
        for i in range(0, num_factors):
            factor = [randint(1, 3), randint(-2, 2)]
            # storing for future printing out / checking
            factors.append(factor)
            #
            new_poly = new_poly.multiply(factor)

        # a dictionary with each key being an exponent and the value being the coefficient
        exps = {}

        # need to combine like terms
        for i in new_poly.terms:
            if i[1] in exps:
                exps[i[1]] += i[0]
            else:
                exps[i[1]] = i[0]

        new_poly = Polynomial(len(exps.keys()), list(exps.values()), list(exps.keys()))
        #print(new_poly.to_string())
        #print(factors)
        return new_poly, factors
