# -*- coding: utf-8 -*-

import os
import random
import json
import sys
# sys.path.append('F:/documents/python/learning2017/ESP_project/data_news')
from LearnModule import StringSplit
# import Data_normalization
#
#
# deplist = ['总经理办公室','产品中心','研发中心','数据中心','销售中心','销售支持中心','项目开发与服务中心',
#            '质量保障部','综合事务部','人力资源部','财务部', '法务部']
#
# AllPathList = os.walk(r'F:\documents\ESP产品开发用数据\ESP_files')
# FilePathList = []
#
# for Apath in AllPathList:
#     if(Apath[2] != []):
#         for Afile in Apath[2]:
#             # AfilePath = os.path.join(Apath[0],Afile)
#             FilePathList.append([Apath[0],Afile])
#             # print(AfilePath)
# # print(len(FilePathList))
#
# def SetFileFormat(FileSuffix):
#     fformatdict = {'word':['doc','docx','wps'],'PPT':['ppt','pptx','dps'],'excel':['xls','xlsx','et'],
#                    'image':['bmp','gif','jpg','jpeg','tiff','psd','png','svg','pcx','dxf','wmf','emf','tga','eps'],
#                    'audio':['CD','OGG','MP3','ASF','WMA','WAV','RM','REAL','APE','MIDI','VQF'],
#                    'video':['aiff','avi','mov','mpeg','mpg','qt','ram','viv','ra','rmvb','asf','wmv','flv'],
#                    'txt':['txt','rtf'],'webpage':['html','htm','asp','jsp','php','css','xml','xhtml','aspx'],
#                    'Email':['eml'],'PDF':['pdf']
#                    }
#     for key in fformatdict:
#         if(FileSuffix in fformatdict[key]):
#             return key
#
#     return 'others'
#
# # ===============================================================
# def FormatTime(xtime):
#     Ftime = StringSplit.stringsplit(xtime,('T','Z'))
#     return Ftime[0] + ' ' + Ftime[1]
#
# # ===============================================================
# def SetFileSize(filesize):
#     if(filesize < 1024):
#         return ('%d %s') %(filesize,'B')
#     elif(filesize / 1024 < 1024):
#         return ('%.2f %s') %(float(filesize / 1024), 'KB')
#     elif(filesize / 1024 / 1024 < 1024):
#         return ('%.2f %s') %(float(filesize / 1024 / 1024) ,'MB')
#     else:
#         return ('%.2f %s') % (float(filesize / 1024 / 1024 / 1024), 'GB')


FileRecord = {}
FileDataList = []
fileindex = 0
with open('F:/documents/python/learning2017/ESP_project/data_files/origin_files.json', mode = 'rb') as infile:
    for aline in infile.readlines():
        aline_decode = aline.decode('utf-8').strip()
        alineJson = json.loads(aline_decode)
        alineJson['全文内容'] = ''
        FileRecord = alineJson
        FileDataList.append(FileRecord.copy())

with open('F:/documents/python/learning2017/ESP_project/data_images/file_anothers.json', mode = 'wb') as outfile:
    for arecord in FileDataList:
        outfile.write(json.dumps(arecord, ensure_ascii= False).encode('utf-8'))
        outfile.write('\n'.encode('utf-8'))


# with open('F:/documents/python/learning2017/ESP_project/data_files/files_normalized.json', mode = 'wb') as outfile:
#     for i in range(20):
#         outfile.write(json.dumps(FileDataList[i], ensure_ascii= False).encode('utf-8'))
#         outfile.write('\n'.encode('utf-8'))
