import threading
import time

# Record the start time
start_time = time.perf_counter()

# Replace with your code

def threadloop1(times):
    for x in range(times):
        print(f"{x}:thread 1 is running")


def threadloop2(times):
    for x in range(times):
        print(f"{x}:thread 2 is running")

t1=threading.Thread(target=threadloop1,args=(100,))
t2=threading.Thread(target=threadloop2,args=(100,))

# start the thread
t1.start()
t2.start()


# stop/end the excution
t1.join()
t2.join()


# Record the end time
end_time = time.perf_counter()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.6f} seconds")