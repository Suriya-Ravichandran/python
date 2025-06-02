def genratehash(password):
    saltkey="ahsdfghgsdfsdfyfdhaf"
    saltkeypassword=saltkey+password+saltkey
    replace1=saltkeypassword.replace("a","r")
    replace2=replace1.replace("s","hack")
    finalsalt=replace2+saltkey
    replace3=finalsalt.replace("g","$")
    replace4=replace3.replace(" ","%")
    finnalpassword=replace4.replace("f","&")
    return finnalpassword

def checkhash(password):
    saltkey="ahsdfghgsdfsdfyfdhaf"
    saltkeypassword=saltkey+password+saltkey
    replace1=saltkeypassword.replace("a","r")
    replace2=replace1.replace("s","hack")
    finalsalt=replace2+saltkey
    replace3=finalsalt.replace("g","$")
    replace4=replace3.replace(" ","%")
    finnalpassword=replace4.replace("f","&")
    return finnalpassword



password=str(input("Enter password: "))

if(genratehash(password)==checkhash(password)):
    print("Login success")
else:
    print("Login failed")

