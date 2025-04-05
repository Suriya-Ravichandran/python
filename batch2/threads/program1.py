import threading


def print_name(num):
    print(num * num)

num1 = 100000000000
num2 = 200002303020202020

# Create and start threads
thread1 = threading.Thread(target=print_name, args=(num1,))
thread2 = threading.Thread(target=print_name, args=(num2,))

thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

print("Threads are finished...exiting")
