try:
    filename=str(input("Enter filename: "))
    f=open(filename,"x")
    print("File create suuccessfully")
except Exception as e:
    print(e)