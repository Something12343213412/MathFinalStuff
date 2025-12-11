from Polynomial import Polynomial

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.


a = Polynomial(6)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(a.to_string())
    a.take_derivative()
    print(a.to_string())
    a.take_integral(4)
    print(a.to_string())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
