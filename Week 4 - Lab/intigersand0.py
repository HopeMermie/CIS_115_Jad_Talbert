num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

sum = int (num1) + int (num2)
print("The sum of {0} and {1} is {3}".format(num1,num2,sum))

quotent = int (sum) / int (num3)
print('The quotent of {3} and {2} is {4}'.format(sum,num3,quotent))

if quotent >0:
    print ("The mathematical operation is > 0")
else:
    print ("The mathematical operation is < = 0")