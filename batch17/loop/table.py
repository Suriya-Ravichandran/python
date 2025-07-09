table=int(input("Enter which table you want: "))
times=int(input("How many times: "))
result=0
for x in range(1,times+1):
    result=table*x
print(f"{table} x {times} = {result}")