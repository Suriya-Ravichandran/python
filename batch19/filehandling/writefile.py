try:
    filename=str(input("Enter file name: "))
    content=str(input("Enter your content: "))
    f=open(filename,"a")
    f.write(content)
    print("File write success")
except Exception as e:
    print(e)