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
print(isinstance('abcd',list))