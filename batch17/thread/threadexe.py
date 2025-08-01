import time
import threading
start_time = time.time()

def loop1(args):
    for x in range(args):
        print(f"Loop1 {x}")

def loop2(args):
    for x in range(args):
        print(f"Loop2 {x}")

th1=threading.Thread(target=loop1,args=(5000,))
th2=threading.Thread(target=loop2,args=(5000,))

th1.start()
th2.start()

th1.join()
th2.join()

end_time = time.time()
print(f"loop1 execution time: {end_time - start_time:.6f} seconds\n")

