import threading

# Shared resource
counter = 0
# Create a Lock object
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        # Acquire the lock before modifying the shared resource
        with lock:
            counter += 1

# Create two threads that run the increment function
t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)

# Start threads
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()

print(f"Final counter value: {counter}")
