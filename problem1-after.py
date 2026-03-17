import threading
import time

counter = 10
mutex = threading.Semaphore(1)

def processA():
    global counter
    for i in range(1000):
        mutex.acquire()
        temp = counter
        time.sleep(0.0001)
        temp = temp + 1
        counter = temp
        mutex.release()

def processB():
    global counter
    for i in range(1000):
        mutex.acquire()
        temp = counter
        time.sleep(0.0001)
        temp = temp + 2
        counter = temp
        mutex.release()

t1 = threading.Thread(target=processA)
t2 = threading.Thread(target=processB)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Counter:", counter)
