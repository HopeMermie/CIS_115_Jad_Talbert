#This program determines if the remainder of the division operation is odd or even

num1 = input('Enter first number: ')
num2 = input ('Enter second number: ')

modulo = int(num1)%int(num2)
 
if modulo:
    print (f'The remainder of the division operation {modulo} is even')
else:
    print ('The remainder of the division operation is odd')