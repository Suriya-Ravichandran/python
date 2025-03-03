import subprocess

file=str(input("Enter your File name: "))
subprocess.call(["touch",file])
print("File created success full")