import threading

def thread1(num):
    for x in range(num):
        print("Thread 1 is runing",x)

def thread2(num):
    for x in range(num):
        print("Thread 2 is runing",x)
    
def square(num):
    print(num*num)


t1=threading.Thread(target=thread1,args=(1000,))
t2=threading.Thread(target=thread2,args=(1000,))
t3=threading.Thread(target=square,args=(10,))


t1.start()
t2.start()
t3.start()

# t1.join()
# t2.join()
# t3.join()