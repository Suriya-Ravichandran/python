my_string = "suriya"
hash_value = hash(my_string)
print(hash_value)

password="suriy"
hash_value1=hash(password)
print(hash_value1)

if hash_value==hash_value1:
    print("same hash")
else:
    print("not same hash")