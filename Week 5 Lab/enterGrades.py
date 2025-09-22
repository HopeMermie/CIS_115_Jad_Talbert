#This program allows a user to enter up to 10 grades

numberofgrades = int(input("Enter up to 10 grades: "))
n=0
print(f"{numberofgrades}")

while n < numberofgrades:
    n=n+1
    grades = int(input("Enter grade: "))
    print(f'{grades}')
if n>=numberofgrades:
    print(f"You have entered {numberofgrades} grades.")