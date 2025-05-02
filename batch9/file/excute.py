import subprocess

filename=str(input("Enter file Name: "))
content=str(input("Enter your file content: "))
f=open(file=filename,mode="a")
f.write(content)
print("file created success")

print("-----------------------")
print(subprocess.call(["python",filename]))