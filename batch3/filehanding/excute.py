import subprocess

file=str(input("Enter your File name: "))
subprocess.call(["python3",file])
print("File created success full")