
def message():
    mass = input("3")
    c = input("2.99 * 10**8")
    calculate_energy()

def calculate_energy():
    joules = float(mass)*float(c)
    print("The energy in joules produce based off of a mass of {1} and the equation {2} is {3}}".format(mass, c, joules))
message()