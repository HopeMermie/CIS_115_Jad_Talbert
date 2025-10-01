    
def kinetic_energy():
    m = input("Please enter your mass: ")
    v = input("Please enter your velocity: ")
    KE = .5 * float(m) * float(v)**2
    print(f"The kenetic energy is {KE}.")
kinetic_energy()