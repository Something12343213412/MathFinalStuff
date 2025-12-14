from criticalNumbers import FindCriticalNumbers, FindInflection
from WordProblems import FenceRiver, FenceTwoSquares
from IntegralRuleProblems import BasicPowerRule
from FunctionOperations import *
from radiusVolumeRates import SphereRate

a = Polynomial(2)
b = Polynomial(2)
c = Polynomial(2)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(a.to_string())
    print(b.to_string())
    print(c.to_string())

    d = MultipliedFunction(a.add(c), b)

    e = RealExponentFunction(d, 2)
    print(f"a = {a.evaluate(3)}, b = {b.evaluate(3)}, c = {c.evaluate(3)}, d = {d.evaluate(3)}, e = {e.evaluate(3)}")
    print(f"a+c = {a.add(c).evaluate(3)}")

