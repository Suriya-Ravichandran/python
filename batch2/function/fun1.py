def setname():
    name="suriya"
    return name

def setpassword():
     password="123"
     return password   

    
def login(name,password):
    name1=str(input("Enter user name:"))
    if(name1==name and password==password):
        print("login success") 
    else:
        print("login failed")
    

name=setname()
password=setpassword()
login(name,password)

