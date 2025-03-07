import subprocess

filename=str(input("Enter file name: "))
subprocess.call(["nano",filename])
print("file create and edit success")