import threading

def loop1(value):
    for x in range(value):
        print(f"Thread 1 loop count{x}")

def loop2(value):
    for x in range(value):
        print(f"Thread 2 loop count{x}")

th1=threading.Thread(target=loop1,args=(1000,))
th2=threading.Thread(target=loop2,args=(1000,))

th1.start()
th2.start()

th1.join()
th2.join()