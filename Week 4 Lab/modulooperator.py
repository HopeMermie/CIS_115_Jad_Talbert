#This program determines if the remainder of the division operation is odd or even

num1 = input('Enter first number: ')
num2 = input ('Enter second number: ')

modulo = int(num1)%int(num2)
 
if modulo ==0:
    print ('The remainder of the division operation is even')
else:
    print ('The remainder of the division operation is odd')