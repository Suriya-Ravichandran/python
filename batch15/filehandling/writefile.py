try:
    filename=str(input("Enter filename: "))
    content=str(input("Enter your file content: "))
    f=open(filename,'a')
    f.write(content)
    print("File write successfully !!")
except Exception as e:
    print(e)