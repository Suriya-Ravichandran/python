password1="suriya@1234"

password=str(input("Enter your password: "))
print("this password: ",password)
ch1=password.replace("s","a")
p1=password1.replace("s","a")
p2=p1.replace("@","#")
ch2=ch1.replace("@","#")
finalpass=ch2
finalpass2=p2

print("This finnal pass: ",finalpass)
print("This finnal pass: ",finalpass2)

if finalpass==finalpass2:
    print("Login")
else:
    print("login failed")
