# 对模块的使用测试
# -*- coding: utf-8 -*-

import sys
import math
import functools
from LearnModule import Module_test
from LearnModule import Func_StringSplit
from LearnModule import StringAddValue

print('the module\'s note is :',Module_test.__doc__)
print('the module\'s author is :',Module_test.__author__)
print('the module\' edit time is : ', Func_StringSplit.__edittime__)
# Module_test.test()
StrList = 'aaa,acb.923asd,88sdfffdd.,sdfk__sldf,1sdfjjj,asiw2,ddd,AFD'
# 先进行字符串拆分
StrNList = Func_StringSplit.stringsplit(StrList, (',', 's'))
# 给每个字符串加上分隔符
for StrN in StrNList:
    print(StringAddValue.StringAddVal(StrN,'***'))

