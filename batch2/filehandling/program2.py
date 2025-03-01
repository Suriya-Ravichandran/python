f=open("new.txt","w")

f.write("\nHello world new overigth")

f.close()

f=open("new.txt","r")
print(f.read())