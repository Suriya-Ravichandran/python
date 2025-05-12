import threading

def thread1(num):
    for x in range(num):
        print(f"{x} thread 1")

def thread2(num):
    for x in range(num):
        print(f"{x} thread 2")


t1=threading.Thread(target=thread1,args=(100,))
t2=threading.Thread(target=thread2,args=(100,))

t1.start()
t2.start()

t1.join()
t2.join()

