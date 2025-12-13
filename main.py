from Polynomial import Polynomial
from criticalNumbers import FindCriticalNumbers, FindInflection
from radiusVolumeRates import SphereRate

a = Polynomial(2)
b = FindCriticalNumbers(2)
c = FindInflection(1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #b.ask_question()
    c.ask_question()
    #initial_question = SphereRate()
    #print(initial_question.ask_question())
    Polynomial.generate_factorable(2)
    #print(a.to_string())
    #print(a.multiply().to_string())
