import base64
saltkey="shffygfybadcbsifhbracsdchdschsrfhurnj"

def signin(password):

    saltedpassword=saltkey+password+saltkey
    sample_string_bytes = saltedpassword.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    hashpassword = base64_bytes.decode("ascii")

    # print("Password:",password)
    # print("saltedpassword:",saltedpassword)
    # print("Hashpassword:",hashpassword)
    return hashpassword


def login(password):

    saltedpassword=saltkey+password+saltkey
    sample_string_bytes = saltedpassword.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    hashpassword = base64_bytes.decode("ascii")

    # print("Password:",password)
    # print("saltedpassword:",saltedpassword)
    # print("Hashpassword:",hashpassword)
    return hashpassword


password=str(input("Enter password: "))

signinhash=signin(password)
loginhash=login("foo@098")

if signinhash==loginhash:
    print("login success")
else:
    print("login failed")
