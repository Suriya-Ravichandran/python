import subprocess
try:
    f=open("demo.txt","a")
    print(f)
    try:
        f.write("\nhello")
    except:
        print("this file only have read permission")
    f=open("demo.txt", "r")
    print("Reading a file")
    print(f.read())
    try:
        subprocess.call(["python3","hello.py"])
    except:
        print("Execution Error...")


except:
    print("File not Avaliable")