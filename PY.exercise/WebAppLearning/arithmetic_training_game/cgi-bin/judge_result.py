# -*- coding: utf-8 -*-

import arithmetic_training_games as ATG
import json,time,os,yate,cgi
from collections import OrderedDict

# ===================获取表单值===================
form_data = cgi.FieldStorage()
ArithmeticExpress = form_data['ArithmeticExpress'].value

if (isinstance(form_data['operator'], list)):
    OperatorList = [x.value for x in form_data['operator']]  # 取值 ，生成运算符列表
else:
    OperatorList = [form_data['operator'].value]
FactResult = form_data['FactResult'].value
MaxNum = int(form_data['numlist'].value)
ExpNum = int(form_data['ExpNum'].value)
WrongNum = int(form_data['WrongNum'].value)
WrongTag = int(form_data['WrongTag'].value)
CorrectNum = int(form_data['CorrectNum'].value)

RecordFilePath = 'data/WrongRecord.json'   #指定错误题目记录文件路径
# ===================生成页面===================
print(yate.start_response())
print(yate.include_header('欢迎来到韦浩宇的算术运算训练营！'))

# print(yate.para('实际计算结果为：%s' %FactResult))
# ===========================================================
try:
    if(int(form_data['CalResult'].value) == int(FactResult)):
        action_URL = 'generate_expression.py'
        header_string1 = '计算结果:'
        header_string2 = '恭喜你，答对了!'
        submit_string = '下一题'
        re_answer_tag = 0
        if(WrongTag):
            CorrectNum += 1
        ExpNum += 1
        WrongTag = 0
    else:
        action_URL = 'judge_result.py'
        header_string1 = '计算结果:'
        header_string2 = '答错了，您再好好想想再重新回答!'
        submit_string = '提交'
        re_answer_tag = 1
        if(not WrongTag):
            WrongNum += 1
            WrongTag = 1
            if(not os.path.isfile(RecordFilePath)):
                with open(RecordFilePath, mode='w', encoding='utf-8') as RecordFile:
                    pass
            with open(RecordFilePath, mode = 'r+', encoding= 'utf-8') as RecordFile:
                Time_string = time.strftime('%Y-%m-%d', time.localtime(time.time()))
                try:
                    RecordJson = json.loads(RecordFile.read().strip())
                    RecordFile.seek(0)
                except json.decoder.JSONDecodeError:
                    RecordJson = {}
                try:
                    RecordJson[Time_string].append(ArithmeticExpress + ' = ?')
                except KeyError:
                    RecordJson[Time_string] = []
                    RecordJson[Time_string].append(ArithmeticExpress + ' = ?')

                json.dump(RecordJson, RecordFile)

except KeyError:

    # Numlist = list(range(MaxNum))
    # CalLevel = int(form_data['level'].value)
    # while (True):
    #     ArithmeticExpress = ATG.ArithmeticMode(Numlist, OperatorList, CalLevel).get_ArtExpress()
    #     try:
    #         FactResult = eval(ArithmeticExpress)
    #         if (0 <= FactResult <= MaxNum):
    #             break
    #     except ZeroDivisionError:
    #         continue
    action_URL = 'judge_result.py'
    header_string1 = '请输入计算结果再提交'
    header_string2 = ''
    submit_string = '提交'
    re_answer_tag = 1


if(header_string1):
    print(yate.header(header_string1,3))
print(yate.start_form(action_URL))
# =================在页面上记录上之前的设置参数=================
print(yate.input_hidden('numlist', form_data['numlist'].value))
for Operator in OperatorList:
    print(yate.input_hidden('operator', Operator))
print(yate.input_hidden('level', form_data['level'].value))
print(yate.input_hidden('ExpNum', ExpNum))
print(yate.input_hidden('WrongNum', WrongNum))
print(yate.input_hidden('WrongTag', WrongTag))
print(yate.input_hidden('CorrectNum', CorrectNum))
print(yate.input_hidden('NewSetting', 0))

if(re_answer_tag):
    print(yate.input_hidden('ArithmeticExpress', ArithmeticExpress))
    print(yate.input_hidden('FactResult', str(FactResult)))
#==============================记录完毕================================
    print(yate.header(
        '第 %d 题  ----> 已答对<font color = "green"> %d </font>题，答错<font color="red"> %d </font>题（已纠正 <font color="blue"> %d </font>题）'
        % (ExpNum, (ExpNum - WrongNum), WrongNum, CorrectNum), 4))
    print(yate.header('%s' % (ArithmeticExpress + ' = &nbsp;&nbsp;' + yate.create_inputs('CalResult')), 2))

print(yate.para(''))
if(header_string2):
    print(yate.header(header_string2, 1))

print(yate.end_form(submit_string))

# =================<换一题>表单提交=================
if(re_answer_tag):
    print(yate.start_form('generate_expression.py'))
    # =================在页面上记录上之前的设置参数=================
    print(yate.input_hidden('numlist', form_data['numlist'].value))
    for Operator in OperatorList:
        print(yate.input_hidden('operator', Operator))
    print(yate.input_hidden('level', form_data['level'].value))
    print(yate.input_hidden('ExpNum', ExpNum + 1))
    print(yate.input_hidden('WrongNum', WrongNum))
    print(yate.input_hidden('WrongTag', 0))
    print(yate.input_hidden('CorrectNum', CorrectNum))
    print(yate.input_hidden('NewSetting', 0))

    print(yate.end_form('换一题'))

# =====================设置页脚的链接（保持固定顺序）=====================
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['错题回顾'] = 'WrongRecord.py'
print(yate.include_footer(FooterString))
