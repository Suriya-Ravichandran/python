try:
    f=open("./file/hello1.txt","a")
    f.write("\nthis is new content")
    f.close()
except:
    print("File not found")

try:
    f=open("./file/hello.txt","r")
    # print(f.readline())
    print(f.read())
    f.close()
except:
    print("File Not found")