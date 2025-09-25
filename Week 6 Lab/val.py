#This program reverses string
def print_iterations():
    val = int(input("Please enter loop amount: "))
    for num in range(val):
        print (num)
    print("The function call looped {0} times.".format(val))
print_iterations()