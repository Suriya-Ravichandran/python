import os

filename=str(input("Enter delete file name: "))
try:
    os.remove(filename)
    print("delete successfully")
except Exception as e:
    print("File does'n Exit")
