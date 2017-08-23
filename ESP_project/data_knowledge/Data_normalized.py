# -*- coding: utf-8 -*-

import random
import json
import os
import sys
sys.path.append('F:/documents/python/learning2017/ESP_project/data_news')
from LearnModule import StringSplit
import Data_normalization

deplist = ['总经理办公室','产品中心','研发中心','数据中心','销售中心','销售支持中心','项目开发与服务中心',
           '质量保障部','综合事务部','人力资源部','财务部', '法务部']

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

with open('F:/documents/python/learning2017/ESP_project/data_knowledge/knowledge_normalized.json', mode = 'wb') as outfile:
    for arecord in KLDataList:
        outfile.write(json.dumps(arecord, ensure_ascii= False).encode('utf-8'))
        outfile.write('\n'.encode('utf-8'))



