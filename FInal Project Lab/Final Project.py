# Week 15: Fix loop error, link credit card stuff
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
    "SKU": "cam_78",
    "Price": 48.00,
    "Qty":0,
    "Description": "Arduino microprocessor.",
    "QtyonHand": 98,
    },
    {
    "ProductID": 4,
    "SKU": "chip_1010",
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

product_cart = {}
def getproduct(pid):
    for p in products:
        if p["ProductID"] == pid:
            return p
    return None
def append_to_list():
    done = True
    while done:  
        try:
            productlist = input("Choose a product ID from the product catalog to continue (1-5): ")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 5.")
            continue
        
        qtyList = int(input(f"Enter quantitiy for product {productlist}: "))
        if productlist in product_cart: 
            product_cart[productlist] += qtyList
        else:
            product_cart[productlist] = qtyList
        prompt = input("Would you like to add another product (y or n?): ")
        if prompt == "y":
            productlist = (input("choose a product ID from the product catalog to conintue: "))
        elif prompt == 'n':
            Check = input("Are you ready to check out (y or n?): ")
            while Check != "y" and Check != "n":
                Check = input("Please enter 'y' for Yes or 'n' No: ")
                if Check == "y":
                    print("Enter your billing/shipping information below: ")
                    firstname = input("Please enter your first name: ")
                    lastname = input("Please enter your last name: ")
                    city = input("Please enter you city: ")
                    state = input("Please enter your state: ")
                    zipcode = input("Please enter your zipcode: ")
                    phonenumber = input("Please enter your phone number: ")
                    break
append_to_list()

names_and_adresses = {
    "firstname" : "{firstname}",
    "lastname" : '{lastname}',
    "city": '{city}',
    "state": '{state}',
    "zipcode": '{zipcode}',
    "phonenumber": '{phone}'}
def print_dictionary():
    print(f"{names_and_adresses}")
print_dictionary()

def validateCreditCard(ccNum):
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
       return True
    else:
       return False
def main():
   while True:
      ccNum = input("Please enter a credit card number to validate: ")

      if validateCreditCard(ccNum):
         print(f"The credit card {ccNum} is valid!")
         break 
      else:
         print("Invalid credit card entered. Please try again.")
main()