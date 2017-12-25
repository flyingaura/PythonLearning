# -*- coding: utf-8 -*-

"""
用来生成一个测试内容页面
"""

import yate
import cgi
from collections import OrderedDict

# # ================== 初始化一个操作符列表 ==================
# operatelist = ['+', '-', '*', '//']
# operatelist['add'] = '+'
# operatelist['subtract'] = '-'
# operatelist['multiply'] = '*'
# operatelist['divide'] = '//'
# # ================== 初始化完毕 ==================
# operatelist = ['+', '-', '*', '//']
operatelist1 = {'加号':'+', '减号':'-', '乘号':'*', '除号':'//'}
operatelist = {}
for key in operatelist1:
    operatelist[operatelist1[key]] = key

print(yate.start_response())
print(yate.include_header('这是一个WEB应用测试页面'))

print(yate.header('%s' %('=' *10 + '下面是测试内容' + '=' *10) , 3))
print(yate.start_form('test_content.py'))

# for Anoperator in operatelist:
#     print(yate.checked_box('operator',Anoperator))

print(yate.select_set('operator',operatelist,3,multiple = True))

print(yate.end_form('提交'))

footer_string = '=' * 10 + '结束' + '=' * 10

form_data = cgi.FieldStorage()
if(form_data):
    if (isinstance(form_data['operator'], list)):
        OperatorList = [x.value for x in form_data['operator']]
    else:
        OperatorList = form_data['operator'].value
    ShowData = str(OperatorList)
    print(yate.para(''))
    print(yate.header('%s' % ('=' * 10 + '以下为测试结果' + '=' * 10), 3))
    print(yate.header(ShowData, 3))


print(yate.include_footer({footer_string:''}))


