print("Welcome To Product Dashboard")
while True:
    print("1 to add product\n2 to exit")
    choice=int(input("Enter Your choice: "))
    if choice==1:
        productname=str(input("Enter product name: "))
        productprice=float(input("Enter price of the product: "))
        print("Product:",productname)
        print("price:",productprice)
    elif choice==2:
        print("Exiting....")
        break
    else:
        print("Invaild choice !!")

