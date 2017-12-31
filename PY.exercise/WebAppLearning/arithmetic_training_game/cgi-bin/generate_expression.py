# -*- coding: utf-8 -*-
"""
这是一个生成算术表述式并进行计算的页面
"""

import arithmetic_training_games as ATG
import cgi,json,yate,time,os
from collections import OrderedDict

# ================= 生成运算表达式 =================
form_data = cgi.FieldStorage()   #取表单中传递过来的值

RecordFilePath = 'data/WrongRecord.json'   #指定错误题目记录文件路径
NewSettingTag = int(form_data['NewSetting'].value)    #取出开始计算标识（第一次为1，以后为0）
# ================= 下面是生成运算表达式的参数 =================
MaxNum = int(form_data['numlist'].value)
Numlist = list(range(MaxNum))   #取值，生成最大计算数范围
if(isinstance(form_data['operator'],list)):
    OperatorList = [x.value for x in form_data['operator']]  #取值 ，生成运算符列表
else:
    OperatorList = [form_data['operator'].value]
CalLevel = int(form_data['level'].value)   #取值，生成最大计算数个数

# ================= 生成表达式 =================
try:
    ArithmeticExpress = form_data['ArithmeticExpress'].value      #错题或空答案提交时要重复做的题
    FactResult = form_data['FactResult'].value          #同步取出表达式的计算结果
except KeyError:                #第一次或重新生成计算题
    while (True):
        ArithmeticExpress = ATG.ArithmeticMode(Numlist, OperatorList, CalLevel).get_ArtExpress()
        try:
            FactResult = eval(ArithmeticExpress)
            if (0 <= FactResult <= MaxNum):
                break
        except ZeroDivisionError:
            continue

# =================第一次进入页面，把表达式配置信息保存到一个文件里=================
if(NewSettingTag):               #第一次进入计算页面
    # ===================初始化各种参数===================
    ExpNum = 1   # 设置题号，从1开始
    RightAnsNum = 0  # 设置正确的答题数量
    WrongNum = 0  # 设置答错的题数
    WrongTag = 0  # 设置答错的标识（同一道题，最多只记一次答错）
    CorrectNum = 0  # 设置纠正后的题目数量
    NewSettingTag = 0    #设置新页面标识为否
    # ==================================================
    with open('data/setting.json', mode = 'w', encoding= 'utf-8') as settingfile:
        json.dump({'numlist':form_data['numlist'].value, 'operator': OperatorList, 'level': form_data['level'].value}, settingfile)

    header_string1 = '开始算术训练！'

else:                  #持续提交答案，进行答案判断
    # ================= 下面是做计算判断和持续训练的参数 =================
    ExpNum = int(form_data['ExpNum'].value)    #取出题号
    WrongNum = int(form_data['WrongNum'].value)   #取出答错题目数量
    WrongTag = int(form_data['WrongTag'].value)   #取出答错题目标识
    CorrectNum = int(form_data['CorrectNum'].value)  #取出纠正后的题目数量
    RightAnsNum = int(form_data['RightAnsNum'].value)
    try:
        if (int(form_data['CalResult'].value) == int(FactResult)):
            # action_URL = 'generate_expression.py'
            header_string1 = '<font color="#009966">恭喜你，答对了! 请继续回答下一题</font>'
            while (True):
                ArithmeticExpress = ATG.ArithmeticMode(list(range(MaxNum)), OperatorList, CalLevel).get_ArtExpress()
                try:
                    FactResult = eval(ArithmeticExpress)
                    if (0 <= FactResult <= MaxNum):
                        break
                except ZeroDivisionError:
                    continue
            # submit_string = '下一题'
            # re_answer_tag = 0
            if (WrongTag):
                CorrectNum += 1
            else:
                RightAnsNum += 1
            ExpNum += 1
            WrongTag = 0

        else:
            # action_URL = 'judge_result.py'
            header_string1 = '<font color="#FF6600">答错了，您再好好想想再重新回答!</font>'

            # re_answer_tag = 1
            if (not WrongTag):
                WrongNum = int(form_data['WrongNum'].value) + 1
                WrongTag = 1
                if (not os.path.isfile(RecordFilePath)):
                    with open(RecordFilePath, mode='w', encoding='utf-8') as RecordFile:
                        pass
                with open(RecordFilePath, mode='r+', encoding='utf-8') as RecordFile:
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

    except KeyError:             #提交空答案时
        try:
            if(form_data['RegenerationTag'].value == '1'):
                header_string1 = '<font color="#336699">重新生成题目如下：</font>'
                if(WrongTag):
                    ExpNum += 1
                    WrongTag = 0
            else:
                header_string1 = '请输入计算结果再提交！'
        except KeyError:
            header_string1 = '请输入计算结果再提交！'
    except ValueError:
        header_string1 = '输入答案必须为数字，请输入正确格式的答案！'

# =================生成一个HTML页面=================
print(yate.start_response())
print(yate.include_header('欢迎来到韦浩宇的算术运算训练营！'))
# print(yate.start_form('arithmetic_training_games.py'))
print(yate.header(header_string1, 2))
print(yate.header('第 %d 题  ----> 已答对<font color = "green"> %d </font>题，答错<font color="red"> %d </font>题（已纠正 <font color="blue"> %d </font>题）'
                  %(ExpNum, RightAnsNum, WrongNum, CorrectNum), 4))
print(yate.start_form('generate_expression.py'))

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
print(yate.input_hidden('NewSetting', NewSettingTag))   #设置是否为新设置的标识（其他页面为0）
print(yate.input_hidden('RightAnsNum', RightAnsNum))
print(yate.input_hidden('RegenerationTag', 0))

#===========================================================

print(yate.header('%s' %(ArithmeticExpress + ' = &nbsp;&nbsp;' + yate.create_inputs('CalResult',style='input_control')), 2))

print(yate.end_form('提交', 'sub'))

# =================<换一题>表单提交=================
print(yate.start_form('generate_expression.py'))
# =================在页面上记录之前的设置参数=================
print(yate.input_hidden('numlist', form_data['numlist'].value))
for Operator in OperatorList:
    print(yate.input_hidden('operator', Operator))
print(yate.input_hidden('level', form_data['level'].value))
print(yate.input_hidden('ExpNum', ExpNum))
print(yate.input_hidden('WrongNum', WrongNum))
print(yate.input_hidden('WrongTag', WrongTag))
print(yate.input_hidden('CorrectNum', CorrectNum))
print(yate.input_hidden('NewSetting', NewSettingTag))
print(yate.input_hidden('RightAnsNum', RightAnsNum))
print(yate.input_hidden('RegenerationTag', 1))

print(yate.end_form('换一题', 'sub'))

# =====================设置页脚的链接（保持固定顺序）=====================
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['错题回顾'] = 'WrongRecord.py'
print(yate.include_footer(FooterString))



