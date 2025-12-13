from Polynomial import Polynomial
from criticalNumbers import FindCriticalNumbers, FindInflection
from WordProblems import FenceRiver, FenceTwoSquares
from IntegralRuleProblems import BasicPowerRule
from radiusVolumeRates import SphereRate

a = Polynomial(2)
b = FindCriticalNumbers(2)
c = FindInflection(1)
d = FenceTwoSquares()
e = BasicPowerRule()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(e.ask_question())
    #b.ask_question()
    d.ask_question()
    c.ask_question()
    #initial_question = SphereRate()
    #print(initial_question.ask_question())
    Polynomial.generate_factorable(2)
    #print(a.to_string())
    #print(a.multiply().to_string())
