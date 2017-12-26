# -*- coding: utf-8 -*-
"""
这是一个生成算术表述式并进行计算的页面
"""

import arithmetic_training_games as ATG
import yate
import cgi
from collections import OrderedDict

# ================= 生成运算表达式 =================
form_data = cgi.FieldStorage()

MaxNum = int(form_data['numlist'].value)
Numlist = list(range(MaxNum))   #取值，生成最大计算数范围
ExpNum = int(form_data['ExpNum'].value)    #取出题号
WrongNum = int(form_data['WrongNum'].value)   #取出答错题目数量
WrongTag = int(form_data['WrongTag'].value)   #取出答错题目标识
CorrectNum = int(form_data['CorrectNum'].value)  #取出纠正后的题目数量

if(isinstance(form_data['operator'],list)):
    OperatorList = [x.value for x in form_data['operator']]  #取值 ，生成运算符列表
else:
    OperatorList = [form_data['operator'].value]

CalLevel = int(form_data['level'].value)   #取值，生成最大计算数个数

while(True):
    ArithmeticExpress = ATG.ArithmeticMode(Numlist, OperatorList, CalLevel).get_ArtExpress()
    try:
        FactResult = eval(ArithmeticExpress)
        if (0 <= FactResult <= MaxNum):
            break
    except ZeroDivisionError:
        continue

# =================生成一个HTML页面=================
print(yate.start_response())
print(yate.include_header('欢迎来到韦浩宇的算术运算训练营！'))
# print(yate.start_form('arithmetic_training_games.py'))
print(yate.para('即将开始算术训练！'))
print(yate.header('第 %d 题  ----> 已答对<font color = "green"> %d </font>题，答错<font color="red"> %d </font>题（已纠正 <font color="blue"> %d </font>题）'
                  %(ExpNum, (ExpNum - WrongNum - 1), WrongNum, CorrectNum), 4))
print(yate.start_form('judge_result.py'))

# =================在页面上记录上之前的设置参数=================
print(yate.input_hidden('numlist', form_data['numlist'].value))
for Operator in OperatorList:
    print(yate.input_hidden('operator', Operator))
print(yate.input_hidden('level', form_data['level'].value))
print(yate.input_hidden('ArithmeticExpress', ArithmeticExpress))
print(yate.input_hidden('FactResult', FactResult))
print(yate.input_hidden('ExpNum', ExpNum))
print(yate.input_hidden('WrongNum',WrongNum))
print(yate.input_hidden('WrongTag',WrongTag))
print(yate.input_hidden('CorrectNum', CorrectNum))

#===========================================================

print(yate.header('%s' %(ArithmeticExpress + ' = &nbsp;&nbsp;' + yate.create_inputs('CalResult')), 2))

print(yate.end_form('提交'))

# print(yate.add_space(5))
# =================<换一题>表单提交=================
print(yate.start_form('generate_expression.py'))
# =================在页面上记录之前的设置参数=================
print(yate.input_hidden('numlist', form_data['numlist'].value))
for Operator in OperatorList:
    print(yate.input_hidden('operator', Operator))
print(yate.input_hidden('level', form_data['level'].value))
print(yate.input_hidden('ExpNum', ExpNum))
print(yate.input_hidden('WrongNum', WrongNum))
print(yate.input_hidden('WrongTag', 0))
print(yate.input_hidden('CorrectNum', CorrectNum))

print(yate.end_form('换一题'))

# =====================设置页脚的链接（保持固定顺序）=====================
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['错题回顾'] = 'WrongRecord.py'
print(yate.include_footer(FooterString))



