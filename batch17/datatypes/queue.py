while True:
    rationshop=[]

    for x in range(5):
        rationshop.append(f"{x+1} Person")
    print("------Queue-------")
    print(rationshop)

    print("--------Remove queue ---------")
    for x in range(len(rationshop)):
        del rationshop[0]
        print(rationshop)