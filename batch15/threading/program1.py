import threading
import time


def loop1(num):
    for x in range(num):
        print(f"loop1 {x}")
    
def loop2(num):
    for x in range(num):
        print(f"loop2 {x}")

start_time = time.time()  # Start timing

# loop1(100000)
# loop2(100000)

th1=threading.Thread(target=loop1,args=(100000,))
th2=threading.Thread(target=loop2,args=(100000,))

th1.start()
th2.start()

th1.join()
th2.join()

end_time = time.time()  # End timing

print(f"Execution time: {end_time - start_time:.4f} seconds")