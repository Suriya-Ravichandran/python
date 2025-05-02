while True:
    try:
    
        filename=str(input("Enter file Name: "))
        f=open(file=filename,mode="x")
        print("File created Successfully !!")
    except FileExistsError as e:
        print("Error:",e)
