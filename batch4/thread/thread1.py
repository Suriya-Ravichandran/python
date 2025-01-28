import threading

def threadloop1(val):
    for x in range(val):
        print("thread 1 is running....")

def threadloop2(val):
    for x in range(val):
        print("thread 2 is running....")

if __name__ =="__main__":
    t1=threading.Thread(target=threadloop1,args=(100,))
    t2=threading.Thread(target=threadloop2,args=(100,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Done....")