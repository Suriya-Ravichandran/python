import subprocess

file=str(input("Enter your File name: "))
subprocess.call(["nano",file])
print("File writed successfull")