# -*- coding: utf-8 -*-

import random
import json
import os
import sys
sys.path.append('F:/documents/python/learning2017/ESP_project/data_news')
from LearnModule import StringSplit,cal_date,cal_time
import Data_normalization

# ===============================================================
def SetPubtime(init_year,init_time,days,seconds):  #随机生成发布日期 2010-05-06 12:34:50
    Pubdata = cal_date.Cal_Data(init_year,days)
    Pubdata = Pubdata[0:4] + '-' + Pubdata[4:6] + '-' + Pubdata[6:]
    Pubtime = cal_time.cal_time(init_time,seconds)
    return Pubdata + ' ' + Pubtime

deplist = ['总经理办公室','产品中心','研发中心','数据中心','销售中心','销售支持中心','项目开发与服务中心',
           '质量保障部','综合事务部','人力资源部','财务部', '法务部']

title_tail = ['','(1)','(2)','(3)','_转载','研究报告','【供参考】','[内部资料]','（个人心得）','【来自XXXX】']

catlog = []
with open('F:/documents/python/learning2017/ESP_project/data_knowledge/学科分类22.dat', mode = 'rb') as infile:
    for aline in infile.readlines():
        catlog.append(aline.decode('utf-8').strip())

# ========== 获取知识的附件路径 ============
appendixfiles = os.listdir('E:/业务项目/Y.学习资料/EKP共享文档/2014年7月15日')
appendixfilesPath = []
appendixRelativePath = '/ESPnews/appendixfiles'
for afile in appendixfiles:
    appendixfilesPath.append(os.path.join('%s/%s' %(appendixRelativePath,afile)))
    # print(appendixfilesPath)
n = 0  #分配附件用的起始值

KLDataList = []
AKLdata = {}

with open('F:/documents/python/learning2017/ESP_project/data_knowledge/origin_knowledge.json', mode = 'rb') as outfile:
    for aline in outfile.readlines():
        aline_decode = aline.decode('utf-8').strip()
        alineJson = json.loads(aline_decode)
        for key in alineJson:
            if(key == 'answer'):
                alineStr = alineJson[key]
                while(True):
                    if(alineStr[0] == '('):
                        while(alineStr[0] != ')'):
                            alineStr = alineStr[1:]
                        alineStr = alineStr[1:]
                    else:
                        break
                AKLdata['content'] = alineStr
            elif(key == 'question'):
                AKLdata['title'] = alineJson[key]
            elif(key == 'author'):
                AKLdata['author'] = alineJson[key]
            elif(key == 'tags'):
                AKLdata['keywords'] = alineJson[key]
            elif(key == 'answer_time'):
                AKLdata['pubtime'] = StringSplit.stringsplit(alineJson[key],'T')[0]

            AKLdata['viewcounts'] = random.randint(0,83)
            AKLdata['subjectCat'] = Data_normalization.SetCatlog(catlog)
            AKLdata['belongdep'] = Data_normalization.SetDepartment(deplist)

            # ============以下为给该条新闻随机分配一个附件============
            appendixFilePath = Data_normalization.SetAppendixFiles(appendixfilesPath, n)
            if (appendixFilePath != ''):
                n = n + 1
                AKLdata['appendix_URL'] = appendixFilePath
                AKLdata['appendix_filenames'] = [os.path.basename(x) for x in appendixFilePath]
            else:
                AKLdata['appendix_URL'] = ''
                AKLdata['appendix_filenames'] = ''

        KLDataList.append(AKLdata.copy())
        # =======================以下为随机复制同类数据=============================================
        CopyIndex = random.randint(1, 10)
        if (CopyIndex % 3 == 0):
            CopyCount = random.randint(1, 4)
            # KLTailList = []
            # KLCopyNum = 0
            for i in range(CopyCount):
                KLTailIndex = random.randint(0, len(title_tail) + 4)
                if (KLTailIndex >= len(title_tail)):
                    KLTailIndex = 0
                # if (KLTailIndex not in KLTailList):
                AKLCopy = AKLdata.copy()
                AKLCopy['title'] = AKLdata['title'] + title_tail[KLTailIndex]
                AKLCopy['belongdep'] = Data_normalization.SetDepartment(deplist)
                if (AKLdata['pubtime']):
                    init_year = ''
                    for Adata in AKLdata['pubtime'].split(' ')[0].split('-'):
                        init_year = init_year + Adata
                    AKLCopy['pubtime'] = SetPubtime(int(init_year), '00:00:00', random.randint(0, 365), random.randint(0, 24 * 3600))
                else:
                    AKLCopy['pubtime'] = SetPubtime(20150101,'00:00:00',random.randint(0,730),random.randint(0,24 * 3600))

                AKLCopy['viewcounts'] = random.randint(0, 83)
                KLDataList.append(AKLCopy.copy())

print(len(KLDataList))
with open('F:/documents/python/learning2017/ESP_project/data_knowledge/knowledge_normalized.json', mode = 'wb') as outfile:
    for arecord in KLDataList:
        outfile.write(json.dumps(arecord, ensure_ascii= False).encode('utf-8'))
        outfile.write('\n'.encode('utf-8'))



