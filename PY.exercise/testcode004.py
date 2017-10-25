# -*- coding: utf-8 -*-
import random
import csv
from LearnModule import String_func,StringSplit
import json
import time
#
# # alist = [random.sample(list(range(10)),3) for i in range(10)]
# alist = []
# bdict = {}
# for i in range(10):
#     bdict[str(i)] = random.sample(list(range(10)),3)
#     # alist.append(blist)
# print(bdict)
# #
# # key0 = list(bdict.keys())[0]
# # print(key0)
#
# datafilepath2 = r'F:\memory\python-learning\learning2017\program data\高校相关数据\2016年全国高等学校名单.csv'
#
# # with open(datafilepath2, mode='r', encoding='GBK') as infile:
# #     # datalist = []
# #     for aline in csv.reader(infile):
# #         print(aline)
# testStr = 'advann123sldfklsv39d3sl540lasd023lk1askf0sldkf001,voi208.30123lsk+++'
# Numlist = String_func.StrExtractNum(testStr)
# print(Numlist)
# TotalCount = 0
# URLCount = 0
# testkey = '链接'
# with open(r'F:\memory\python-learning\learning2017\ESP_project\data_news\origin_news.json', mode = 'rb') as infile:
#     for Aline in infile.readlines():
#         Aline_decode = Aline.decode('utf-8').strip()
#         AlineJson = json.loads(Aline_decode)
#         TotalCount += 1
#         if(testkey in AlineJson.keys() and AlineJson[testkey]):
#             URLCount += 1
#
# print('TotalCount = %d' %TotalCount)
# print('URLCount = %d' %URLCount)
# date = '2010-1101'
# print(time.strptime(date, "%Y-%m-%d"))
# print(list(time.strptime(date, "%Y-%m-%d")))
# NowTime = int(time.time())
# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(NowTime)))

teststr = 'http://gongyi.sohu.com/20120716/n348242197.shtml'
print(StringSplit.stringsplit(StringSplit.stringsplit(teststr,'/')[1],'.')[0])