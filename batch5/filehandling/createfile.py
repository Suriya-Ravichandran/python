try:
    f=open("demo.txt","a")
    f.write("new word added\n")



    f=open("demo.txt","r")
    # print(f)
    print(f.read())
except:
    print("file not found")
