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
AimageFile = {}
imagesFilesList = []
deplist = ['总经理办公室','产品中心','研发中心','数据中心','销售中心','销售支持中心','项目开发与服务中心',
           '质量保障部','综合事务部','人力资源部','财务部', '法务部']

with open(r'F:\documents\python\learning2017\ESP_project\data_images\图片主题.txt', mode = 'rb') as infile:
    OutFiles = infile.readlines()

ImageFilesName = os.walk(r'F:\documents\ESP产品开发用数据\ESP_images')
Findex = 0
with open(r'F:\documents\python\learning2017\ESP_project\data_images\origin_images.json', mode = 'rb') as imagesfile:
    # OutImagesFiles = imagesfile.readlines()
    for IFile in ImageFilesName:
        if(IFile[2] != []):
            for Afile in IFile[2]:
                AimageFile['filename'] = Afile
                AFileName, AFileSuffix = os.path.splitext(Afile)
                if (ischinese(Afile)):
                    AimageFile['title'] = AFileName
                else:
                    AimageFile['title'] = OutFiles[Findex].strip().decode('utf-8') + '_' + AFileName

                AimageFile['file_suffix'] = AFileSuffix.strip('.')

                FilePathSet = StringSplit.stringsplit(IFile[0], '\\')
                FilePath = ''
                FilesCat = ''
                for xpath in FilePathSet[3:]:
                    FilePath = os.path.join(FilePath, xpath)
                for xpath in FilePathSet[4:]:
                    FilesCat = FilesCat + '//' + xpath

                AimageFile['fileURL'] = os.path.join(FilePath,Afile)
                AimageFile['FilesCat'] = FilesCat
                AimageFile['belongdep'] = SetDepartment(deplist)
                AimageFile['viewcounts'] = random.randint(0,163)
                if(Findex < len(OutFiles) - 1):
                    Findex = Findex + 1
                else:
                    Findex = 0
                OutImagesFile = imagesfile.readline().strip()
                if(OutImagesFile):
                    OutImagesJson = json.loads(OutImagesFile.decode('utf-8'))
                    keylist = OutImagesJson.keys()
                    AimageFile['content'] = OutImagesJson['备注']
                    AimageFile['authors'] = OutImagesJson['作者']
                    AimageFile['filesize'] = SetFileSize(int(OutImagesJson['文件大小']))
                    if('图像高度' in keylist and '图像宽度' in keylist):
                        AimageFile['imagePixel'] = [int(OutImagesJson['图像宽度'].split(' ')[0]), int(OutImagesJson['图像高度'].split(' ')[0])]
                    else:
                        AimageFile['imagePixel'] = []
                    if(OutImagesJson['修改时间']):
                        AimageFile['pubtime'] = FormatTime(OutImagesJson['修改时间'])
                    else:
                        AimageFile['pubtime'] = SetPubtime(20150101,'00:00:00',random.randint(0,730),random.randint(0,24 * 3600))
                    AimageFile['imagesdescription'] = OutImagesJson['备注']
                    AimageFile['fileformat'] = AimageFile['file_suffix']
                    if('相机型号' in keylist):
                        AimageFile['imageSource'] = OutImagesJson['相机型号']
                    else:
                        AimageFile['imageSource'] = '未知'
                    if ('拍摄日期' in keylist):
                        AimageFile['edittime'] = OutImagesJson['拍摄日期']
                    else:
                        AimageFile['edittime'] = AimageFile['pubtime']

                imagesFilesList.append(AimageFile.copy())

with open(r'F:\documents\python\learning2017\ESP_project\data_images\images_normalized.json', mode = 'wb') as outfile:
    for Aimage in imagesFilesList:
        outfile.write(json.dumps(Aimage,ensure_ascii= False).encode('utf-8'))
        outfile.write('\n'.encode('utf-8'))







