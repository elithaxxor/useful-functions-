
## RANDOM SHUFFLE 
deck = 'ace two three four'.split()
>>> shuffle(deck)                        # Shuffle a list
>>> deck
['four', 'two', 'ace', 'three']

>>> sample([10, 20, 30, 40, 50], k=4)    # Four samples without replacement
[40, 10, 50, 30]


## threading class w/ raise exception ##
import threading
import ctypes
import time
  
class thread_with_exception(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
             
    def run(self):
 
        # target function of the thread class
        try:
            while True:
                print('running ' + self.name)
        finally:
            print('ended')
          
    def get_id(self):
 
        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id
  
    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
              ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
      
t1 = thread_with_exception('Thread 1')
t1.start()
time.sleep(2)
t1.raise_exception()
t1.join()



## DAEMON THREAD 
import Queue
import threading

def basic_worker(queue):
    while True:
        item = queue.get()
        # do_work(item)
        print(item)
        queue.task_done()
def basic():
    # http://docs.python.org/library/queue.html
    queue = Queue.Queue()
    for i in range(3):
         t = threading.Thread(target=basic_worker,args=(queue,))
         t.daemon = True
         t.start()
    for item in range(4):
        queue.put(item)
    queue.join()       # block until all tasks are done
    print('got here')

basic()




# #- Method 2: from Thread Inherit and rewrite run()
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()#Note: be sure to explicitly call the initialization function of the parent class.
        self.arg=arg
    def run(self):#Define the function to run for each thread
        time.sleep(1)
        print('the arg is:%s\r' % self.arg)

for i in range(4):
    t =MyThread(i)
    t.start()

print('main thread end!')


# Python program showing
# how to kill threads
# using set/reset stop
# flag
 
import threading
import time
 
def run():
    while True:
        print('thread running')
        global stop_threads
        if stop_threads:
            break
 
stop_threads = False
t1 = threading.Thread(target = run)
t1.start()
time.sleep(1)
stop_threads = True
t1.join()
print('thread killed')



# Python program killing
# threads using stop
# flag
 
import threading
import time
 
def run(stop):
    while True:
        print('thread running')
        if stop():
                break
                 
def main():
        stop_threads = False
        t1 = threading.Thread(target = run, args =(lambda : stop_threads, ))
        t1.start()
        time.sleep(1)
        stop_threads = True
        t1.join()
        print('thread killed')
main()
