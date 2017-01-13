# 通过中图分类号，从CNKI中分析得到这个分类号对应的关键词排行

# 打开保存着中图分类号的文件
# -*- coding: utf-8 -*-

from urllib import parse
import httplib2
import json
from LearnModule import Func_StringSplit

# # 定义一个保存分类号数据源的类
class ZTNo_source(object):
    def __init__(self,sourcekw,sourceZTNo,sourceZTName):
        self.sourcekw = sourcekw
        self.sourceZTNo = sourceZTNo
        self.sourceZTName = sourceZTName

    def get_kw(self):
        return self.sourcekw

    def get_ZTNo(self):
        return self.sourceZTNo

    def get_ZTName(self):
        return self.sourceZTName

ZTNo_List = []  #定义一个存储分类号的列表
fline_split = []
# ZT_ClassNO_Temp = []
# ClassNO_Split = []
test_txt_temp = []
# ZT_Class_dict = {}
with open('C:/Users/flyingaura/Desktop/test.txt','rb') as init_file:
    for fline in init_file.readlines():
        # fline.strip()
        # print(fline)
        fline_decode = fline.decode('utf-8')
        # print(fline_decode)
        if(fline_decode.strip() != ''):
            test_txt_temp.append(fline_decode.strip())

# 对从文件中读出来的数据做处理
test_txt_temp.pop(0)
for key in test_txt_temp:
    fline_split.append(Func_StringSplit.stringsplit(key,'\t'))
for Kstring in fline_split:
    if(len(Kstring) == 1):
        ZTNo_List.append(ZTNo_source(Kstring[0],'',''))
    elif(len(Kstring) == 2):
        for ZTkey in Func_StringSplit.stringsplit(Kstring[1],';'):
            ZTNo_List.append(ZTNo_source(Kstring[0],ZTkey,''))
    else:
        ZTNo_temp = Func_StringSplit.stringsplit(Kstring[1], ';')
        ZTNo_name = Func_StringSplit.stringsplit(Kstring[2], ';')
        for i in range(len(ZTNo_temp)):
            if (i < len(ZTNo_name)):
                ZTNo_List.append(ZTNo_source(Kstring[0],ZTNo_temp[i],ZTNo_name[i]))
            else:
                ZTNo_List.append(ZTNo_source(Kstring[0], ZTNo_temp[i], ''))

# 调用搜索接口
headerdata = {"Content-type": "application/x-www-form-urlencoded"}
conn = httplib2.HTTPConnectionWithTimeout("192.168.10.9", 9095, timeout=120)
# 设置接口参数
data = {
        'tableNames': 'cnki_analyze_test',
        'size': 200,
        # 'query': 'ZT_classNo_list:A81',
        'field': 'keyword_list'
    }
# 把要取值的字段名称取出来
field_query = Func_StringSplit.stringsplit(data['field'], ':')[0]

 # 把结果写回到文件
ZT_query = []
ZTNo_Name = {}
with open('C:/Users/flyingaura/Desktop/CNKI_Keywords.txt', 'w') as result_file:
    # 开始分析
    i = 1  #计数器
    for ZTvalue in ZTNo_List:
        if(ZTvalue.get_ZTNo() == ''):
            ZT_query.append((Func_StringSplit.stringsplit(ZTvalue.get_kw(),';')[0],'--无分类号--'))
        else:
            # 把分类号和分类名称放入一个dict，是为了对分类号去重
            ZTNo_Name[ZTvalue.get_ZTNo()] = ZTvalue.get_ZTName()

    for key in ZTNo_Name:
        ZT_query.append((key,ZTNo_Name[key]))

    for ZTNo in ZT_query:
        print('=================== Analysis: %d ====================' % i)

        # 给query赋值，有分类号的取分类号，没有分类号的取第一个关键词
        if(ZTNo[1] == '--无分类号--' ):
            data['query'] = 'keyword_list:%s' % ZTNo[0]
        else:
            data['query'] = 'ZT_classNo_list:%s' % ZTNo[0]
        # if(ZTvalue.get_ZTNo() == ''):
        #     ZTkeyword = Func_StringSplit.stringsplit(ZTvalue.get_kw(),';')[0]
        #     data['query'] = 'keyword_list:%s' %ZTkeyword
        # else:
        #     data['query'] = 'ZT_classNo_list:%s' %ZTvalue.get_ZTNo()
        # 调用接口开始分析
        conn.request(method="POST", url="http://192.168.10.9:9095/api/MssSearchApi/aggregationsByQuery", headers=headerdata,
                     body=parse.urlencode(data))
        # 获取全部分析结果,转成json格式
        get_result = json.loads(conn.getresponse().read().decode('utf-8'))
        # 把需要的关键词和词频值从结果中取出来
        result_list = get_result['obj']['aggregations'][field_query]['buckets']
        # 取出本次分析所用时间
        result_time = float(get_result['obj']['took']/1000)
        # 把关键词和词频数取出来保存成一个key:value对
        result_data = []
        for resultkey in result_list:
            result_data.append((resultkey['key'],resultkey['doc_count']))
        # 将关键词和词频数对，按词频排序
        # result_SortedList = sorted(result_data.items(),key = lambda item:item[1],reverse = True)
        # 把一条结果输出到文件的一块区域
        result_file.write('================================== Analysis:%d | use time: %f s==================================\n' %(i,result_time))
        result_file.write(ZTNo[0] + ' : ' + ZTNo[1] + '\n')
        result_file.write('前 %d 关键词：\n' % data['size'])
        for resultkey in result_data:
            result_file.write(resultkey[0] + '( %d )' % resultkey[1] + '   ')
        result_file.write('\n\n')
        print('=================== Analysis: %d end !====================' % i)
        i = i + 1
        # All_result.append(hotkeyword(CNo,ZT_Class_dict[CNo],result_data))
    # valuelist = []














