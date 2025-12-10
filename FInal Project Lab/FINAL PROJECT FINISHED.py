print("	--------------------------------------------------------------------")
print("	                           PRODUCT CATALOG")
print("	--------------------------------------------------------------------")
print("	1      |    USB Drive(128 GB)                           |   $12.00")
print("	2      |   Mac Book Pro(15 inch)                        |   $2900.00")
print("	3      |   Arduino 1010(with blue tooth)                |   $48.00")
print("	4      |   Ring Camera(wireless)                        |   $156.00")
print("	5      |   Smart TV(TCL 70 inch)                        |   $359.00")
print("	---------------------------------------------------------------------")

products = [
     {
    "ProductID": 1,
    "SKU": "usb_k981",
    "Price": 12.00,
    "Description": "USB 128 GB drive.",
    "QtyonHand": 1000,
    },
    {
    "ProductID": 2,
    "SKU": "mbpro_490",
    "Price": 2900.00,
    "Description": "Mac Book Pro 15 inch.",
    "QtyonHand": 45,
    },
    {
    "ProductID": 3,
    "SKU": "chip_1010",
    "Price": 48.00,
    "Description": "Arduino microprocessor.",
    "QtyonHand": 325,
    },
    {
    "ProductID": 4,
    "SKU": "cam_78",
    "Price": 156.00,
    "Description": "Ring Camera. Model 78.",
    "QtyonHand": 98,
    },
    {
    "ProductID": 5,
    "SKU": "smt_tv_100",
    "Price": 359.00,
    "Description": "TCL Smart TV.",
    "QtyonHand": 225,
    }
]

#The dictionary(cart) will be editted by user when adding products

product_cart = {
     1:0,
     2:0,
     3:0,
     4:0,
     5:0,
}


#The names and adresses dictionary will be editted by user after finalizing cart

names_and_adresses = {
    "firstname" : "{firstname}",
    "lastname" : '{lastname}',
    "city": '{city}',
    "state": '{state}',
    "zipcode": '{zipcode}',
    "phonenumber": '{phone}'}
def append_to_list():
    done = True
    while done: 
            #Ask if user would like to start
            affirm = input("Would you like to add a product to your cart (y or n)?: ")
            if affirm == "y":
                #Prompt a product they would like to add to cart
                productlist = int(input("Choose a product ID from the product catalog to continue (1-5): "))
                product_found = False

                for items in products:

                    #validates if the item assigned to product id input is valid

                    if (items["ProductID"] == productlist):
                        #This prints the item information
                        print (items)
                        product_found = True

                        print(product_cart)
                        
                    #Product 1

                        if affirm == "y":
                            if productlist==1:
                                Done = True
                                while Done:
                                    qtyList = int(input(f"Enter quantitiy for product {productlist} (Max 1000): "))
                                    if qtyList in range (1,1001):
                                        product_cart[1] += qtyList
                                        print(product_cart)
                                        Done = False
                                    else: 
                                        print("Invalid quantity, we do not have that many in stock.")

                    #Product 2

                            if productlist==2:
                                Done = True
                                while Done:
                                    qtyList = int(input(f"Enter quantitiy for product {productlist} (Max 45): "))
                                    if qtyList in range (1,46):
                                        product_cart[2] += qtyList
                                        print(product_cart)
                                        Done = False
                                    else: 
                                        print("Invalid quantity, we do not have that many in stock.")

                    #Product 3

                            if productlist==3:
                                Done = True
                                while Done:
                                    qtyList = int(input(f"Enter quantitiy for product {productlist} (Max 325): "))
                                    if qtyList in range (1,326):
                                        product_cart[3] += qtyList
                                        print(product_cart)
                                        Done = False
                                    else: 
                                        print("Invalid quantity, we do not have that many in stock.")

                    #Product 4

                            if productlist==4:
                                Done = True
                                while Done:
                                    qtyList = int(input(f"Enter quantitiy for product {productlist} (Max 98): "))
                                    if qtyList in range (1,99):
                                        product_cart[4] += qtyList
                                        print(product_cart)
                                        Done = False
                                    else: 
                                        print("Invalid quantity, we do not have that many in stock.")

                    #Product 5

                            if productlist==5:
                                Done = True
                                while Done:
                                    qtyList = int(input(f"Enter quantitiy for product {productlist} (Max 225): "))
                                    if qtyList in range (1,226):
                                        product_cart[5] += qtyList
                                        print(product_cart)
                                        Done = False
                                    else: 
                                        print("Invalid quantity, we do not have that many in stock.")
            i_total = 0
            for items in products:
                if items["ProductID"] in product_cart:
                    qtyList = product_cart[items["ProductID"]]
                    total = qtyList * items["Price"]
                    i_total += total
            print(f"Your total currently is ${i_total:.2f}")
            if affirm == "n":
                #Prompt user if they'd like to check out
                checkout = input("Would you like to check out (y or n)?: ")
                done = False
                if checkout == "y":
                    DONE = True
                    while DONE:
                        print(product_cart)
                        #Begin asking for billing information
                        firstname = input("Please enter your first name: ")
                        lastname = input("Please enter your last name: ")
                        address = input("Please enter your address: ")
                        city = input("Please enter you city: ")
                        state = input("Please enter your state: ")
                        zipcode = input("Please enter your zipcode: ")
                        email = input("Please enter your email: ")
                        phonenumber = input("Please enter your phone number: ")
                        names_and_adresses["firstname"] = firstname
                        names_and_adresses["lastname"] = lastname
                        names_and_adresses["address"] = address
                        names_and_adresses["city"] = city
                        names_and_adresses["state"] = state
                        names_and_adresses["zipcode"] = zipcode
                        names_and_adresses["email"] = email
                        names_and_adresses["phonenumber"] = phonenumber
                        print(names_and_adresses)
                        #Affirm if information is correct
                        info_affirm = input("Does the information above look correct (y or n?): ")
                        if info_affirm == "y":
                            #If correct ask for credit card information
                            DONE = False
                            done = True
                            while True:
                                ccNum = input("Please enter a credit card number to validate: ")
                                ccNum = ccNum [::-1]
                                total = 0
                                for i, digit in enumerate(ccNum):
                                    n = int(digit)
                                    if i % 2 == 1:
                                        n = n * 2
                                        if n > 9:
                                            n = n - 9
                                    total = total + n
                                if total % 10 == 0:
                                    print(f"The credit card {ccNum} is valid!")
                                    expdate = input("Enter the expiration date on your card: ")
                                    cvv = input("Please enter your CVV: ")
                                    print("----------------------------")
                                    print("-----Credit Information-----")
                                    print("----------------------------")
                                    print(f"Credit Card Number: {ccNum}")
                                    print(f"Expiration Date: {expdate}")
                                    print(f"CVV: {cvv}")
                                    print("----------------------------")

                                    #multiply quantity and price for each product for total here

                                    #add for each of that total 

                                    #After calculating both print receipt 
                                    print(" ")
                                    print("----------------------------------------------------------------------------------------")
                                    print("                              Billing/Shipping Information: ")
                                    print("----------------------------------------------------------------------------------------")
                                    print(" ")
                                    print(f"{firstname} {lastname} ")
                                    print(f"Address: {address}")
                                    print(f"City: {city}")
                                    print(f"State: {state}")
                                    print(f"Zip/Post Code: {zipcode}")
                                    print(f"Email: {email}")
                                    print(f"Phone: {phonenumber}")
                                    print(" ")
                                    print("----------------------------------------------------------------------------------------")
                                    print("                              Billing/Shipping Information: ")
                                    print("----------------------------------------------------------------------------------------")
                                    print(" ")
                                    print("****************************************************************************************")
                                    print(" SKU         Qty        Price       Description                                    Total")
                                    print("****************************************************************************************")
                                    for x in product_cart:
                                        if product_cart[x] > 0:
                                            qty = product_cart[x]
                                            price = products[x-1]["Price"]
                                            line_total = qty * price
                                            print(f"{products[x-1]['SKU']:12} {qty:<10} ${price:<10.2f} {products[x-1]['Description']:40} ${line_total:.2f}")
                                    print("****************************************************************************************")
                                    print(f"           Cart Total:{i_total:.2f}")
                                    done = False
                                    break
                                else:
                                    #If card doesnt pass MOD 10 check, loop to prompt another card number
                                    print("Invalid credit card entered. Please try again.")
                        if info_affirm == "n":
                            #If billing info is incorrect loop to prompt information
                            print("Please correct information. ")
                if checkout == "n":
                    #If user doesnt want to check out loop over the product 
                    done = True
append_to_list()