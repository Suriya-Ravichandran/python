# f=open("Demo.txt","a")
# f.write("Hello this is demo file created by python\n")
# f.close()



# f=open("Demo.txt","r")
# print(f.read())

# f=open("Demo.txt","a")
# f.write("Hello this is demo file created by python\n")
# f.close()

print("-----------This is Orginal content--------------")

f=open("Demo.txt","r")
print(f.read())


f=open("Demo.txt", "w")
f.write("")

print("-----------This is Override content--------------")

f=open("Demo.txt","r")
print(f.read())