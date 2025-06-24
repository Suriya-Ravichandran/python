import threading

def loop1(num):
    for x in range(num):
        print(f"Loop1 {x}")

def loop2(num):
    for x in range(num):
        print(f"Loop2 {x}")

th1=threading.Thread(target=loop1,args=(100,))
th2=threading.Thread(target=loop2,args=(100,))

th1.start()
th2.start()

th1.join()
th2.join()