import threading

def loop1(num):
    for x in range(num):
        print(f"Loop 1 num{x}")

def loop2(num):
    for x in range(num):
        print(f"Loop 2 num{x}")



th1=threading.Thread(target=loop1,args=(1000,))
th2=threading.Thread(target=loop2,args=(1000,))

th1.start()
th2.start()

th1.join()
th2.join()

