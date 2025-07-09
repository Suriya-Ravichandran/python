table=int(input("Enter which table you want: "))
times=int(input("How many times: "))

# i=1
# while i<=times:
#     print(f"{table} x {i} = {table*i}")
#     i+=1
result=0
i=1
while i<=times:
    result=table*i
    i+=1
print(f"{table} x {times} = {result}")