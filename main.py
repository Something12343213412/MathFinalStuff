from criticalNumbers import FindCriticalNumbers, FindInflection
from WordProblems import FenceRiver, FenceTwoSquares
from IntegralRuleProblems import BasicPowerRule
from FunctionOperations import *
from Trig import *
from radiusVolumeRates import SphereRate

a = Polynomial(3)
b = SecSquared(a)
#b = Polynomial(2)
#c = Polynomial(2)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(b.to_string())
    print(b.take_integral().to_string())
