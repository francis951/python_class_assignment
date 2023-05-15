#capturing the custommer detailed
def customer_info(id, name):
    print(f'Customer ID {id}')
    print(f'Customer Name {name}')
    # print(f'Customer Town code {town_code}')
    return 0

id = int(input('Please Your ID: '))
name = str(input('Please name: '))

#prompting user for the ordered parts
def part_ordered_info(part_num, description, price_per_part, quantity, oversize_order_status):
    print(f'Part Number : {part_num}')
    print(f'Description : {description}')
    print(f'Price per part : {price_per_part}')
    print(f'Quantity : {quantity}')
    print(f'Oversize order status : {oversize_order_status}')
    return 0

part_num = int(input('Enter part number: '))
description = str(input("Enter Description: "))
price_per_part = float(input('Enter price per part: '))
quantity = int(input("Enter quantity: "))
oversize_order_status = input("Enter status of your order (y/n): ")

#compute for the cost
def cumpute_cost(price, quantity):
    cost = round(price * quantity,2)
    return cost
#calculates for sales cost
def sales_tax(customer_type, town_code, price_per_part, quantity):
    # sale_tax
    if customer_type == 'ret':
        sale_tax = 0
    elif town_code == "KLA":
        sale_tax = (0.1 * price_per_part * quantity)
    elif town_code == 'EBB' or town_code == 'MBR':
        sale_tax = round(0.5 * price_per_part * quantity)
    else:
        sale_tax = 0
    return sale_tax

town_code = str(input('Enter Town code (EBB, KLA, MBR): '))
customer_type = str(input('Enter Customer Type("ret" for RETAIL or "who" for WHOLESALE): '))

#computes for the shipping cost
def shipping_cost(shipping_charge, price_per_part, quantity):
    if shipping_charge == 'UPS':
        charge_per_part = 7.00
    elif shipping_charge == 'US PostalAir':
        charge_per_part = 8.50
    elif shipping_charge == 'Fed Ex Ground':
        charge_per_part = 9.25
    elif shipping_charge == 'Fed Ex Overnight':
        charge_per_part = 12.00
    shipping_rate_cost = round(charge_per_part * price_per_part * quantity, 2)
    return shipping_rate_cost

#prompting User
shipping_charge = str(input('Enter Shipping Method (UPS, Fed Ex Overnight, US PostalAir, Fed Ex Ground): '))

#the output of the system
def shipping_details(town_code, customer_type, shipping_charge, price_per_part, quantity):
    cost = cumpute_cost(price_per_part, quantity)
    print(f'Cost {cost}')
    sale_tax = sales_tax(customer_type, town_code, price_per_part, quantity)
    print(f'sales tax {sale_tax}')
    shipping_rate_cost = shipping_cost(shipping_charge, price_per_part, quantity)
    print(f'shipping cost {shipping_rate_cost}')
    total = shipping_rate_cost + sale_tax + cost
    print(f'Total: {total}')
    with open('total.txt', 'a') as file:
        file.write(str(total))
        
#prompting User to Enter name, Id
customer_info(id, name)
#calling a function for the part_order_inf()
part_ordered_info(part_num, description, price_per_part, quantity, oversize_order_status)
#Calling shipping details
shipping_details(town_code, customer_type, shipping_charge, price_per_part, quantity)

# In Python, a function is a block of reusable code that performs a specific task. 
# It is a self-contained unit of code that can be called from other parts of the program to perform a particular operation.

# Functions can take arguments (also known as parameters) as input and may return a value as output. 
# They can also be defined with no arguments or return value.

# Functions are a fundamental concept in Python and are used extensively in the language. 
# They make it possible to break down a complex problem into smaller, more manageable tasks, 
# improving code organization, and making it easier to maintain, test, and reuse code.