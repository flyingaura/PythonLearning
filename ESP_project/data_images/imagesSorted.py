# -*- coding: utf-8 -*-
"""
图片搜索结果根据页面宽度自适应排序算法
"""

from urllib import parse
import httplib2
import json

# 定义一个从一堆数中找出所加和最接近固定值要求的一种组合情况，采用递归方式
def OptClosedNum(datadict,FixedValue,Gap):  #datadic:数值字典，FixedValue:逼近值，Gap:允许误差
    ValueCount = 0
    resultDict = {}
    # AGroup = {}
    if(datadict == {}):
        print('bad exit!')
        return resultDict,datadict

    key0 = list(datadict.keys())[0]
    if(ValueCount + datadict[key0] < FixedValue - Gap):
        resultDict[key0] = datadict[key0]
        # print('The First ValueCount is : %d' % (ValueCount + resultDict[key0]))
        ValueCount = ValueCount + datadict[key0]
        datadict.pop(key0)
        # print('in < , resultDict :',end = '\t')
        # print(resultDict)
        # print('The Middle ValueCount is : %d and the rest FixedValue is : %d' % (ValueCount,FixedValue - ValueCount))
        resultDict.update(OptClosedNum(datadict,FixedValue - ValueCount, Gap)[0])
    elif(ValueCount + datadict[key0] > FixedValue):
        tempDict = {}
        tempDict[key0] = datadict[key0]
        datadict.pop(key0)
        # print('Pass here !')
        resultDict.update(OptClosedNum(datadict,FixedValue - ValueCount, Gap)[0])
        datadict[key0] = tempDict[key0]
    else:
        # print('The Good ValueCount is : %d' % (ValueCount + datadict[key0]))
        print('Good exit!')
        resultDict[key0] = datadict[key0]
        datadict.pop(key0)
        return resultDict, datadict

    # print('The finally ValueCount is : %d' %ValueCount)
    return resultDict, datadict



headerdata = {"Content-type": "application/x-www-form-urlencoded"}
conn = httplib2.HTTPConnectionWithTimeout("192.168.10.9", 9095, timeout=120)
# 设置接口参数
data = {
        'tableNames': 'esp_images',
        'size': 50,
        # 'query': 'ZT_classNo_list:A81',
        # 'field': 'keyword_list'
    }


conn.request(method="POST", url="http://192.168.10.9:9095/api/MssSearchApi/searchByQuery", headers=headerdata,
                     body=parse.urlencode(data))
# 获取全部分析结果,转成json格式
get_result = json.loads(conn.getresponse().read().decode('utf-8'))

result_list = get_result['obj']['hits']['hits']

# for Aresult in result_list:
#     print(Aresult['_source']['imagePixel'])

fixedheight = 200
Alinelength = 1200
gap = 20    #页面宽度的允许误差
RestData = {}
FullScreenRows = 10

with open(r'F:\documents\python\learning2017\ESP_project\data_images\imagesSorted.dat', mode = 'w') as outfile:
    DataDict = {}
    # icount = 0
    for Aresult in result_list:
        if(Aresult['_source']['imagePixel'] != []):
            # icount += 1
            Aimagelength =int(fixedheight * Aresult['_source']['imagePixel'][0] / Aresult['_source']['imagePixel'][1])
            DataDict[Aresult['_id']] = Aimagelength
    # print('the total imageFiles is : %d' %icount)
    # ImagesCount = 0
    NowRows = 0
    DataDictBackup = {}
    FactAlineLength = 0
    while(DataDict and NowRows < FullScreenRows):
        DataDictBackup = DataDict.copy()
        AlineData, DataDict = OptClosedNum(DataDict,Alinelength,gap)
        # ImagesCount += len(AlineData)
        # print('See the Result:', end = '\t')
        # print(AlineData)
        FactAlineLength = 0
        for key in AlineData:
            FactAlineLength += AlineData[key]
            for Aresult in result_list:
                if(key == Aresult['_id']):
                    print('--[%s][%s][%s]--' % (Aresult['_id'],Aresult['_source']['title'], Aresult['_source']['fileURL']))
                    outfile.write('--[%s][%s][%s]--' % (Aresult['_id'],Aresult['_source']['title'], Aresult['_source']['fileURL']))
        outfile.write('\n')
        NowRows += 1
        print('FactAlineLength = %d' %FactAlineLength)
        # print(DataDictBackup)

    if(NowRows == FullScreenRows):
        RestData = DataDict
    else:
        if(FactAlineLength < Alinelength - gap):
            print('pass here')
            RestData = DataDictBackup
            print(RestData)



# print(ImagesCount)
    #     outfile.write('%s%s%s' %('=' * 20,' 下一页 ','=' * 20))
    # if(AlineList != []):
    #     next_result_list.extend(AlineList)
    # for Aimage in next_result_list:
    #     outfile.write('--[%s][%s]--' % (Aimage['title'], Aimage['fileURL']))
    # outfile.write('\n')





