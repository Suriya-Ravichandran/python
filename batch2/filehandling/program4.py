import os
if os.path.exists("hello.py"):
  os.remove("hello.py")
else:
  print("The file does not exist")