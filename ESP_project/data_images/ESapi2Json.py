# -*- coding: utf-8 -*-

from urllib import parse
import httplib2
import json
from LearnModule import StringSplit

headerdata = {"Content-type": "application/x-www-form-urlencoded"}
conn = httplib2.HTTPConnectionWithTimeout("192.168.10.9", 9095, timeout=120)
# 设置接口参数
data = {
        'tableNames': 'esp_images',
        'size': 500,
        # 'query': 'ZT_classNo_list:A81',
        # 'field': 'keyword_list'
    }


conn.request(method="POST", url="http://192.168.10.9:9095/api/MssSearchApi/searchByQuery", headers=headerdata,
                     body=parse.urlencode(data))
# 获取全部分析结果,转成json格式
get_result = json.loads(conn.getresponse().read().decode('utf-8'))

result_list = get_result['obj']['hits']['hits']

with open(r'F:\documents\python\learning2017\ESP_project\data_images\origin_images.json', mode = 'wb') as outfile:
    for Aresult in result_list:
        outfile.write(json.dumps(Aresult['_source'],ensure_ascii= False).encode('utf-8'))
        outfile.write('\n'.encode('utf-8'))