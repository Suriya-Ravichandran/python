filename=str(input("Enter file name: "))
filecontent=str(input("Enter the content: "))

f=open(filename,"w")
f.write(filecontent)
f.close()

f=open(filename,"r")
print(f.read())
f.close
