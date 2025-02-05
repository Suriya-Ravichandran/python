def vaildateemail(data): #data comehere
    data=data # store a data in local varible
    flag1=False #this flag1
    flag2=True #this flag2
    for x in range(len(data)): #find the email index value
        if(data[x]=="@"): #find @ char
            flag1=True
        if(data[x]>="A" and data[x]<="Z"):
            flag2=False
    if(flag1==True and flag2==False):
        print("login success")
    else:
        print("login failed")


# app start
email=str(input("Enter your email: "))
email=email.upper()

# for x in range(len(email)):
#     print(f"{x}: {email[x]}")
vaildateemail(email) #passing email to verify function