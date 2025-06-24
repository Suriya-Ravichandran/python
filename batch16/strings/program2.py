import hashlib
def generate_md5_hash(input_string):
        # Create an MD5 hash object
        md5_hash = hashlib.md5()
        # Update the hash object with bytes-like object
        md5_hash.update(input_string.encode('utf-8'))
        # Return the hexadecimal digest of the hash
        return md5_hash.hexdigest()

def genratehash(password):
    saltkey="dahfdasggbrthrngdsafashdsdsssssssssshdsafhsdfh"
    password=password[0:4]
    password=saltkey+str(password)+saltkey
    password=password.replace("s","z")
    password=password.replace("b","y")
    password=password.replace("f","w")
    password=password.replace("@","#")
    hash=generate_md5_hash(password)
    return hash

password=str(input("Enter your password: "))
print(f"Orignal password: {password}")
print(f"Hashed Password: {genratehash(password)}")



