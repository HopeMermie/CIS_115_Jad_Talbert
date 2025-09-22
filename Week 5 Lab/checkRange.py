#This program allows a user to enter a value up to 100, if the go over however it will tell them.


x = input("Please enter an integer value between the range of 0 and 100: ")
int1 = 0
int2 = 100
y = int(x)
while int(int1) < int(x) < int(int2):
    x = input("Please enter an integer value between the range of 0 and 100: ")
    int1 = 0
    int2 = 100
    y = int(x)
else: 
    print("Sorry, the number you entered is out of range!")
