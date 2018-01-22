#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import yate,json,cgi
from collections import OrderedDict
import arithmetic_training_games as ATG

form_data = cgi.FieldStorage()   #取表单中传递过来的值

# ================= 下面是获取运算表达式的参数 =================
MaxNum = int(form_data['numlist'].value)
Numlist = list(range(MaxNum))   #取值，生成最大计算数范围
if(isinstance(form_data['operator'],list)):
    OperatorList = [x.value for x in form_data['operator']]  #取值 ，生成运算符列表
else:
    OperatorList = [form_data['operator'].value]
CalLevel = int(form_data['level'].value)   #取值，生成最大计算数个数

# =================第一次进入测验页面，把表达式生成参数保存到一个文件里=================
NewSettingTag = int(form_data['NewSetting'].value)   #取出开始计算标识（第一次为1，以后为0）
if(NewSettingTag):               #第一次进入测验页面
    # ===================初始化各种参数===================
    NewSettingTag = 0    #设置新页面标识为否
    # ==================================================
    with open('data/setting.json', mode = 'w', encoding= 'utf-8') as settingfile:
        json.dump({'numlist':form_data['numlist'].value, 'operator': OperatorList, 'level': form_data['level'].value}, settingfile)

# =================== 下面是生成这次的考试题（一共20道）===================
ExamList = {}
ExpNum = 1
ExamCount = 20
while(ExpNum <= ExamCount):
    while (True):
        ArithmeticExpress = ATG.ArithmeticMode(Numlist, OperatorList, CalLevel).get_ArtExpress()
        try:
            FactResult = eval(ArithmeticExpress)
            if (0 <= FactResult <= MaxNum):
                break
        except ZeroDivisionError:
            continue
    ExamList[ExpNum] = [ArithmeticExpress, FactResult]
    ExpNum += 1

# =================== 定义一段显示考试倒计时的代码 ===================
JS_string = 'var time=new Date();time.setHours(0);time.setMinutes(10);time.setSeconds(0);var downtime = 1;var timeOutText="";var totalseconds=0;' \
            'function countdown(){var timeshow=document.getElementById("timeshow");var hour=time.getHours();var min=time.getMinutes();var second=time.getSeconds();' \
            'setTimeout("countdown()",1000);totalseconds ++;if(downtime==1){time.setSeconds(second-1);timeshow.style.color="#0099CC";}' \
            'else{time.setSeconds(second+1);timeOutText="你已超时  ";timeshow.style.color="#CC0033";}if(hour=="0"&&min=="0"&&second=="1"){downtime=0;}' \
            'hour<10?hour="0"+hour:hour;min<10?min="0"+min:min;second<10?second="0"+second:second;timeshow.innerHTML=timeOutText+hour+":"+min+":"+second;' \
            'document.form.totaltime.value = totalseconds}var timer=setTimeout("countdown()",1000);'

# =================== 下面是生成考试页面 ===================

print(yate.start_response())
print(yate.include_header_js('欢迎来到韦浩宇的算术运算训练营！', JS_string))
# print(yate.start_form('arithmetic_training_games.py'))
print('<div id="topfixed">')
print(yate.header('欢迎来到韦浩宇的算术运算训练营！', 1))
print(yate.header('开始算术测验%s<span class="timeshow">开始计时：</span><span  id="timeshow" class="timeshow"></span>' % ('&nbsp;' * 8), 2))
print('</div>')
print('<div style="margin-top:125px">')
print(yate.start_form('exam_result.py', name='form'))

for key in sorted(ExamList.keys()):
    ExamData = 'ExamData' + str(key)   #在页面上记录本次考题和答案
    print(yate.input_hidden(ExamData, str(key)))
    print(yate.input_hidden(ExamData, ExamList[key][0]))
    print(yate.input_hidden(ExamData, str(ExamList[key][1])))
    print(yate.header('<span class="specfont">%d.</span>&nbsp;&nbsp;&nbsp;&nbsp;%s' %(key, ExamList[key][0] + ' = &nbsp;&nbsp;' + yate.create_inputs(ExamData, style='input_control')), 2))
# ================= 在页面上记录上之前的设置参数 =================
print(yate.input_hidden('numlist', form_data['numlist'].value))
for Operator in OperatorList:
    print(yate.input_hidden('operator', Operator))
print(yate.input_hidden('level', form_data['level'].value))
print(yate.input_hidden('ExamCount', ExamCount))               #把考试题目数量传过去
print(yate.input_hidden('NewSetting', NewSettingTag))
print(yate.input_hidden('totaltime'))                      #把考试用时传过去（由JS提供值）
# print(yate.para('新页面标识为：%s' % NewSettingTag))
# # ================= 在页面上记录本次考题和答案 =================
# ExpressListJson = json.dumps(ExamList)   #把考题列表转换为json字符串
# print(yate.input_hidden('ExpressListJson', ExpressListJson))
# print(yate.para(ExpressListJson))

#===========================================================

print(yate.end_form('完成提交', 'sub'))
print('</div>')

# =====================设置页脚的链接（保持固定顺序）=====================
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['测验回顾'] = 'ExamRecords.py'
print(yate.include_footer(FooterString))



