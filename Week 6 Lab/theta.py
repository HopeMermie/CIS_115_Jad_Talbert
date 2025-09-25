#This program determines the angle of a right triangle using trigonometric functions
import math
X = int(input("Please enter the value of leg 1: "))
Y = int(input("Please enter the value of leg 2: "))

#Using our result, find theta
function = math.atan2(X,Y)
theta = 180/ int(math.pi)

def message():
    print(f"The angle theta for the right triangle is {theta} degrees.")
message()
