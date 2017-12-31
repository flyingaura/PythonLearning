# -*- coding: utf-8 -*-

"""
用来选择配置算术表达式的页面
"""
import yate,json
from collections import OrderedDict


#==============初始化计算数值区间列表==============
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

# =================尝试从setting文件中读取已有配置=================
try:
    with open('data/setting.json', mode = 'r', encoding= 'utf-8') as settingfile:
        try:
            jsonstring = json.loads(settingfile.read().strip())
            numlist_checked = [jsonstring['numlist']]
            operator_checked = jsonstring['operator']
            level_checked = [jsonstring['level']]
        except json.decoder.JSONDecodeError:
            numlist_checked = []
            operator_checked = []
            level_checked = []

except FileNotFoundError:
    numlist_checked = []
    operator_checked = []
    level_checked = []

#==================设置一段JS代码用来区分同一个表单的两个不同提交指向=================

Form_JS = 'function FreeExerAction(){\
    document.name.action="generate_expression.py";\
    document.name.submit();\
}\
function ExamAction(){\
    document.name.action="exam.py";\
    document.name.submit();\
}'

# SubURLS = OrderedDict()
# SubURLS['自由练习'] = 'FreeExerAction()'
# SubURLS['进行测验'] = 'ExamAction()'

# =================生成一个HTML页面=================
print(yate.start_response())
print(yate.include_header_js('设置算术表达式的生成参数！', Form_JS))
print(yate.header('设置算术表达式的生成参数！', 1))
# print(yate.para('%s' %('=' * 10 + '请设置算术表达式的生成参数' + '=' * 10)))
print(yate.start_form('', 'name'))
print(yate.para('1.请设置计算值范围'))
print(yate.select_set('numlist',NumList, SelectedVals = numlist_checked))
print(yate.para('2.请设置训练用到的操作符'))
for key in OperatorList:
    checkedVal = False
    if(OperatorList[key] in operator_checked):
        checkedVal = True
    print(yate.checked_box('operator',OperatorList[key],key, checked = checkedVal))
print(yate.para('3.请设置计算数的个数'))
print(yate.select_set('level',NumLevel, SelectedVals = level_checked))
print(yate.input_hidden('NewSetting', 1))   #设置是否为新设置的标识（设置页面初始化为1）
# print(yate.input_hidden('StartCal', 1))    #设置开始计算训练标识
print(yate.para(''))
print(yate.subbutton('自由练习', 'FreeExerAction()',  'sub'))
print('&nbsp;' * 4)
print(yate.subbutton('进行测验', 'ExamAction()',  'sub'))
print('</form>')

# =====================设置页脚的链接（保持固定顺序）=====================
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['错题回顾'] = 'WrongRecord.py'
FooterString['测验回顾'] = 'ExamRecords.py'
print(yate.include_footer(FooterString))



