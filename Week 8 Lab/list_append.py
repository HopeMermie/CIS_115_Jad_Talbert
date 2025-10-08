
list2 = []
def append_to_list():
    done = True
    while done:  
        prompt = input("Would you like to enter a value to append the yest?(y or n): ")
        if prompt == 'y':
            list2.append(input('input var into list:'))
        elif prompt == 'n':
            print(f'{list2}')
            done = False
        else:
            print(f'error, printing list: {list2}')
            done = False
append_to_list()
