# -*- coding: utf-8 -*-
import time,datetime
from enum import Enum

week_day = Enum('星期',('星期一','星期二','星期三','星期四','星期五','星期六','星期天'))

Nowdata = datetime.datetime.now()
print(Nowdata.weekday())
Now_weekday = week_day((Nowdata.weekday()+1) % 7)
# print(Now_weekday.name)

with open('C:/Users/flyingaura/Desktop/aaa.txt',mode = 'w') as test_file:
    # print(test_file.tell())
    # test_file.seek(0)
    # print(test_file.tell())
    # print(test_file.read())
    # test_file.write('\n')
    # test_file.write('\t 好好学习 \t 天天向上')
    # test_file.seek(21)
    # f_content = test_file.read()
    # print('content: %s  || content_length: %d' % (f_content,len(f_content)))
    # print(test_file.tell())
    test_file.write('今天是 ')
    test_file.write(time.strftime('%Y-%m-%d',time.localtime(time.time())))
    test_file.write('  %s' %Now_weekday.name)

with open('C:/Users/flyingaura/Desktop/aaa.txt',mode = 'r') as read_file:
    print(read_file.read())
