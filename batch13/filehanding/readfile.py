try:
    f=open("hello.txt","r")
    print(f.read())
except Exception as e:
    print(e)