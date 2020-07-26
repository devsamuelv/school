items = {
    {
        "name": input("Enter the item name >> "),
        "price": input("Enter the item price >> ")
    },

    {
        "name": input("Enter the item name >> "),
        "price": input("Enter the item price >> ")
    }
}

tax = 6
shipping = 5.99

def calTax():
    return tax / 100 

def calFullPrice(price: float):
    return round(shipping + (float(price) + (calTax() * float(price))))

for item in items:
    print(item.price)

for item in items:
    print(calFullPrice(float(item.price)))
