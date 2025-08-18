import time 
import threading


def loop1(num):
    for x in range(num):
        print(f"{x} loop 1")

def loop2(num):
    for x in range(num):
        print(f"{x} loop 2")


start_time = time.time()

th1=threading.Thread(target=loop1,args=(1000,))
th2=threading.Thread(target=loop2,args=(1000,))

th1.start()
th2.start()

th1.join()
th2.join()


end_time = time.time() 
print(f"Program executed in {end_time - start_time:.2f} seconds")