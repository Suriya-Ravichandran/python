try:
    f=open("Hello.txt",'x')
    print("File created !!!")
except Exception as e:
    print(f"Error: {e}")