'给每个字符串加上一个默认串'
# -*- coding: utf-8 -*-
import functools

__author__ = 'Flyingaura_wl'

def StringAddVal(StrN,ValueN):
    StrValue = ValueN
    if(not isinstance(StrValue,str)):
        StrValue = str(ValueN)
    StrN = StrValue + StrN + StrValue
    return StrN