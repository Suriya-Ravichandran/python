try:
    filename=str(input("Enter filename: "))
    content=str(input("Enter Your content here: "))
    f=open(filename,"w")
    f.write(content)
    print("File write success")
except Exception as e:
    print(e)
