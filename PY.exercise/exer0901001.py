# -*- coding: utf-8 -*-

import math

class point(object):
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def distance(self,Pinstance):
        return math.sqrt((self.x - Pinstance.x) ** 2 + (self.y - Pinstance.y) ** 2)

    def sum(self,Pinstance):
        return point((self.x + Pinstance.x), (self.y + Pinstance.y))

    def __str__(self):
        return '(%.3f,%.3f)' %(self.x,self.y)

P1 = point(y = 5)
P2 = point(4,9)

print('第1个点坐标为：%s' %P1)
print('第2个点坐标为：%s' %P2)

print('两点间距离为: %f' %P1.distance(P2))
print('两点矢量和为: %s' %P1.sum(P2))