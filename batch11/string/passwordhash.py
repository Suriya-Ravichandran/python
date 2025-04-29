def hashpass(data):
    salt="afdfhdsgsayhdfgyrsbfhsdfb"
    hashpassword=salt+data+salt
    hashpassword=hashpassword.replace("a","ji")
    hashpassword=hashpassword.replace("s","kb")
    hashpassword=hashpassword.replace("y","gk")
    return hashpassword

def verifypassword(data):
    salt="afdfhdsgsayhdfgyrsbfhsdfb"
    verifypassword=salt+data+salt
    verifypassword=verifypassword.replace("a","ji")
    verifypassword=verifypassword.replace("s","kb")
    verifypassword=verifypassword.replace("y","gk")
    return verifypassword

data=str(input("Enter password: "))
hashpassword=hashpass(data)
verifypass=verifypassword(data)
if(hashpassword==verifypass):
    print("Hash match")
else:
    print("Hash not")