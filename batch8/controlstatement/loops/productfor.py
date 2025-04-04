print("Welcome To Product Dashboard")
times=int(input("Enter How many product You Want to Add: "))
for x in range(times):
    productname=str(input("Enter product name: "))
    productprice=float(input("Enter price of the product: "))
    
    print("Product:",productname)
    print("price:",productprice)
    print(f"{x+1} Product Add success")

