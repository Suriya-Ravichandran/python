import subprocess
try:
    f=open("hello.py","w")
    f.write("print(\"hello\")")
    try:
        print("reading a file")
        f=open("hello.py","r")
        print(f.read())
    except:
        print("File Not found")

    try:
        subprocess.call(["python3","hello.py"])
    except:
        print("Execution Error")
except:
    print("File Directory Not found")

