# -*- coding: utf-8 -*-
import json

def SetImageSizeType(width,height):
    ImageSizeTypeDict = {'小尺寸':[500,500],'中尺寸':[1000,1000],'大尺寸':[],
                         '壁纸尺寸':[(800,600),(1024,768),(1280,960),(1280,1024),(1600,1200),(1920,1080),(2560,1440),(2560,1600),(3840,2160)]}
    Dvalue = 10   #定义壁纸尺寸的误差范围

    if(width <= ImageSizeTypeDict['小尺寸'][0] and height <= ImageSizeTypeDict['小尺寸'][1]):
        IStype = ['小尺寸']
    elif((width <= ImageSizeTypeDict['小尺寸'][0] and (height > ImageSizeTypeDict['小尺寸'][1] and height <= ImageSizeTypeDict['中尺寸'][1]))
         or (height <= ImageSizeTypeDict['小尺寸'][1] and (width > ImageSizeTypeDict['小尺寸'][0] and width <= ImageSizeTypeDict['中尺寸'][0]))
         or (width <= ImageSizeTypeDict['中尺寸'][0] and height <= ImageSizeTypeDict['中尺寸'][1])):
        IStype = ['中尺寸']
    else:
        IStype = ['大尺寸']


    for VPair in ImageSizeTypeDict['壁纸尺寸']:
        if((width >= VPair[0] - Dvalue and width <=  VPair[0] + Dvalue)
            and (height >= VPair[1] - Dvalue and height <= VPair[1] + Dvalue)):
            IStype.append('壁纸尺寸')
            break
        if(width <=  VPair[0] - Dvalue or height <= VPair[1] - Dvalue):
            break

    return IStype

# print(SetImageSizeType(1600,1203))

with open(r'F:\documents\python\learning2017\ESP_project\data_images\images_normalized.json', mode = 'rb') as infile:
    for aline in infile.readlines():
        alineJson = json.loads(aline.decode('utf-8').strip())
        # print(alineJson['imagePixel'])
        if(alineJson['imagePixel'] != []):
            print(alineJson['imagePixel'])
            width = int(alineJson['imagePixel'][0])
            height = int(alineJson['imagePixel'][1])
            print(SetImageSizeType(width,height))