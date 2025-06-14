
def decimal_to_binary(num):
    binary=""
    if num==0:
        return 0
    while num>0:
        binary=str(num%2)+binary
        num=num // 2
    return binary

data=decimal_to_binary(10)
one=data.count("1")
zero=data.count("0")
print(one)
print(zero)

