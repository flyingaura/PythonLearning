# -*- coding: utf-8 -*-
"""
这是一个生成算术表述式的脚本
"""

import arithmetic_training_games as ATG
import yate
import cgi

form_data = cgi.FieldStorage()

if(isinstance(form_data['operator'],list)):
    OperatorList = [x.value for x in form_data['operator']]
else:
    OperatorList = form_data['operator'].value

print(yate.start_response())
print(yate.include_header('这是查看结果页面'))
print(yate.header('%s'%('=' * 10 + '以下为测试结果' + '=' * 10),3))
print(yate.header(str(OperatorList)))


footer_string = '=' * 10 + '结束' + '=' * 10

print(yate.include_footer({footer_string:''}))