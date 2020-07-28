import math
import json

itemNumber = 1 # input("Number of items >> ")
tax = 6
flat_shipping = 5

items = [
        
]

def printInfo(input):
    print("[info]:: " + str(input))

def countItems():
    count = 0

    for i in items:
        count + 1

    # to make sure its an int
    return int(count)

def insert(data):
    item_count = countItems()

    items.insert(item_count + 1, data)

# create json data for each item

for num in range(0, int(itemNumber)):
    name = input("Enter the name of the item >> ")
    price = input("Enter the price of the item >> ")

    insert({
        "name": name,
        "price": price 
    })

    # printInfo(num)

def calTax():
    return tax / 100

def calFullPrice(price: float):
    return (price + calTax()) + flat_shipping

for i in items:
    print("Item: " + str(i.get("name")) + " Will cost: " + "$" + str(calFullPrice(float(i.get("price")))) + " to ship with tax")
