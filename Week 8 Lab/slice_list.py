#This program slices the month list, from position 4 to 6 using a defined function that returns and prints May and June. 
def slice_list():
    months = ["January", "Febuauary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    months = months[4:6]
    print (months)
    return months
slice_list()