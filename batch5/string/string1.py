def signup(password,saltkey):
    hashpassword=f"{saltkey}{password}{saltkey}"
    print("Hash Password: ",hashpassword)
    return hashpassword

def signin(hashpassword,password,saltkey):
    verfiy=f"{saltkey}{password}{saltkey}"
    print("Verfiy password:",verfiy)
    if(hashpassword==verfiy):
        print("Login success")
    else:
        print("login failed")
    
    

# app
saltkey="a2ir@#$gdshsfhudshffhgbsfjh"
password=str(input("Enter password: "))
success=signup(password,saltkey)

signin(success,password,saltkey)



