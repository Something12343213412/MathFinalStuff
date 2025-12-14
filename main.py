from Polynomial import Polynomial
from criticalNumbers import FindCriticalNumbers, FindInflection
from WordProblems import FenceRiver, FenceTwoSquares
from IntegralRuleProblems import BasicPowerRule
from FunctionOperations import MultipliedFunction, RealExponentFunction
from radiusVolumeRates import SphereRate

a = Polynomial(2)
b = Polynomial(2)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(a.to_string())
    print(b.to_string())
    c = MultipliedFunction(a, b)

    d = RealExponentFunction(c, 1.5)

