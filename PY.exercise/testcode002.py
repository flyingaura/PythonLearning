# -*- coding: utf-8 -*-

#
# Nlist = []
# if(Nlist):
#     print('True')
# else:
#     print('False')
#
# Aset = {1,2,3,4}
#
# print(Aset.add(6),Aset)

# Letterlist = [chr(ascii_code) for ascii_code in range(ord('A'),ord('z') + 1)]
# # print(Letterlist)
#
# aa = slice(1,3)
# print(len([]))

import json

# with open('F:\documents\python\learning2017\ESP_project\data_news\origin_news.json', mode = 'r', encoding= 'utf-8') as infile:
#     for Aline in infile.readlines():
#         # Aline_decode = Aline.decode('utf-8').strip()
#         AlineJson = json.loads(Aline)
#         print(AlineJson)

# aa = {}
# bb = []
# for i in range(3):
#     aa['title'] = chr(ord('a') + i) * 3
#     aa['content'] = i * 2
#
#     bb.append(aa.copy())
#
# print(bb)
import json
# testdata = []
# with open('F:\documents\python\learning2017\ESP_project\data_news\origin_news.json', mode = 'rb') as infile:
#
#     for i in range(10):
#         Aline = infile.readline()
#         Aline_decode = Aline.decode('utf-8').strip()
#         testdata.append(Aline_decode)
#
# # for aline in testdata:
# #     print(aline)
#
# with open('F:/documents/python/learning2017/ESP_project/data_news/news_test.json',mode = 'wb') as outfile:
#     for Adata in testdata:
#         outfile.write(Adata.encode('utf-8'))
#         outfile.write('\n'.encode('utf-8'))


import json
import sys
import os
sys.path.append('F:/documents/python/learning2017/ESP_project/data_news')
from LearnModule import StringSplit
import Data_normalization
#
# deplist = ['总经理办公室','产品中心','研发中心','数据中心','销售中心','销售支持中心','项目开发与服务中心',
#            '质量保障部','综合事务部','人力资源部','财务部', '法务部']
#
# print(Data_normalization.SetDepartment(deplist))
#
# with open('F:/documents/python/learning2017/ESP_project/data_knowledge/knowledge_normalized.json', mode = 'rb') as outfile:
#     for aline in outfile.readlines():
#         aline_decode = aline.decode('utf-8').strip()
#         alineJson = json.loads(aline_decode)
#
#         if(len(alineJson['appendix_filenames']) == 1 or len(alineJson['appendix_filenames']) == 2
#            or len(alineJson['appendix_filenames']) == 3):
#             print(alineJson['appendix_filenames'],alineJson['appendix_URL'])

filename = 'i.ndex..html'
print(os.path.splitext(filename))