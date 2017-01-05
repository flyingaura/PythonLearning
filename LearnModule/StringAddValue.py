'1、给每个字符串加上一个默认串的函数  2、把大写字母统一转换成小写字母的函数'
# -*- coding: utf-8 -*-
import functools

__author__ = 'Flyingaura_wl'

def StringAddVal(StrN,ValueN):
    StrValue = ValueN
    if(not isinstance(StrValue,str)):
        StrValue = str(ValueN)
    StrN = StrValue + StrN + StrValue
    return StrN


def StringLower(StrN):
    StrGap = ord('a') - ord('A')
    StrTemp = ''
    for n in StrN:
        StrNum = ord(n)
        if(StrNum in range(ord('A'),ord('Z')+1)):
            StrNum = StrNum + StrGap
        StrTemp = StrTemp + chr(StrNum)
        # print(chr(StrNum),StrN[n])

    return StrTemp

# print(StringLower('AAbbCCdd'))


