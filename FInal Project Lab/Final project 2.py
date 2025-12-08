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
    "Qty":0,
    "Description": "USB 128 GB drive.",
    "QtyonHand": 1000,
    },
    {
    "ProductID": 2,
    "SKU": "mbpro_490",
    "Price": 2900.00,
    "Qty":0,
    "Description": "Mac Book Pro 15 inch.",
    "QtyonHand": 45,
    },
    {
    "ProductID": 3,
    "SKU": "chip_1010",
    "Price": 48.00,
    "Qty":0,
    "Description": "Arduino microprocessor.",
    "QtyonHand": 325,
    },
    {
    "ProductID": 4,
    "SKU": "cam_78",
    "Price": 156.00,
    "Qty":0,
    "Description": "Ring Camera. Model 78.",
    "QtyonHand": 98,
    },
    {
    "ProductID": 5,
    "SKU": "smt_tv_100",
    "Price": 359.00,
    "Qty":0,
    "Description": "TCL Smart TV.",
    "QtyonHand": 225,
    }
]

product_cart = {
     1:0,
     2:0,
     3:0,
     4:0,
     5:0,
}
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
            affirm = input("Would you like to add a product to your cart (y or n)?: ")
            if affirm == "y":
                productlist = int(input("Choose a product ID from the product catalog to continue (1-5): "))
                product_found = False

                for items in products:
                    #validates if the item assigned to product id input is valid
                    if (items["ProductID"] == productlist):
                        #This prints the item information
                        print (items)
                        product_found = True

                        print(product_cart)

                    #Make sure they still want product before continuing

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
                if not product_found:
                    print ("Sorry, the product ID you are looking for is unavailable.")
            if affirm == "n":
                checkout = input("Would you like to check out (y or n)?: ")
                done = False
                if checkout == "y":
                    DONE = True
                    while DONE:
                        print(product_cart)
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
                        info_affirm = input("Does the information above look correct (y or n?): ")
                        if info_affirm == "y":
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
                                    done = False
                                else:
                                    print("Invalid credit card entered. Please try again.")
                        if info_affirm == "n":
                            print("Please correct information. ")
                if checkout == "n":
                    done = True
append_to_list()