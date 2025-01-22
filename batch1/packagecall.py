# import mypackage  # This will also run __init__.py
# Accessing functions from modules inside the package:
from mypackage import passwordhash

password=str(input("Enter password: "))
hashpassword=passwordhash.genhashpass(password)
print(hashpassword)

# c3VyaXlhQDA5ODAuNzcyNDYxMjg5NzE5MDI3OQ==

password=str(input("Enter decode-password: "))
decodepassword=passwordhash.reshashpass(password)
print(decodepassword)
