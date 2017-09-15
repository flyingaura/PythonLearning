# -*- coding: utf-8 -*-

import os
import random
import json
import sys
sys.path.append('F:/documents/python/learning2017/ESP_project/data_news')
from LearnModule import StringSplit,cal_date,cal_time
import Data_normalization


deplist = ['总经理办公室','产品中心','研发中心','数据中心','销售中心','销售支持中心','项目开发与服务中心',
           '质量保障部','综合事务部','人力资源部','财务部', '法务部']

file_tail = ['','(1)','(2)','(3)','_转载','研究报告','【供参考】','[内部资料]','（个人心得）','【来自XXXX】']

# AllPathList = os.walk(r'F:\documents\ESP产品开发用数据\ESP_files')
# FilePathList = []

# for Apath in AllPathList:
#     if(Apath[2] != []):
#         for Afile in Apath[2]:
#             # AfilePath = os.path.join(Apath[0],Afile)
#             FilePathList.append([Apath[0],Afile])
#             # print(AfilePath)
# # print(len(FilePathList))

def SetFileFormat(FileSuffix):
    fformatdict = {'word':['doc','docx','wps'],'PPT':['ppt','pptx','dps'],'excel':['xls','xlsx','et'],
                   'image':['bmp','gif','jpg','jpeg','tiff','psd','png','svg','pcx','dxf','wmf','emf','tga','eps'],
                   'audio':['CD','OGG','MP3','ASF','WMA','WAV','RM','REAL','APE','MIDI','VQF'],
                   'video':['aiff','avi','mov','mpeg','mpg','qt','ram','viv','ra','rmvb','asf','wmv','flv'],
                   'txt':['txt','rtf'],'webpage':['html','htm','asp','jsp','php','css','xml','xhtml','aspx'],
                   'Email':['eml'],'PDF':['pdf']
                   }
    for key in fformatdict:
        if(FileSuffix in fformatdict[key]):
            return key

    return 'others'

# ===============================================================
def FormatTime(xtime):
    Ftime = StringSplit.stringsplit(xtime,('T','Z'))
    return Ftime[0] + ' ' + Ftime[1]

# ===============================================================
def SetFileSize(filesize):
    if(filesize < 1024):
        return ('%d %s') %(filesize,'B')
    elif(filesize / 1024 < 1024):
        return ('%.2f %s') %(float(filesize / 1024), 'KB')
    elif(filesize / 1024 / 1024 < 1024):
        return ('%.2f %s') %(float(filesize / 1024 / 1024) ,'MB')
    else:
        return ('%.2f %s') % (float(filesize / 1024 / 1024 / 1024), 'GB')

# ===============================================================
def SetPubtime(init_year,init_time,days,seconds):  #随机生成发布日期 2010-05-06 12:34:50
    Pubdata = cal_date.Cal_Data(init_year,days)
    Pubdata = Pubdata[0:4] + '-' + Pubdata[4:6] + '-' + Pubdata[6:]
    Pubtime = cal_time.cal_time(init_time,seconds)
    return Pubdata + ' ' + Pubtime

# ===========================以下主程序====================================

FileRecord = {}
FileDataList = []
fileindex = 0
OriginFilePath = 'F:/documents/python/learning2017/ESP_project/data_files/origin_files.json'
# OriginFilePath = r'F:\documents\python\learning2017\ESP_project\data_files\files_test.json'
with open(OriginFilePath, mode = 'rb') as infile:
    DropCount = 0
    for aline in infile.readlines():
        aline_decode = aline.decode('utf-8').strip()
        alineJson = json.loads(aline_decode)
        AfileKey = alineJson.keys()

        if('文件名称' in AfileKey):
            FileRecord['filename'] = alineJson['文件名称']
        else:               #文件名为空的数据直接扔掉
            DropCount += 1
            continue
        # ===============================设置文件名相关属性==============================
        FileName = os.path.splitext(FileRecord['filename'])
        FileRecord['title'] = FileName[0]
        FileRecord['file_suffix'] = FileName[1].strip('.').lower()
        FileRecord['fileformat'] = SetFileFormat(FileRecord['file_suffix'])

        # ===============================设置文件路径相关属性==============================
        SetFilePath = StringSplit.stringsplit(alineJson['文件路径'],'\\')
        FilePath = ''
        for Apath in SetFilePath[1:]:
            FilePath = os.path.join(FilePath,Apath)
        FileRecord['fileURL'] = FilePath

        # ===============================设置文件所属分类==============================
        FileCat = ''
        for Apath in SetFilePath[2:-1]:
            FileCat = FileCat + '//' + Apath
        FileRecord['FilesCat'] = FileCat

        # ===============================设置文件其他属性==============================

        if('全文内容' in AfileKey):
            FileRecord['content'] = alineJson['全文内容'].strip()
        else:
            FileRecord['content'] = ''
        if('作者' in AfileKey):
            FileRecord['authors'] = alineJson['作者']
        else:
            FileRecord['authors'] = ''
        if('文件大小' in AfileKey):
            FileRecord['filesize'] = SetFileSize(int(alineJson['文件大小']))
        else:
            FileRecord['filesize'] = '0'

        if ('创建时间' in AfileKey):
            FileRecord['edittime'] = FormatTime(alineJson['创建时间'])
        else:
            FileRecord['edittime'] = ''
        if ('修改时间' in AfileKey):
            FileRecord['pubtime'] = FormatTime(alineJson['修改时间'])
        else:
            FileRecord['pubtime'] = SetPubtime(20150101, '00:00:00', random.randint(0, 730), random.randint(0, 24 * 3600))

        FileRecord['belongdep'] = Data_normalization.SetDepartment(deplist)
        FileRecord['viewcounts'] = random.randint(0,117)

            # fileindex += 1
        FileDataList.append(FileRecord.copy())

        # ====================================随机分配相似文件================================
        CopyIndex = random.randint(1,10)
        if(CopyIndex % 3 == 0):
            CopyCount = random.randint(1,5)
            # FileTailList = []
            # FileCopyNum = 0
            # while(FileCopyNum < CopyCount):
            for i in range(CopyCount):
                FileTailIndex = random.randint(0, len(file_tail) + 4)
                if(FileTailIndex >= len(file_tail)):
                    FileTailIndex = 0
                # if(FileTailIndex not in FileTailList):
                AFileCopy = FileRecord.copy()
                AFileCopy['title'] = AFileCopy['title'] + file_tail[FileTailIndex]
                AFileCopy['belongdep'] = Data_normalization.SetDepartment(deplist)
                if(FileRecord['edittime']):
                    # print(FileRecord['edittime'])
                    init_year = ''
                    for Adata in FileRecord['edittime'].split(' ')[0].split('-'):
                        init_year = init_year + Adata
                    AFileCopy['edittime'] = SetPubtime(int(init_year),FileRecord['edittime'].split(' ')[1],random.randint(0,365),random.randint(0,24 * 3600))
                else:
                    AFileCopy['edittime'] = SetPubtime(20150101, '00:00:00', random.randint(0, 730), random.randint(0, 24 * 3600))
                if(FileRecord['pubtime']):
                    init_year = ''
                    for Adata in FileRecord['pubtime'].split(' ')[0].split('-'):
                        init_year = init_year + Adata
                    AFileCopy['pubtime'] = SetPubtime(int(init_year),FileRecord['pubtime'].split(' ')[1],random.randint(0,365),random.randint(0,24 * 3600))
                else:
                    AFileCopy['pubtime'] = AFileCopy['edittime']

                AFileCopy['viewcounts'] = random.randint(0, 117)

                FileDataList.append(AFileCopy.copy())
                # FileCopyNum += 1
                # FileTailList.append(FileTailIndex)


print('DropFiles Count = %d' %DropCount)
print('The total Files Count = %d' %(len(FileDataList)))
with open('F:/documents/python/learning2017/ESP_project/data_files/files_normalized.json', mode = 'wb') as outfile:
    for arecord in FileDataList:
        # arecord['content'] = ''
        outfile.write(json.dumps(arecord, ensure_ascii= False).encode('utf-8'))
        outfile.write('\n'.encode('utf-8'))


# with open('F:/documents/python/learning2017/ESP_project/data_files/files_normalized.json', mode = 'wb') as outfile:
#     for i in range(20):
#         outfile.write(json.dumps(FileDataList[i], ensure_ascii= False).encode('utf-8'))
#         outfile.write('\n'.encode('utf-8'))
