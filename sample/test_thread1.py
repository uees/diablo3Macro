import threading
import time


def print_time(thread_name, delay):
    for i in range(0, 5):
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))


# 创建两个线程
t1 = threading.Thread(target=print_time, args=("Thread-1", 1))
t2 = threading.Thread(target=print_time, args=("Thread-2", 2))
t1.start()
t2.start()
t1.join()
t2.join()
