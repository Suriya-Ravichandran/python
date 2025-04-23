import threading

def Thread1(num):
    for x in range(num):
        print("Thread1  Hello wolrd",x)

def Thread2(num):
    for x in range(num):
        print("Thread2  Hello wolrd",x)

# create a thread    target = function args= send arguments via tuple
t1=threading.Thread(target=Thread1,args=(100,))

t2=threading.Thread(target=Thread2,args=(100,))

t1.start() # to start a thread

t2.start()

t1.join() # to comibined a multithreads
t2.join()