# -*-coding: utf-8 -*-
# 通过URL获取 搜狐新闻语料库.json 中的所有新闻主题
# URL:http://gongyi.sohu.com/20120620/n346094762.shtml
from LearnModule import StringSplit
import json

infilePath = r'F:\memory\python-learning\learning2017\ESP_project\data_news\搜狐新闻语料库.json'
outfilePath = r'F:\memory\python-learning\learning2017\ESP_project\data_news\NewsCalsses.json'
NewsCalsses = {}
TotalCount = 0
with open(infilePath, mode = 'r', encoding= 'utf-8') as infile:
    for aline in infile.readlines():
        TotalCount += 1
        try:
            alineJson = json.loads(aline.strip())
        except:
            print('OrderId:%d -- %s' %(TotalCount,aline))
        if('url' in alineJson.keys()):
            OneCalss = StringSplit.stringsplit(StringSplit.stringsplit(alineJson['url'],'/')[1],'.')[0]
        if(OneCalss not in NewsCalsses.keys()):
            NewsCalsses[OneCalss] = alineJson['url']

        if(TotalCount % 1000 == 0):
            print('===== %d =====' % TotalCount)

print('=====在 %d 条数据中,类型读取结束 %d 个新闻类型=====' % (TotalCount, len(NewsCalsses)))
with open(outfilePath, mode = 'w', encoding= 'utf-8') as outfile:
    for key in NewsCalsses:
        outfile.write('%s\t%s' %(key,NewsCalsses[key]))
        outfile.write('\n')



# for AClass in NewsCalsses:
#     print(AClass)
#
# print('TotalCount = %d' %TotalCount)
# print('TotalClass = %d' %(len(NewsCalsses)))