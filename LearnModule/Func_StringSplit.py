'定义一个字符串拆分的模块'
# -*- coding: utf-8 -*-

__author__ = 'Flyingaura_wl'
__edittime__ = '20170101'

import math
import functools

def stringsplit(strN,splitN):
    # strN:待拆分字符串
    # splitN:分隔符,可以多个
    if(not isinstance(strN,str)):
        return None
    i = 0
    strL = []
    for n in range(len(strN)):
        if((strN[n] in splitN)):
            if(i != n):       # 抛掉空串
                strL.append(strN[i:n])
            i = n+1
    if(i <= n):
        strL.append(strN[i:])
    return strL
#
# stringOrigin = '银行卡:7251,支付:4216,前绑定:3991,账户:2513,身份证:1845,姓名:1118,登录:1029,暂时:798,更改:724,ajf'
# print(stringOrigin[2:])
stringSP = stringsplit(None,['j',','])
# print(stringSP)
# print('the origin string is :',stringOrigin)
# for n in stringSP:
#     print(n)


