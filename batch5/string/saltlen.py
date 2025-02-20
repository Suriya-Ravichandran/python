saltkey="73419b546535a017b6a05091b74ee18e"
hashpass="27e0b7a975b28fb705c4b95c172e95b8ef713eeeeb0c62b765d1473b38c4148b"


combine=saltkey+hashpass
lensalt=len(saltkey)
print(lensalt)
print(combine)

salt = combine[:lensalt]
hash_value = combine[lensalt:]


print(f"Extracted Salt: {salt}")
print(f"Extracted Hash: {hash_value}")