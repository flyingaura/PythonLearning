# -*- coding: utf-8 -*-

import os
from LearnModule import StringSplit,MY_math
import random
import math

# AllPathList = os.walk(r'F:\documents\ESP产品开发用数据\ESP_files')
# FilePathList = []
#
# for Apath in AllPathList:
#     if(Apath[2] != []):
#         for Afile in Apath[2]:
#             # AfilePath = os.path.join(Apath[0],Afile)
#             FilePathList.append([Apath[0],Afile])
#             # FilePath = os.path.join(Apath[0],Afile)
#             # print(FilePath)
#
#
#             FilePathlist = StringSplit.stringsplit(Apath[0],'\\')
#             # print(FilePathlist[3:][::-1])
#
#             FilePath = ''
#             for xpath in FilePathlist[3:][::-1]:
#                 # print(xpath)
#                 FilePath = os.path.join(xpath,FilePath)
#                 # print(xpath,FilePath)
#             print(FilePath)
            # FilePath = lambda os.path.join(x,FilePath)

# def ischinese(s):
#     if(s >= '\u4e00' and s <= '\u9fa5'):
#         return True
#     else:
#         return False
#
# print(ischinese('1中a国人aa'))

# ImageFilesName = os.walk(r'F:\documents\ESP产品开发用数据\ESP_images')
#
# for afile in ImageFilesName:
#     print(afile)
# bb = []
# for i in range(3):
#     aa = []
#     aa.append(i)
#     bb.append(aa)
#
# print(bb)

# print(dir(list))

# alist = list()
# alist.justtest = 'aa'
# print(alist.justtest)
# print(alist)

# print(random.uniform(-180,180))

# print(type('1'))

# print(type(float) == type)

# a = 18
# # b = 84
# # print(MY_math.CalGCD(a,b))
# # print(MY_math.CalLCM(a,b))
#
# # print(random.random())
# RoleGroup = ['GeneralManager','ProductCenter','SalesCenter','R&DCenter','PMCenter',
#              'QMCenter','CorManager','F&ICenter']
#
# # for i in range(100):
# #     AllocatedACL = random.sample(RoleGroup,random.randint(1,len(RoleGroup)))
# #     if(AllocatedACL == []):
# #         print(i)
# AllocatedACL = random.sample(RoleGroup, random.randint(1, len(RoleGroup)))
# alist = list(range(10))
# alist.extend(AllocatedACL)
# print(alist)


from urllib import parse
import httplib2
import json

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

for Aresult in result_list:
    # print(Aresult['_source']['imagePixel'])
    print('%s: %s' %(Aresult['_id'],str(Aresult['_source']['imagePixel'])))
