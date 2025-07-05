try:
    filename=str(input("Enter filename: "))
    f=open(filename,"w")
    f.write("Hello wolrd")
    print("File write  suuccessfully")
except Exception as e:
    print(e)