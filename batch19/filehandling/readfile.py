try:
    filename=str(input("Enter file name: "))
    f=open(filename,"r")
    print(f.read())
except Exception as e:
    print(e)             