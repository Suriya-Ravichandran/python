try:
    f=open("Hello.txt","r")
    print(f.read())
except Exception as e:
    print(e)