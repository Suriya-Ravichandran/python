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


threadloop1(100)
threadloop2(100)

# Record the end time
end_time = time.perf_counter()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.6f} seconds")