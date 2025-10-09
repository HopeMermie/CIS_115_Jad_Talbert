#This program uses a defined function to search for a desired month inputed by user. When written, if there is the word written in the list- it will be successful. However, whatever else is written will resilt in no result and print that. 
def search():
    months = ["January", "Febuauary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    search = input("Enter month: ")
    if (search) in months:
        print(f"We found {search} in the months list. Search successful!")
    else:
         print(f"We could not find {search} in the months list.")
search()