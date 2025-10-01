#This program determines which inputed number is the greater integer through a called function that also uses "If/Else" logic to determine. 
def max():
    num1 = int(input("Please enter first number: "))
    num2 = int(input ("Please enter second number: "))
    if num1 > num2:
        print(f" {num1} is the greater number.")
    else:
        print(f"{num2} is the greater number.")
max()