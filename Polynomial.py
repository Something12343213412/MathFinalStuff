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
            for i in range(0, num_terms-1):
                coefficients.append(randint(-4, 4))

        if exponents is None:
            exponents = []
            # creating temp list so we can remove terms
            temp_exp_list = exponent_list
            for i in range(0, num_terms-1):
                exp_chosen = choice(temp_exp_list)
                # so we don't get repeats
                temp_exp_list.remove(exp_chosen)
                exponents.append(exp_chosen)

        for i in range(0, num_terms-1):
            # append an array with first index of coefficient and second of exponent
            self.terms.append([coefficients[i], exponents[i]])

        print(self.terms)

        # sort by order
        self.terms.sort(key=lambda term: term[1], reverse=True)
        print(self.terms)

    def to_string(self):
        output = ""
        # probably could make more efficient using something like join but oh well
        for i in self.terms:
            # don't put + sign if at the end
            if self.terms.index(i) == len(self.terms)-1:
                output = output + f" {i[0]}x^{i[1]}"
            else:
                output = output + f" {i[0]}x^{i[1]} +"

        return output
