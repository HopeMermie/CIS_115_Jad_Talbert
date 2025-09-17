#This program allows a user to enter up to 10 grades

count = 0
numOfGrades = int(input("How many grades would you like to enter?: "))

while count < numOfGrades:
    count = count + 1 
    grade = int(input("Enter your grade: "))
    print = (f"You entered {grade}")
    if (count >= numOfGrades):
        print (f"The user enetered {numOfGrades} grades and is done.")