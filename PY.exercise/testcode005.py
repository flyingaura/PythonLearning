# -*- coding: utf-8 -*-
import random,numpy,math
from string import Template
import sys,msvcrt,json,time
from collections import OrderedDict
# sys.path.append('.\WebAppLearning')
# from yate import yate
#
# print(yate.start_response('text/plain'))
# # print(sys.path)
# # alist = [math.sqrt(random.randint(0,100)) for x in range(10)]
# # print(alist)
# # print(numpy.array(alist) * 4)
#
#
# print(int('aa'))
# def inputPassWD(msg = '', maskchar = '*'):
#     if(msg):
#         # print('------')
#         print(msg, end='',flush=True)
#         # print(':::')
#     inputStr = []
#     while(True):
#         Achar = msvcrt.getch()
#         if(Achar in b'\n\r'):
#             break
#         elif(Achar == b'\3'):
#             inputStr = []
#             break
#         elif(Achar == b'\b'):
#             if(inputStr):
#                 inputStr.pop()
#                 sys.stdout.write('\b\b')
#         else:
#             inputStr.append(Achar)
#             if(maskchar != None):
#                 sys.stdout.write(maskchar)
#
#     # return ''.join(inputStr)
#     return inputStr
#
# passwd = inputPassWD('请输入密码：')
# print(passwd)

#

# # print(list(range(1,11)))
# init_dict = OrderedDict()
# filepath = r'F:\documents\python\learning2017\PY.exercise\WebAppLearning\arithmetic_training_game\data\test.json'
# with open(filepath, mode = 'a+', encoding= 'utf-8') as NetFile:
#     NetFile.seek(0)
#     time_string = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
#     init_dict[time_string] = list(range(10))
#     json.dump(init_dict, NetFile)
#     NetFile.write('\n')
#
#     NetFile.seek(0)
#     for Arec in NetFile.readlines():
#         Arec_json = json.loads(Arec)
#         print(Arec_json)

# test_string = 'adad  ;akdklasf ;; ksf  |   '
# print(test_string)
# print(test_string.strip(' ').strip('|'))

test_dict = {}
for i in range(10):
    time_string = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time() + random.randint(-100000,100000)))
    test_dict[time_string.split(' ')[0]] = time_string

print(test_dict)
print(sorted(test_dict.keys()))
print(sorted(test_dict.keys(), reverse=True))

