# -*- coding: utf-8 -*-
import random,csv,json
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
#

# infilepath = r'E:\业务项目\X.内部项目\国务院公文服务（罗斯福计划）项目\项目数据\最终数据\国务院新闻 for WeiLiang\gov.cn news refined-2017-10-25.csv'
# outfilepath = r'E:\业务项目\X.内部项目\国务院公文服务（罗斯福计划）项目\项目数据\最终数据\国务院新闻 for WeiLiang\govnews_struct.csv'
#
# datalist = []
# with open(infilepath, mode = 'r', encoding= 'utf-8') as infile:
#     for i in range(6):
#         datalist.append(infile.readline())
#
# print(len(datalist))
#
# with open(outfilepath, mode = 'w', encoding= 'utf-8') as outfile:
#     for Aline in datalist:
#         outfile.write(Aline)
# #         outfile.write('\n')
#
#
# astr = "{'pub_date': '发布日期', 'record_title_fp': 'record_title_fp', 'index_number': '索引号', 'datasource': '来源-new', 'symbol_of_document_lssuing': '文号', 'pubyear_f': '发布年份', 'accomplishment_date_of_document': '成文日期-refined', 'issuing_department_of_document': '单位', 'turnpages': '翻页链接', 'naviclassify': '页面导航', 'related_title': '相关标题', 'keywords': '主题词', 'text_of_document': '全文源码', 'pubtime': '发布时间', 'year_of_document_issuing': '年', 'twolevelclassify': '二级分类', 'related_titleURL': '相关标题链接', 'serial_number_of_document_issuing': '号', 'onelevelclassify': '一级分类', 'URI': 'record_id_uri', 'title': '标题', 'record_type': '文种', 'content': '全文', 'URL': 'URI'}"
# print(type(astr))
# print(json.dumps(astr))

aaa = '城乡建设、环境保护'
bbb = '城市规划'
try:
    onelevel = aaa
except:
    tofield = ''

else:
    try:
        twolevel = bbb
    except:
        tofield = onelevel

    else:
        if(not onelevel):
            tofield = ''
        else:
            if(twolevel):
                tofield = onelevel + '/' + twolevel
            else:
                tofield = onelevel

print(str(aaa.__str__()))