def signup(password):
    saltkey="a2ir@#$gdshsfhudshffhgbsfjh"
    hashpassword=f"{saltkey}{password}{saltkey}"
    print("Hash Password: ",hashpassword)
    return hashpassword

def signin(hashpassword,password,saltkey):
    pass
    


