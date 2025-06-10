table=int(input("Enter which tables you want: "))
HMT=int(input("Enter How many times You want: "))
for x in range(1,HMT+1):
    print(f"{table} x {x} = {x*table}")