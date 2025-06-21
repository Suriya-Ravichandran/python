try:
    f=open("Hello.txt",'x')
except Exception as e:
    print(e)