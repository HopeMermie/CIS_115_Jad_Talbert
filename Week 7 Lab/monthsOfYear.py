#This program assigns specific parts of a list to desired user input to then return.
start = int(-1) + int(input("Please enter the number of desired starting month: "))
end = int(input("Please enter the the number of desired ending month: "))
def months_of_year(): 
    months = ["January", "Febuauary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print(f"{months[start: end]}")
months_of_year()