import time 
import threading


def loop1(num):
    for x in range(num):
        print(f"{x} loop 1")

def loop2(num):
    for x in range(num):
        print(f"{x} loop 2")

start_time = time.time()  # Start time


th1=threading.Thread(target=loop1,args=(10000,))
th2=threading.Thread(target=loop2,args=(10000,))

th1.start()
th2.start()

th1.join()
th2.join()

end_time = time.time()  # End time

print(f"Program executed in {end_time - start_time:.2f} seconds")