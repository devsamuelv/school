import math

# option one
# made by samuel villegas
# 7/27/20 10:57 PM

itemNumber = 1
tax = 6
flat_shipping = 5

items = [
    {
        "name": "Sony DJ Headset",
        "price": "56.99"
    },

    {
        "name": "Razer Gaming Key Board",
        "price": "70.99"
    }
]

# print info
def printInfo(input):
    print("[info] " + str(input))

# count items in the json data
def countItems():
    count = 0

    # for each item in the json varible add 1 to the current count
    for i in items:
        count + 1

    # to make sure its an int
    return int(count)

# insert an object into the json data
def insert(data):
    item_count = countItems()

    items.insert(item_count + 1, data)

# create json data for each item
# for num in range(0, int(itemNumber)):
#     name = input("Enter the name of the item >> ")
#     price = input("Enter the price of the item >> ")

      # insert json function
#     insert({
#         "name": name,
#         "price": price 
#     })

    # printInfo(num)

# calulate tax
def calTax():
    return tax / 100

# calulate full price
def calFullPrice(price):
    return (float(price) + calTax()) + flat_shipping

# print data for each item in the json data
for i in items:
    # i.get("name") is to get the object name and i.get("price") is to get the price if the object
    print("Item: " + str(i.get("name")) + " Will cost: " + "$" + str(calFullPrice(float(i.get("price")))) + " to ship with tax")
