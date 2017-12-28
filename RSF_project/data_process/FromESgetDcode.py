# -*- coding: utf-8 -*-
# 通过ES获取公文文号，并对类种类型进行清洗

from urllib import parse
import httplib2
import json
from LearnModule import StringSplit

# outfilepath = r'F:\documents\python\learning2017\RSF_project\data\doctype.dat'

headerdata = {"Content-type": "application/x-www-form-urlencoded"}
conn = httplib2.HTTPConnectionWithTimeout("192.168.10.179", 9095, timeout=120)
# 设置接口参数
data = {
        'tableNames': 'officialdocs',
        'size': 5000,
        # 'query': 'title:石沉大海',
        'field': 'record_type'
    }


conn.request(method="POST", url="http://192.168.10.179:9095/api/MssSearchApi/searchByQuery", headers=headerdata,
                     body=parse.urlencode(data))
# 获取全部分析结果,转成json格式
get_result = json.loads(conn.getresponse().read().decode('utf-8'))

result_list = get_result['obj']['hits']['hits']
DocTypeList = []
splitstr = ['〔','第']
for Adata in result_list:
    # print(Adata['_source']['symbol_of_document_lssuing'])
    try:
        AdocType = StringSplit.stringsplit(Adata['_source']['symbol_of_document_lssuing'],splitstr)[0]
    except:
        AdocType = ''

    if(AdocType not in DocTypeList):
        print(Adata['_source']['symbol_of_document_lssuing'])
        DocTypeList.append(AdocType)

for Adata in DocTypeList:
    print(Adata)

