'定义一个字符串拆分的模块'
# -*- coding: utf-8 -*-

__author__ = 'Flyingaura_wl'
__edittime__ = '20170101'

import math
import functools

def stringsplit(strN,splitN):
    # strN:待拆分字符串
    # splitN:分隔符,可以多个
    i = 0
    strL = []
    for n in range(len(strN)):
        if((strN[n] in splitN)):
            if(i != n):       # 抛掉空串
                strL.append(strN[i:n])
            i = n+1
    if(i < n):
        strL.append(strN[i:])
    return strL

# stringOrigin = 'asdkfj,as23lwj,0129,ddd,1iasdfj,83484,sdkf,aaaddd,kfjdkj,'
# stringSP = stringsplit(stringOrigin,['j',','])
# print(stringSP)
# print('the origin string is :',stringOrigin)
# for n in stringSP:
#     print(n)


