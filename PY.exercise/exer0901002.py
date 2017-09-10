# -*- coding: utf-8 -*-

import math
import random

class Point(object):  #定义一个经纬度坐标类
    def __init__(self,x = 0.0,y = 0.0):
        self.x = x
        self.y = y

    def GetPoint(self):
        return (self.x,self.y)

    def Distance(self,Pinstance):
        return math.sqrt((self.x - Pinstance.x) **2 + (self.y - Pinstance.y) ** 2)

    def AngleDiff(self,Pinstance):
        Angle = math.atan2(self.y, self.x) - math.atan2(Pinstance.y, Pinstance.x)
        return Angle / math.pi * 180    #返回角度数

    def __str__(self):
        return '(%.4f,%.4f)' %(self.x,self.y)

# 将Point做为GPS的父类
class GPS(Point):

    def __init__(self, PointName = '', x = 0.0, y = 0.0, PointList = {}):
        self.PointName = PointName
        self.LocalPoint = Point(x,y)
        self.PointList = PointList

    def GetGPSinfo(self):
        return {self.PointName:self.LocalPoint.GetPoint()}

    def PointSave(self):
        self.PointList[self.PointName] = self.LocalPoint
        return self.PointList

    def Distance(self,GPSinstance):
        return self.LocalPoint.Distance(GPSinstance.LocalPoint)

    def AngleDiff(self,GPSinstance):
        return self.LocalPoint.AngleDiff(GPSinstance.LocalPoint)

    def __str__(self):
        return '%s: %s' %(self.PointName, self.LocalPoint)

PointList = {}
GPSList = []
# while(True):
#     Px = random.uniform(-180,180)
#     Py = random.uniform(-180,180)
#     print('当前导航点为：(%.4f,%.4f)' %(Px,Py))
#     PointName = input('输入当前导航点名称(q退出):' )
#     if(PointName.lower() == 'q'):
#         print('程序结束！')
#         break
#     NewGPS = GPS(PointName,Px,Py,PointList)
#     PointList = NewGPS.PointSave()
#     GPSList.append(NewGPS)
    # print(NewGPS)

for i in range(1,6):
    Px = random.uniform(-180, 180)
    Py = random.uniform(-90,90)
    PointName = str(i) * 3
    NewGPS = GPS(PointName, Px, Py, PointList)
    PointList = NewGPS.PointSave()
    GPSList.append(NewGPS)

for key in PointList:
    print('导航点： %s:%s' %(key,PointList[key]))

# print('所有导航点位置为：')
# for Apoint in GPSList:
#     print(Apoint)
#     # print(Apoint.GetGPSinfo())

MyPoint = input('输入你所在位置名称：')
MyGPSPoint = GPS(MyPoint,random.uniform(-180,180),random.uniform(-90,90))
print('我所在位置 %s: %s' %(MyGPSPoint.PointName,MyGPSPoint.LocalPoint))

for Apoint in GPSList:
    print('%s 和 %s 导航点间距离为：%.4f' % (MyGPSPoint.PointName,Apoint.PointName,MyGPSPoint.Distance(Apoint)))
    print('%s 和 %s 导航点偏差为：%.4f' %(MyGPSPoint.PointName,Apoint.PointName,MyGPSPoint.AngleDiff(Apoint)))

with open(r'F:\documents\python\learning2017\program data\GPS.dat', mode = 'w', encoding= 'utf-8') as outfile:
    outfile.write('所有导航点位置如下：\n')
    for key in PointList:
        outfile.write('%s\t%.4f\t%.4f\n' % (key, PointList[key].x, PointList[key].y))
    outfile.write('\n')
    outfile.write('我所在位置如下：\n')
    outfile.write('%s\t%.4f\t%.4f\n' % (MyGPSPoint.PointName,MyGPSPoint.LocalPoint.x,MyGPSPoint.LocalPoint.y))


