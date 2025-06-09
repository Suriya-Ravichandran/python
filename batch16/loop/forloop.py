# data=["hello","world","foo"]

# for x in range(len(data)):
#     print(x)


# for x in data:
#     print(x)

hmp=int(input("Enter How many product you want to add:"))

for x in range(hmp):
    pname=str(input("Enter product name: "))
    price=float(input("Enter price: "))
    quantity=int(input("Enter quantity: "))
    print(f"product name: {pname}")
    print(f"price: {price}")
    print(f"quantity: {quantity}")
    print(f"Add {x+1} product success ")