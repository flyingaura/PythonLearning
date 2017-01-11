'数字型字符串转换为数字的模块'

__author__ = 'weil'
# -*- coding: utf-8 -*-

from functools import reduce

# 初始化一个数字字符对应字典
NumberList = {}
i = 0
for key in '0123456789':
    NumberList[key] = i
    i = i + 1


def fn_multip(x,y):
    return x * 10 + y

def str2int(str):
    NumList = []
    for key in str:
        NumList.append(NumberList[key])
    Outint = reduce(fn_multip,NumList)
    return Outint




