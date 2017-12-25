# -*- coding: utf-8 -*-

"""
用来选择配置算术表达式的页面
"""
import yate
from collections import OrderedDict


#===========初始化计算数值区间列表==============
NumList = OrderedDict()
for i in range(1,11):
    Anum = i * 10
    NumList[str(Anum)] = str(Anum)

#===========初始化运算符列表==============
OperatorList = OrderedDict()
OperatorList['加号'] = '+'
OperatorList['减号'] = '-'
OperatorList['乘号'] = '*'
OperatorList['除号'] = '/'

#===========初始化计算数个数列表==============
NumLevel = OrderedDict()
for i in range(2,6):
    NumLevel[str(i)] = str(i)

# =================生成一个HTML页面=================
print(yate.start_response())
print(yate.include_header('设置算术表达式的生成参数！'))
print(yate.para('%s' %('=' * 10 + '请设置算术表达式的生成参数' + '=' * 10)))
print(yate.start_form('generate_expression.py'))
print(yate.para('1.请设置计算值范围'))
print(yate.select_set('numlist',NumList,5))
print(yate.para('2.请设置训练用到的操作符'))
for key in OperatorList:
    print(yate.checked_box('operator',OperatorList[key],key))
print(yate.para('3.请设置计算数的个数'))
print(yate.select_set('level',NumLevel,3))

print(yate.end_form('确定'))
print(yate.include_footer({'返回首页':'/index.html'}))



