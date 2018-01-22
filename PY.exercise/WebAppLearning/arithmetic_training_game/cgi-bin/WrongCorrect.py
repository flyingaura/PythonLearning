#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi, yate, cgitb, json
from collections import OrderedDict

cgitb.enable()

form_data = cgi.FieldStorage()

#==================== 定义一个把json字符串转换为json对象的js ====================
JS_string = ''
#==================== 输出错题页面 ====================
print(yate.start_response())
print(yate.include_header_js('欢迎来到韦浩宇的算术运算训练营！', JS_string))
print(yate.header('<span style="color:#ff6666">赶紧对错题进行更正吧！</span>', 2))

# 从表单中获取错题：
try:
    # print(yate.para(form_data['WrongQuestions'].value))
    WrongQuestionList = json.loads(form_data['WrongQuestions'].value)
    # print(yate.para(json.dumps(form_data['WrongQuestions'].value)))
    for AnExamNum in sorted([int(x) for x in WrongQuestionList.keys()]):
        print(yate.header('<span class="specfont">%d.</span>&nbsp;&nbsp;&nbsp;&nbsp;%s'
                          % (AnExamNum, WrongQuestionList[str(AnExamNum)][0] + ' = &nbsp;&nbsp;' + yate.create_inputs(str(AnExamNum), style='input_control')), 2))
except KeyError:
    print(yate.header('没有错题', 2))
except json.JSONDecodeError:
    print(yate.header('无法读取错题数据，请重试', 2))

# 从表单中获取奖励值：
try:
    AwardCount = form_data['AwardCount'].value
except KeyError:
    AwardCount = '没有获取到奖励值'
except json.JSONDecodeError:
    AwardCount = '没有获取到奖励值'

# =====================设置页脚的链接（保持固定顺序）=====================
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['考题回顾'] = 'ExamRecords.py'
AwardString = yate.img_tag('/images/奖励.png') + '<span style="font-weight:bolder;color:#FF6666;"> × %s</span>' % AwardCount\
              + '&nbsp;&nbsp;<span style="font-weight:bolder;color:#FF6666;">兑换奖励</span>'
FooterString[AwardString] = 'AwardTable.py'
print(yate.include_footer(FooterString))