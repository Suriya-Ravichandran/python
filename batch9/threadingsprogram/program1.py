import threading

def loop1(num):
    for x in range(num):
        print(f"{x} Loop1")


def loop2(num):
    for x in range(num):
        print(f"{x} Loop2")


t1=threading.Thread(target=loop1,args=(10000,))
t2=threading.Thread(target=loop2,args=(10000,))

t1.start()
t2.start()

t1.join()
t2.join()


