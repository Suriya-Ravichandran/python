import threading
import time

def loop1(num):
    for x in range(num):
        print(f"{x} loop 1")


def loop2(num):
    for x in range(num):
        print(f"{x} loop 2")


start_time = time.time()  

t1 =threading.Thread(target=loop1,args=(100,))
t2 =threading.Thread(target=loop2,args=(100,))

t1.start()
t2.start()

t1.join()
t2.join()

end_time = time.time()  # End timing

print(f"Execution time: {end_time - start_time:.4f} seconds")