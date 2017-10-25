# -*- coding: utf-8 -*-

# 按省级提取高校分布情况

import csv
from LearnModule import StringSplit,String_func

filepath = r'F:\documents\python\learning2017\program data\高校相关数据\2016年全国高等学校名单.csv'

def readCSV(filepath,reqcode = 'utf-8'):
    with open(filepath, mode = 'r', encoding= reqcode) as infile:
        datalist = []
        for aline in csv.reader(infile):
            datalist.append(aline)

    return datalist

DataDistrList = []
for aline in readCSV(filepath):
    DataRec = {}
    if(not aline[0].isdigit()):
        DataDistr = StringSplit.stringsplit(aline[0],('（','）'))
        try:
            DataRec[DataDistr[0]] = String_func.StrExtractNum(DataDistr[1],1)[0]
        except IndexError:
            continue
        DataDistrList.append(DataRec)

with open(r'F:\documents\python\learning2017\program data\高校相关数据\高校按省分布.dat', mode = 'w', encoding = 'utf-8') as outfile:
    for Arec in DataDistrList:
        for key in Arec:
            outfile.write('%s\t%d' %(key,Arec[key]))
            outfile.write('\n')





