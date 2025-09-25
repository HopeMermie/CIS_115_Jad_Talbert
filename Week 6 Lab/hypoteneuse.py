#This program determines the hypotenuse of a right-triangle using the Pathagroean Theorem
import math
X = input("Please enter the value of leg 1: ")
Y = input("Please enter the value of leg 2: ")
c = float(X)**2+float(Y)**2
result = math.sqrt (c)

def message1():
    print(f"The hypoteneuse of the right-triangle is {result} ")
message1()