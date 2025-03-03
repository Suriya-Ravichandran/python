import subprocess

file=str(input("Enter your File name: "))
subprocess.call(["rm","-rf",file])
print("File deleted successfull")