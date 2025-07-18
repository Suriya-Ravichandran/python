try:
    filename=str(input("Enter filename: "))
    f=open(filename,"r")
    print(f.read())
except Exception as e:
    print(e)