try:
    f=open("Hello.txt","x")
    print("File create successfully")
except Exception as e:
    print(e)