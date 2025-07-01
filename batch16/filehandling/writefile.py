try:
    f=open("Hello.txt","a")
    f.write("Hello world\n")
    print("File write successfully")
except Exception as e:
    print(e)