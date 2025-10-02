#This program returns the kinetic energy ina define function that asks for user input of mass and velocity
def kinetic_energy():
    m = float(input("Please enter your mass: "))
    v = float(input("Please enter your velocity: "))
    KE = .5 * (m) * (v)**2
    print(f"The kenetic energy is {KE}.")
    return KE
kinetic_energy()