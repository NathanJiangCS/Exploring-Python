#A thread can be thought of as a seperate program running along side each other
#But they can share data easily
import threading
from queue import Queue
import time
#A major problem with multithreading is that the same variable might be
#Accessed at the same time. Therefore, we must lock the variable so that it
#cannot change from time to time.

#Locking ability of the threading module
#We have to have a lock per thing
#This sets a threading lock to the print function
print_lock = threading.Lock()

#Defining our task
def exampleJob(worker):
    time.sleep(0.5)
    
    with print_lock:
        print(threading.current_thread().name, worker)

def threader():
    while True:
        worker = q.get()
        exampleJob(worker)

        q.task_done()
q = Queue()

#Defining threads
for x in range(10):
    t = threading.Thread(target = threader)
    #It will die when the main thread dies
    t.daemon = True
    #Starts the thread
    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)

q.join()

print('Time taken: ',time.time() - start)
