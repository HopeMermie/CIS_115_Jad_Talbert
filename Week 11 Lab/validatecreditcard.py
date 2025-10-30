#
def validateCreditCard(ccNum):
    ccNum = ccNum [::-1]
    total = 0
    for i, digit in enumerate(ccNum):
       n = int(digit)
       if i % 2 == 1:
          n = n * 2
          if n > 9:
             n = n - 9
       total = total + n
    if total % 10 == 0:
       return True
    else:
       return False
def main():
   while True:
      ccNum = input("Please enter a credit card number to validate: ")

      if validateCreditCard(ccNum):
         print(f"The credit card {ccNum} is valid!")
         break 
      else:
         print("Invalid credit card entered. Please try again.")
main()