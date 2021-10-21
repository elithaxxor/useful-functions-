
## RANDOM SHUFFLE 
deck = 'ace two three four'.split()
>>> shuffle(deck)                        # Shuffle a list
>>> deck
['four', 'two', 'ace', 'three']

>>> sample([10, 20, 30, 40, 50], k=4)    # Four samples without replacement
[40, 10, 50, 30]



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
