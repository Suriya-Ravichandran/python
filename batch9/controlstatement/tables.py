table=int(input("Enter Which Table You want: "))
times=int(input("Enter how many times You Want: "))

for x in range(1,times+1):
    print(f"{table} X {x} = {table*x}")