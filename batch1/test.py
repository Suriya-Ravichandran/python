import threading

# Shared resource
counter = 0

# Create a lock object
lock = threading.Lock()

# Function to increment the counter
def increment():
    global counter
    for _ in range(1000000):
        # Acquire the lock
        lock.acquire()
        counter += 1
        # Release the lock
        lock.release()

# Create threads
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Counter:", counter)
