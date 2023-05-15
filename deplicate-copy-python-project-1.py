def customer_info(id, name):
    print(f'Customer ID {id}')
    print(f'Customer Name {name}')
    # print(f'Customer Town code {town_code}')
    return 0

id = int(input('Please Your ID: '))
name = str(input('Please name: '))


def part_ordered_info(part_num, description,  oversize_order_status):
    print(f'Part Number : {part_num}')
    print(f'Description : {description}')
    # print(f'Price per part : {price_per_part}')
    # print(f'Quantity : {quantity}')
    print(f'Oversize order status : {oversize_order_status}')
    return 0

part_num = int(input('Enter part number: '))
description = str(input("Enter Description: "))
oversize_order_status = input("Enter status of yor order (y/n): ")

def cumpute_cost(price, quantity):
    cost = round(price * quantity,2)
    return cost

def sales_tax(customer_type, town_code, quantity):
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

def shipping_cost(shipping_charge, quantity):
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
shipping_charge = str(input('Enter Shipping Method (UPS, Fed Ex Overnight, US PostalAir, Fed Ex Ground): '))

def shipping_details(town_code, customer_type, shipping_charge, price_per_part, quantity):
    cost = cumpute_cost(price_per_part, quantity)
    print(f'Cost {cost}')
    sale_tax = sales_tax(customer_type, town_code, quantity)
    print(f'sales tax {sale_tax}')
    shipping_rate_cost = shipping_cost(shipping_charge, quantity)
    print(f'shipping cost {shipping_rate_cost}')
    total = shipping_rate_cost + sale_tax + cost
    print(f'Total: {total}')
    with open('total.txt', 'a') as file:
        file.write(str(total))
        
price_per_part = float(input('Enter price per part: '))
quantity = int(input("Enter quantity: "))
shipping_details(town_code, customer_type, shipping_charge, price_per_part, quantity)