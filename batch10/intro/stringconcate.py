import hashlib
password="suriya"
salt="asdadfjhfhdasfsghfyugrbf"

saltedpassword=salt+password+salt+salt
md5hashpassword=hashlib.md5(saltedpassword.encode())
print(md5hashpassword.hexdigest())