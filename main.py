from criticalNumbers import FindCriticalNumbers, FindInflection
from WordProblems import FenceRiver, FenceTwoSquares
from IntegralRuleProblems import BasicPowerRule
from FunctionOperations import *
from Trig import *
from radiusVolumeRates import SphereRate

a = Polynomial(3)
#b = Polynomial(2)
#c = Polynomial(2)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(a.to_string())
    d = Cos(inside=a, coef=2)
    e = Tan(inside=a, coef=2)
    print(d.to_string())
    print(d.take_derivative().to_string())
    print(e.to_string())
    print(e.take_derivative().to_string())
