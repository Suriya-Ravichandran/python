import threading
import time

def printthreadone(*times,):
    for x in range(*times):
        print(f"times{x} This is Thead 1 is Running")


def printthreadtwo(*times):
    for x in range(*times):
        print(f"times{x} This is Thead 2 is Running")



thead1=threading.Thread(target=printthreadone,args=(10,))
thead2=threading.Thread(target=printthreadtwo,args=(10,))

thead1.start()
thead2.start()

thead1.join()
thead2.join()


print("---------------Thread runed suucessfully--------------------")
