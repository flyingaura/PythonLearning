#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import threading, time

def print_thread(ThreadName, delay):
    icount = 0
    # ipercent = icount / 10.0
    while(icount / 10.0 < 1.0):
        time.sleep(delay)
        icount += 1
        print('%s:%s ---> %.3f %%' % (ThreadName, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), icount * 10.0))
        # return '%.3f %%' %(ipercent)
    return '进度完成'

try:
    str1 = threading._start_new_thread(print_thread, ('ThreadName1', 2))
    str2 = threading._start_new_thread(print_thread, ('ThreadName2', 5))
except:
    str1 = '错误：线程无法启动'
    str2 = '错误：线程无法启动'

while(str1 != '进度完成' or str2 != '进度完成'):
    print('%s || %s' % (str1, str2))

# print(str1)
# print(str2)
