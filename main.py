from criticalNumbers import FindCriticalNumbers, FindInflection
from WordProblems import FenceRiver, FenceTwoSquares
from IntegralRuleProblems import BasicPowerRule
from FunctionOperations import *
from Trig import *
from radiusVolumeRates import SphereRate

a = Polynomial(3)
b = CscSquared(a)
c = Tan()
#b = Polynomial(2)
#c = Polynomial(2)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f"c deriv = {c.take_derivative().to_string()}")
    d = c.take_derivative()
    print(c.take_derivative().take_integral().to_string())
    print(c.find_definite_integral(.3, .2))
    print(a.to_string())
    print(a.find_definite_integral(.2, .3))
