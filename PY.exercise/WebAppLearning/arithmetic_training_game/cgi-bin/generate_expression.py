# -*- coding: utf-8 -*-
"""
这是一个生成算术表述式并进行计算的页面
"""

import arithmetic_training_games as ATG
import yate
import cgi

# ================= 生成运算表达式 =================
form_data = cgi.FieldStorage()

try:
    MaxNum = int(form_data['numlist'].value)
    Numlist = list(range(MaxNum))   #取值，生成最大计算数范围

    if(isinstance(form_data['operator'],list)):
        OperatorList = [x.value for x in form_data['operator']]  #取值 ，生成运算符列表
    else:
        OperatorList = [form_data['operator'].value]

    CalLevel = int(form_data['level'].value)   #取值，生成最大计算数个数
    ArithmeticSettings = {'numlist':MaxNum, 'operator':OperatorList, 'level':CalLevel}
except KeyError:
    MaxNum = ArithmeticSettings['numlist']
    Numlist = list(range(MaxNum))
    OperatorList = ArithmeticSettings['operator']
    CalLevel = ArithmeticSettings['level']

# ArithmeticSettings = {'numlist':MaxNum, 'operator':OperatorList, 'level':CalLevel}

ArithmeticExpress = ATG.ArithmeticMode(Numlist, OperatorList, CalLevel).get_ArtExpress()

CalResult = eval(ArithmeticExpress)
while(CalResult < 0 or CalResult > MaxNum):
    ArithmeticExpress = ATG.ArithmeticMode(Numlist, OperatorList, CalLevel).get_ArtExpress()
    CalResult = eval(ArithmeticExpress)

# =================生成一个HTML页面=================
print(yate.start_response())
print(yate.include_header('欢迎来到韦浩宇的算术运算训练营！'))
# print(yate.start_form('arithmetic_training_games.py'))
print(yate.para('即将开始算术训练！'))
print(yate.start_form(''))
print(yate.header('%s' %(ArithmeticExpress + ' = &nbsp;&nbsp;' + yate.create_inputs('CalResult')), 3))
print(yate.end_form('提交'))

print(yate.para('%s' %('<---' + str(Numlist) + '>-----<' + str(OperatorList) + '>-----<' + str(CalLevel) + '---->')))
#
# try:
#     SubResult = int(cgi.FieldStorage()['CalResult'].value)
#     print(yate.para('%s%d' %('计算结果是：', SubResult)))
#     if(SubResult == CalResult):
#         print(yate.header('答对了！', 3))
#
#     else:
#         print(yate.header('答错了，请认真思考后重新答题'))
# except KeyError:
#     pass

print(yate.include_footer({'返回首页': '/index.html'}))



