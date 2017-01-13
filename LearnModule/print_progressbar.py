'按指定时间间隔循环打印进度条，默认时间间隔为500毫秒'

__author__ = 'weil'

# -*- coding:utf-8 -*-
import time, os
#
# def printbar(str,inc = 2):
#     while True:
#         print('*')
#         time.sleep(inc)
#
#
# printbar('=')

import time

for i in range(1000):
    percent = 1.0 * i / 1000 * 100

    print('complete percent:%10.8s%s' % (str(percent), '%'))

    time.sleep(0.5)