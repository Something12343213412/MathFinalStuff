# file exists to avoid circular imports lmao
from Function import Function
# have to move polynomial into here because of circular imports
from random import randint, choice
from copy import deepcopy

# in here bc of circ imports, the code is maximal spaghetti
# region polynomial
# possible exponents that can be chosen, more positive which means more likely a positive number will be gotten
#exponent_list = [4, 3.5, 3, 2.5, 2, 1.5, 1, .5, 0, -.5, -1, -1.5, -2]
exponent_list = [1, 2, 3, 4, 5]
# do not try to understand this class, this is the most spaghetti thing I wrote before I made the rest of the infastructure
class Polynomial(Function):
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
            if not i[0] == 1:
                output += f"{i[0]}".removesuffix(".0")
            # making output more readable
            if not i[1] == 0:
                output += "x"
                if not i[1] == 1:
                    output += f"^{i[1]}".removesuffix(".0")

            #print(f"i is = ", i)
            #special case if it is just 1
            if i == [1, 0]:
                output += "1"
            # putting + sign if index is not last
            if self.terms.index(i) < len(self.terms)-1:
                output += " + "


            """
            # don't put + sign if at the end
            if self.terms.index(i) == len(self.terms)-1:
                # checking if exp is 0
                if i[1] == 0:
                    output = output + f"{i[0]}"
                elif i[1] == 1:
                    output += f"{i[0]}x"
                else:
                    output = output + f"{i[0]}x^{i[1]}"
            else:
                if i[1] == 0:
                    output = output + f"{i[0]} + "
                elif i[1] == 1:
                    output += f"{i[0]}x + "
                else:
                    output = output + f"{i[0]}x^{i[1]} + "
            """
        return output

    def take_derivative(self):
        # need to use deep copy bc needs to create a copy as don't want to actually change the data of the og poly
        new_poly = deepcopy(self)
        # removing zeros beforehand so no issues will happen with .length
        for i in self.terms:
            if i[1] == 0:
                new_poly.terms.remove(i)

        for i in range(0, len(new_poly.terms)):
            # separating for readability
            term = new_poly.terms[i]
            new_coef = term[0] * (term[1])
            new_exp = term[1] - 1
            new_poly.terms[i] = [new_coef, new_exp]

        return new_poly

    # exists to have a tool to prevent /0 errors that come from the exponent of -1
    # ln solution will be in a different type of poly
    def remove_power(self, power):
        for i in self.terms:
            if i[1] == power:
                self.terms.remove(i)

    def take_integral(self, c=None):
        new_poly = self
        for i in range(0, len(self.terms)):
            term = new_poly.terms[i]
            new_coef = term[0] / (term[1]+1)
            new_exp = term[1] + 1
            new_poly.terms[i] = [new_coef, new_exp]

        if c is not None:
            new_poly.terms.append([c, 0])

        return new_poly

    def evaluate(self, x):
        output = 0
        for i in self.terms:
            output += i[0]*(x**i[1])
        return output

    # multiplies a factor to the polynomial. Factor format [ceof x, + num]
    def multiply_factor(self, factor=[5, 3]):
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

    # multiplies a specific term, here to make multiply code look cleaner
    def multiply_term(self, coef=1, exponent=1):
        new_terms = {}
        for i in self.terms:
            #multiply coef and add exponents
            new_terms[i[1] + exponent] = i[0]*coef
        return Polynomial(len(list(new_terms.keys())), list(new_terms.values()), list(new_terms.keys()))

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

    # have to put these here bc base func operations relies on this so oh well
    def multiply(self, other: Function = None):
        new_poly = Polynomial(0, [], [])
        if other.__class__ == Polynomial:
            for i in other.terms:
                multiplied_terms = self.multiply_term(i[0], i[1])
                #print(f"multiplied terms {multiplied_terms.to_string()}")
                new_poly = new_poly.add(multiplied_terms)
            return new_poly

        return MultipliedFunction(self, other)

    # can't simplify as can't do simple exponent operations
    def divide(self, other: Function = None):
        return MultipliedFunction(self, RealExponentFunction(other, -1))

    def add(self, other: Function = None):
        if other.__class__ == Polynomial:
            exponents = {}
            terms = self.terms + other.terms
            #print(f"terms when adding {terms}")
            # need to combine like terms
            for i in terms:
                if i[1] in exponents:
                    exponents[i[1]] += i[0]
                else:
                    exponents[i[1]] = i[0]
            return Polynomial(len(exponents.keys()), list(exponents.values()), list(exponents.keys()))
        return AddedFunction(self, other)

    def subtract(self, other=None):
        return AddedFunction(self, MultipliedFunction(negative_one, other))

    def raise_exp(self, num=None):
        return RealExponentFunction(self, num)

# endregion


# declaring a constant just for ease as it is used in each subtraction formula
negative_one = Polynomial(1, [-1], [0])
positive_one = Polynomial(1, [1], [0])

# purely for inheritance purposes, contains all basic func operations
class BasicFuncOperations(Function):
    def __init__(self):
        super().__init__()

    def multiply(self, other: Function = None):
        return MultipliedFunction(self, other)

    def divide(self, other: Function = None):
        return MultipliedFunction(self, RealExponentFunction(other, -1))

    def add(self, other=None):
        return AddedFunction(self, other)

    def subtract(self, other=None):
        return AddedFunction(self, MultipliedFunction(negative_one, other))

    def raise_exp(self, num=None):
        return RealExponentFunction(self, num)

#when one needs to add two functions
class AddedFunction(BasicFuncOperations):
    def __init__(self, left: Function, right: Function):
        super().__init__()
        self.left = left
        self.right = right

    def evaluate(self, x):
        return self.left.evaluate(x) + self.right.evaluate(x)

    def to_string(self):
        return f"({self.left.to_string()} + {self.right.to_string()})"

    # just separates it into two integrals
    def take_integral(self):
        return AddedFunction(self.left.take_integral(), self.right.take_integral())

    # just takes two separate derivatives
    def take_derivative(self):
        return AddedFunction(self.left.take_derivative(), self.right.take_derivative())

    # creates an added function of new multiplied Functions
    def multiply(self, other: Function = None):
        left = MultipliedFunction(self.left, other)
        right = MultipliedFunction(self.right, other)
        return AddedFunction(left, right)

    def divide(self, other: Function = None):
        left = MultipliedFunction(self.left, RealExponentFunction(other, -1))
        right = MultipliedFunction(self.right, RealExponentFunction(other, -1))
        return left, right

# Exist when one needs to multiply two functions
class MultipliedFunction(BasicFuncOperations):
    def __init__(self, left: Function, right: Function):
        super().__init__()
        self.left = left
        self.right = right

    def evaluate(self, x):
        return self.left.evaluate(x)*self.right.evaluate(x)

    def to_string(self):
        return f"({self.left.to_string()})({self.right.to_string()})"

    # don't even try lmao
    def take_integral(self):
        return None

    def take_derivative(self):
        #create new left as dv*u + v*du
        #print(f"left before is {self.left.to_string()}")
        left = MultipliedFunction(self.left.take_derivative(), self.right)
        right = MultipliedFunction(self.left, self.right.take_derivative())
        #print(f"Left is {left.to_string()}, right is {right.to_string()}")
        # combining both with new multiplied function
        return AddedFunction(left, right)

# A function raised to a real number power
class RealExponentFunction(BasicFuncOperations):
    def __init__(self, inside: Function, exponent: float):
        super().__init__()
        self.inside = inside
        self.exponent = exponent

    def evaluate(self, x):
        return self.inside.evaluate(x)**self.exponent

    def to_string(self):
        return f"({self.inside.to_string()})^{self.exponent}"

    # assumes form of f(u)du, very restricted
    def take_integral(self):
        # adding 1 to the exponent
        new_exp = self.exponent+1
        # creates exponent^-1 in the form of a polynomial
        coef = Polynomial(1, [new_exp**(-1)], [0])
        # takes the original function and multiplies it by the coef found earlier
        inside = MultipliedFunction(self.inside, coef)
        # return the function with the nex exp
        return RealExponentFunction(inside, new_exp)

    # assumes d/dx[f(g(x))] = df(g(x))*dg(x), could be infinite composition
    def take_derivative(self):
        # d/dx x^n = nx^(...)
        coef = Polynomial(1, [self.exponent], [0])
        # d/dx x^n = nx^(n-1)
        new_exp = self.exponent-1
        # d/dx f(x)^n = nf(x)^...*...
        inside = MultipliedFunction(self.inside, coef)
        # d/dx f(x)^n = nf(x)^(n-1)*...
        left = RealExponentFunction(inside, new_exp)
        # d/dx f(x)^n = ...*d/dx f(x)
        right = self.inside.take_derivative()
        # d/dx f(x)^n = nf(x)^(n-1)*df(x)
        return MultipliedFunction(left, right)

    def raise_exp(self, num=None):
        new_exp = self.exponent + num
        # basically just adding exponents to make it a bit more clean
        return RealExponentFunction(self.inside, new_exp)
