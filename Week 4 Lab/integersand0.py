#This program determines the less or greater value of an interger with 0

num1 = input ("Enter first number: ")
num2 = input ("Enter Second number: ")
num3 = input ("Enter third number: ")

sum = int(num1)+int(num2)
quotent = sum/int(num3)

if quotent > 0:
    print (f"The mathematical operation {quotent} is > 0")
else:
    print (f"The mathematical operation {quotent} is < = 0")