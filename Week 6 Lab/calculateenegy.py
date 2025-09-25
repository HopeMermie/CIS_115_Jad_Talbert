#This program calculates the energu in Joules
mass = input("Please enter your mass: ")
c = float(2.99)*float(10**8)
e = float(mass)*float(c)**2

def calculate_energy():
    print(f"The energy produced is {e} Joules")
calculate_energy()