#Example of threading
#When creating a GUI, always try to use multithreading
#One for the GUI and one for the background processing
#This way, the GUI doesn't become unresponsive
from threading import Thread
from threading import Lock
import time

print_lock = Lock()

def timer(name, delay, repeat):
    print('timer: ' + name + ' started')
    print_lock.acquire()
    while repeat > 0:
        time.sleep(delay)
        print(name + ': '+ str(time.ctime(time.time())))
        repeat -= 1
    print_lock.release()
    print('timer: ' + name + ' completed')

def Main():
    #We seperate the args from timer because we do not want to call the function immediately
    t1 = Thread(target = timer, args=('Timer1',1,5))
    t2 = Thread(target = timer, args=('Timer2',2,5))

    t1.start()
    t2.start()

    print('Main completed')

if __name__ =='__main__':
    Main() 
    
