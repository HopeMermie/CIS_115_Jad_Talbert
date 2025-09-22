#This prgram calculates tax and prints the item price, sales tax and total cost of the item

tax = .0725
product = 75.34

salestax = float(product) * float(tax)
totalcost = float(product) + float(salestax)

print(f"The item price before tax is {product}")
print(f"The sales tax is {salestax}")
print(f"The total cost of the product is {totalcost:,.2f}")