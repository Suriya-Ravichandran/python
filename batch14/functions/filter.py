age=[10,20,19,18,23,9,8]


def eligablevote(data):
    if data>=18:
        return True
    else:
        return False

eligableage=filter(eligablevote,age)
print(list(eligableage))