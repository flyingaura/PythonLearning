#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import threading, time

class MyThread(threading.Thread):
    def __init__(self, ThreadID, ThreadName, delay, counter=5):
        threading.Thread.__init__(self)
        self.ThreadID = ThreadID
        self.ThreadName = ThreadName
        self.delay = delay
        self.counter = counter

    def run(self):
        print('<-- %s 线程启动 -->' % self.ThreadName)
        print_thread(self.ThreadName, self.delay, self.counter)
        print('<-- %s 线程结束 -->' % self.ThreadName)

def print_thread(ThreadName, delay, counter):
    runtimes = 0
    while(runtimes < counter):
        print('%s-->run NO.%d : %s ' % (ThreadName, runtimes + 1, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
        time.sleep(delay)
        runtimes += 1
    # ThreadName.exit()

thread1 = MyThread(1, 'thread_1', 2,10)
thread2 = MyThread(2, 'thread_2', 5)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('所有线程运行完毕，主线程退出！')
