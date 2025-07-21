import subprocess

filename=str(input("Enter file name: "))
subprocess.run(["python",filename],shell=True)