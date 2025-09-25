import math
def message1():
    x = input("Please enter the value of leg 1: ")
    y = input("Please enter the value of leg 2: ")
    message2()
def message2():
    c = float(x**2)+float(y**2)
    result = math.sqrt (c)
    print(f"The hypoteneuse of the right-triangle is {result} ")

message1()