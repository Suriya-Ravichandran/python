import threading
import time
def loop1(value):
    for x in range(value):
        print(f"{x} threading 1")
def loop2(value):
    for x in range(value):
        print(f"{x} threading 2")
start_time = time.time()  
th1=threading.Thread(target=loop1,args=(100,))
th2=threading.Thread(target=loop2,args=(100,))

th1.start()
th2.start()

th1.join()
th2.join()

end_time = time.time()  # End timing

print(f"Execution time: {end_time - start_time:.4f} seconds")


