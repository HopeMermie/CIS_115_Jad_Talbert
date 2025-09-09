#This program determines the less or greater value of an interger with 0

num1 = input ("Enter first number: ")
num2 = input ("Enter second number: ")
value = int(num1)-int(num2)

if value <=0:
    print (" #####################################")
    print (f" Invalid! The value {value} is less than zero ")
    print (" #####################################")
else:
    print ("The values entered were valid integers")