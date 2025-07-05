try:
    filename=str(input("Enter filename: "))
    f=open(filename,"a")
    f.write("Hello wolrd\n")
    print("File write  successfully")
except Exception as e:
    print(e)