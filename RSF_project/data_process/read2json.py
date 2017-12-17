# -*- coding: utf-8 -*-

import json,time
from LearnModule import cal_time

infilepath = r'F:\documents\python\learning2017\RSF_project\data\gov.cn news refined-2017-10-25.txt'
filecount = 1
OutlinesCount = 10000
OutJsonList = []
print('数据处理开始----->')

with open(infilepath, mode = 'r', encoding= 'utf-8') as infile:
    Nouseline = (infile.readline(),infile.readline())
    i = 0
    outstr = infile.readline().strip()
    jsonstr = ''
    starttime = time.time()
    fstarttime = starttime
    print('-----> 开始处理第 %d批数据' %filecount)
    while(outstr):
        if(i < OutlinesCount):
            if(outstr == '},'):
                jsonstr = jsonstr + '}'
                OutJsonList.append(json.dumps(jsonstr, ensure_ascii=False))
                i += 1
                jsonstr = ''
            else:
                jsonstr = jsonstr + outstr
            outstr = infile.readline().strip()
        else:
            outfilepath = r'F:\documents\python\learning2017\RSF_project\data\news_out%d.json' %filecount
            print('-----> 开始写入第%d个文件！' %filecount)
            with open(outfilepath, mode = 'w', encoding= 'utf-8') as outfile:
                for Arecord in OutJsonList:
                    outfile.write(json.loads(Arecord))
                    outfile.write('\n')
            endtime = time.time()
            print('-----> 第%d个文件写入完成，耗时 %f 秒' % (filecount, (endtime - starttime)))
            i = 0
            filecount += 1
            OutJsonList = []
            starttime = endtime
            print('-----> 开始处理第 %d批数据' % filecount)


if(OutJsonList):
    outfilepath = r'F:\documents\python\learning2017\RSF_project\data\news_out%d.json' %filecount
    print('-----> 开始写入第%d个文件！' %filecount)
    with open(outfilepath, mode = 'w', encoding= 'utf-8') as outfile:
        for Arecord in OutJsonList:
            outfile.write(json.loads(Arecord))
            outfile.write('\n')
    endtime = time.time()
    print('-----> 第%d个文件写入完成，耗时 %f 秒' % (filecount, (endtime - starttime)))

totaldata = (filecount - 1) * OutlinesCount + len(OutJsonList)
totalcosttime = cal_time.seconds2time(endtime - fstarttime)

print('----->数据处理结束，共处理 %d 条数据，共耗时 %d小时 %d分 %d秒'
      %(totaldata,totalcosttime[0],totalcosttime[1],totalcosttime[2]))

