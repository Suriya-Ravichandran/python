import subprocess

file=str(input("Enter your File name: "))
subprocess.call(["python",file])
print("File created success full")