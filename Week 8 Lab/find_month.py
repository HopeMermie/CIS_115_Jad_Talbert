
def search():
    months = ["January", "Febuauary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    search = input("Enter month: ")
    if (search) in months:
        print(f"We found {search} in the months list. Search successful!")
    else:
         print(f"We could not find {search} in the months list.")
search()