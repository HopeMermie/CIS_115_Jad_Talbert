#This program uses the input function to capture a credit card number

creditnumber = input('Enter credit card number: ')
creditdate = input('Enter expiration date (format mm/yy): ')
creditCVV = input('Enter CVV (found on the back of your card): ')

print (f'Your credit card number is {creditnumber}, your expiration date is {creditdate}, and your credit verification value {creditCVV}.')
