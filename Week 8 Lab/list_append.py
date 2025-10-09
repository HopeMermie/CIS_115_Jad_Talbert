#This program prompts the user to put an initial value that they can then decide if they would like to continue adding to or not through a defined function that loops if 'y'
list2 = []
list2.append(input('Input inital value: '))
def append_to_list():
    done = True
    while done:  
        prompt = input("Would you like to enter a value to append the list?(y or n): ")
        if prompt == 'y':
            list2.append(input('input var into list:'))
        elif prompt == 'n':
            print(f'{list2}')
            done = False
        else:
            print(f'error, printing list: {list2}')
            done = False
append_to_list()
