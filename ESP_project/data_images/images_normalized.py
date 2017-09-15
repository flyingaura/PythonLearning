# -*- coding: utf-8 -*-

import os
import json
import random
from LearnModule import StringSplit,cal_time,cal_date

# 判断某个字母是否为汉字
def ischinese(s):
    if(s >= '\u4e00' and s <= '\u9fa5'):
        return True
    else:
        return False

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
def SetDepartment(deplist):   #从部门列表中随机分配一个所属部门
    index = random.randint(0,len(deplist) - 1)
    return deplist[index]

# ===============================================================
def FormatTime(xtime):
    Ftime = StringSplit.stringsplit(xtime,('T','Z'))
    return Ftime[0] + ' ' + Ftime[1]

# ===============================================================
def SetPubtime(init_year,init_time,days,seconds):  #随机生成发布日期 2010-05-06 12:34:50
    Pubdata = cal_date.Cal_Data(init_year,days)
    Pubdata = Pubdata[0:4] + '-' + Pubdata[4:6] + '-' + Pubdata[6:]
    Pubtime = cal_time.cal_time(init_time,seconds)
    return Pubdata + ' ' + Pubtime

# ===========================主程序====================================

deplist = ['总经理办公室','产品中心','研发中心','数据中心','销售中心','销售支持中心','项目开发与服务中心',
           '质量保障部','综合事务部','人力资源部','财务部', '法务部']

with open(r'F:\documents\python\learning2017\ESP_project\data_images\图片主题.txt', mode = 'rb') as infile:
    OutFiles = infile.readlines()

# ImageFilesName = os.walk(r'F:\documents\ESP产品开发用数据\ESP_images')
Findex = 0
FileRecord = {}
FileDataList = []
with open(r'F:\documents\python\learning2017\ESP_project\data_images\origin_images.json', mode = 'rb') as imagesfile:
    # OutImagesFiles = imagesfile.readlines()
    TotalCount = 0
    DropCount = 0
    for aline in imagesfile.readlines():
        aline_decode = aline.decode('utf-8').strip()
        alineJson = json.loads(aline_decode)
        AfileKey = alineJson.keys()

        if ('文件名称' in AfileKey):
            FileRecord['filename'] = alineJson['文件名称']
        else:  # 文件名为空的数据直接扔掉
            DropCount += 1
            continue
        # ===============================设置文件名相关属性==============================
        FileName = os.path.splitext(FileRecord['filename'])
        AfileName = FileName[0]
        if (ischinese(AfileName)):
            FileRecord['title'] = AfileName
        else:
            FileRecord['title'] = OutFiles[Findex].strip().decode('utf-8') + '_' + AfileName
            if(Findex < len(OutFiles) - 1):
                Findex += 1
            else:
                Findex = 0

        FileRecord['file_suffix'] = FileName[1].strip('.').lower()
        FileRecord['fileformat'] = FileRecord['file_suffix']

        # ===============================设置文件路径相关属性==============================
        SetFilePath = StringSplit.stringsplit(alineJson['文件路径'], '\\')
        FilePath = ''
        for Apath in SetFilePath[1:]:
            FilePath = os.path.join(FilePath, Apath)
        FileRecord['fileURL'] = FilePath

        # ===============================设置文件所属分类==============================
        FileCat = ''
        for Apath in SetFilePath[2:-1]:
            FileCat = FileCat + '//' + Apath
        FileRecord['FilesCat'] = FileCat

        # ===============================设置文件其他属性==============================

        if ('备注' in AfileKey):
            FileRecord['content'] = alineJson['备注'].strip()
        else:
            FileRecord['content'] = ''
        if ('作者' in AfileKey):
            FileRecord['authors'] = alineJson['作者']
        else:
            FileRecord['authors'] = ''
        if ('文件大小' in AfileKey):
            FileRecord['filesize'] = SetFileSize(int(alineJson['文件大小']))
        else:
            FileRecord['filesize'] = '0'

        if ('图像高度' in AfileKey and '图像宽度' in AfileKey):
            FileRecord['imagePixel'] = [int(alineJson['图像宽度'].split(' ')[0]),
                                        int(alineJson['图像高度'].split(' ')[0])]
        else:
            FileRecord['imagePixel'] = []

        if ('修改时间' in AfileKey):
            FileRecord['pubtime'] = FormatTime(alineJson['修改时间'])
        else:
            FileRecord['pubtime'] = SetPubtime(20150101, '00:00:00', random.randint(0, 730),
                                               random.randint(0, 24 * 3600))
        if ('拍摄日期' in AfileKey):
            FileRecord['edittime'] = alineJson['拍摄日期']
        else:
            FileRecord['edittime'] = FileRecord['pubtime']

        if('备注' in AfileKey):
            FileRecord['imagesdescription'] = alineJson['备注']
        else:
            FileRecord['imagesdescription'] = ''

        if ('相机型号' in AfileKey):
            FileRecord['imageSource'] = alineJson['相机型号']
        else:
            FileRecord['imageSource'] = ''

        FileRecord['belongdep'] = SetDepartment(deplist)
        FileRecord['viewcounts'] = random.randint(0, 163)

        TotalCount += 1
        FileDataList.append(FileRecord.copy())

print('处理文件总数为： %d' %TotalCount)
print('无效文件数量为： %d' %DropCount)

with open(r'F:\documents\python\learning2017\ESP_project\data_images\images_normalized.json', mode = 'wb') as outfile:
    for Aimage in FileDataList:
        outfile.write(json.dumps(Aimage,ensure_ascii= False).encode('utf-8'))
        outfile.write('\n'.encode('utf-8'))







