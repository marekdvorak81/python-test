import threading
import time
from datetime import datetime

class MyThreadPrintout(threading.Thread):
    def __init__(self, name="", sleep_duration = 1):
        super(MyThreadPrintout, self).__init__()
        self.setName(name)
        self.sleep_duration = sleep_duration

    def run(self):
        #my_lock.acquire()
        thread_name = self.getName()
        print("start thread " + thread_name)
        print("Thread name: %s" % thread_name)

        for i in range(3):
            print(thread_name + " " + datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
            time.sleep(self.sleep_duration)

        #my_lock.release()
        print("exit thread " + thread_name)

if __name__ == '__main__':
    print("Hello world!")

    my_lock = threading.Lock()
    t1 = MyThreadPrintout("Thread1", 1)
    t2 = MyThreadPrintout("Thread2", 1.1)
    #t3 = threadPrintout("Thread3", 1)

    threads = []
    threads.append(t1)
    threads.append(t2)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("exit main thread")