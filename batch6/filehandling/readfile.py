try:
    f=open("./file/hello.txt","r")
    # print(f.readline())
    print(f.read())
    f.close()
except:
    print("File Not found")