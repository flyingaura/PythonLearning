# -*- coding: utf-8 -*-

import json
import random
import os
from LearnModule import cal_date
from LearnModule import cal_time
from LearnModule import StringSplit

datalist = []
AnormalData = {}

def SetDepartment(deplist):   #从部门列表中随机分配一个所属部门
    index = random.randint(0,len(deplist) - 1)
    return deplist[index]

def SetSource(sourcelist):  #从新闻来源列表中随机分配一个新闻来源
    return sourcelist[random.randint(0,len(sourcelist) - 1)]

def SetCatlog(catlog):  #从新闻分类列表中随机分配一个新闻类别
    return catlog[random.randint(0,len(catlog) - 1)]

def SetAppendixFiles(FilesPathList,n):   #从附件列表中分配一个第n个附件给该条新闻
    if(n >= len(FilesPathList)):
        n = n % len(FilesPathList)
    randNum = random.randint(1,12)
    if(randNum > 9):
        AppendixFilesList = []
        fileindexset = set()
        for i in range(3):
            fileindexset.add(random.randint(0,2))
        for i in fileindexset:
            if(n + i < len(FilesPathList)):
                AppendixFilesList.append(FilesPathList[n + i])
        return AppendixFilesList
    else:
        return ''

def SetPubtime(init_year,init_time,days,seconds):  #随机生成发布日期 2010-05-06 12:34:50
    Pubdata = cal_date.Cal_Data(init_year,days)
    Pubdata = Pubdata[0:4] + '-' + Pubdata[4:6] + '-' + Pubdata[6:]
    Pubtime = cal_time.cal_time(init_time,seconds)
    return Pubdata + ' ' + Pubtime

deplist = ['总经理办公室','产品中心','研发中心','数据中心','销售中心','销售支持中心','项目开发与服务中心',
           '质量保障部','综合事务部','人力资源部','财务部', '法务部']

sourcelist = ['公司官网','营销管理系统','资产管理系统','OA系统','项目管理系统','质量管理系统','统一开发平台',
              '外网新闻与情报监控系统','内网办公门户']

catlog = ['科技','金融','互联网生态','企业管理','行业动态','娱乐','房地产','政策环境','其他']

# ========== 获取新闻的附件路径 ============
appendixfiles = os.listdir('E:/业务项目/Y.学习资料/EKP共享文档/2014年7月15日')
appendixfilesPath = []
appendixRelativePath = '/ESPnews/appendixfiles'
for afile in appendixfiles:
    appendixfilesPath.append(os.path.join('%s/%s' %(appendixRelativePath,afile)))
    # print(appendixfilesPath)
n = 0  #分配附件用的起始值
with open('F:/documents/python/learning2017/ESP_project/data_news/origin_news.json', mode = 'rb') as infile:   #origin_news
    StripStr = '安卓网 > \t\t\t\t科技频道 \t\t\t\t\t\t\t\t\t  \t\t\t\t\t\t\t\t\t  > 互联\t\t\t\t\t\t\t  \t\t       <!-- //头部 ---> \t \t\t\t \t\t\t\t \t\t\t\t\t'
    for Aline in infile.readlines():
        Aline_decode = Aline.decode('utf-8').strip()
        AlineJson = json.loads(Aline_decode)
        # print(AlineJson)
        for key in AlineJson:
            # print(key)
            if(key == '标题'):
                AnormalData['title'] = AlineJson[key]
            elif(key == '正文内容'):
                try:
                    AnormalData['content'] = StringSplit.stringsplit(AlineJson[key].strip(StripStr),'\t')[-1]
                except TypeError as e:
                    print(AlineJson[key].strip(StripStr))

            elif(key == '链接'):
                AnormalData['Original_address'] = AlineJson[key]

            AnormalData['pubtime'] = SetPubtime(20150101,'00:00:00',random.randint(0,730),random.randint(0,24 * 3600))
            AnormalData['belongdep'] = SetDepartment(deplist)
            AnormalData['viewcounts'] = random.randint(0,76)
            AnormalData['source'] = SetSource(sourcelist)
            AnormalData['NewsCat'] = SetCatlog(catlog)

        #============以下为给该条新闻随机分配一个附件============
            appendixFilePath = SetAppendixFiles(appendixfilesPath,n)
            if(appendixFilePath != ''):
                n = n + 1
            AnormalData['appendix_URL'] = appendixFilePath
            AnormalData['appendix_filenames'] = [os.path.basename(x) for x in appendixFilePath]

        datalist.append(AnormalData.copy())

# 把规范化处理后的新闻数据写入到json文件中，用来导入数据库
with open('F:/documents/python/learning2017/ESP_project/data_news/normalized_news.json',mode = 'wb') as outfile:
    for Adata in datalist:
        outfile.write(json.dumps(Adata,ensure_ascii= False).encode('utf-8'))
        outfile.write('\n'.encode('utf-8'))


