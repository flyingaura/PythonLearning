# -*- coding: utf-8 -*-
import random
import time
import os
from LearnModule import StringSplit,String_func
# # alist = [random.sample(list(range(10)),3) for i in range(10)]
# alist = []
# bdict = {}
# for i in range(10):
#     bdict[str(i)] = random.sample(list(range(10)),3)
#     # alist.append(blist)
# print(bdict)
#
# key0 = list(bdict.keys())[0]
# print(key0)

# NowTime = time.time()
# # JustTime = []
# # JustTime.append(NowTime)
# print(NowTime)
# NowTime = 1505100099
# print(type(NowTime))
# print(time.localtime(NowTime))
#
# FormatTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(NowTime))
# print(FormatTime)

# print(os.path.splitext('备忘录_20130630_174926-马云论断.pdf')[0])
# filepath = 'D:\\ESP_files\\相关技术学习\\搜索技术\\信息检索关键技术_2.ppt'
# print(os.path.split(filepath))
#
# SetFilePath = StringSplit.stringsplit(filepath,'\\')
# FilePath = ''
# for Apath in SetFilePath[1:]:
#     FilePath = os.path.join(FilePath,Apath)
#
# print(FilePath)

# print(String_func.if_enletter('t'))

# astr = '\\公司管理\\总经理办'
# splitstr = '\\'
#
# print(astr.strip(splitstr).split(splitstr)[0])
# print(isinstance('abcd',list))
# xlist = [x for x in range(10)]
# for x in xlist:
#     if(2 <= x < 7):
#         print('good')
#     else:
#         print('bad')
class aaa(object):
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def __str__(self):
        return '(%d,%d)' %(self.i, self.j)

class bbb(object):

    def __init__(self,i,j):
        self.i = i * i
        self.j = j * j

    def __str__(self):
        return '[%d,%d]' %(self.i, self.j)

alist = []
blist = []
cdict = {}
for i in 'abcde':
    cdict[i] = ord(i)
    # for j in range(3):
        # alist.append(aaa(i,j))
        # blist.append(bbb(i,j))

print(cdict)
print(sorted(cdict.keys()))

