import threading
import time

counter = 10

def processA():
    global counter
    for i in range(1000):
        temp = counter
        time.sleep(0.0001)   # force context switch
        temp = temp + 1
        counter = temp

def processB():
    global counter
    for i in range(1000):
        temp = counter
        time.sleep(0.0001)
        temp = temp + 2
        counter = temp

t1 = threading.Thread(target=processA)
t2 = threading.Thread(target=processB)

t1.start()
t2.start()

t1.join()
t2.join()

print("Final Counter:", counter)
