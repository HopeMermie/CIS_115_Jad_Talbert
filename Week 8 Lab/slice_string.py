#This program takes a defined function that prompts the user to input positions in which they would slice the list. It should be 0 to 3. 
String_Value_1 = int(input("Please enter first string value: "))
String_Value_2 = int(input("Please enter second string value: "))
def slice_my_string():
    numbers = ['0','1','2','3','4','5']
    my_list = numbers [String_Value_1:String_Value_2]
    print(my_list)
    return my_list
slice_my_string()