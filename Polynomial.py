from Equation import Equation
from random import randint, choice

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

        print(self.terms)

        # sort by order
        self.terms.sort(key=lambda term: term[1], reverse=True)
        print(self.terms)

    def take_out_zeros_coef(self):
        for i in self.terms:
            if i[0] == 0:
                self.terms.remove(i)

    def to_string(self):
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
