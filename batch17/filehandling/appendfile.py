try:
    filename=str(input("Enter filename: "))
    content=str(input("Enter Your content here: "))
    f=open(filename,"a")
    f.write(f"{content}\n")
    print("File write success")
except Exception as e:
    print(e)