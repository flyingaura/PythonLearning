#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi, yate, cgitb, json
from collections import OrderedDict

cgitb.enable()

form_data = cgi.FieldStorage()

ShowWrongQuestions = []   #定义在HTML中展示错题的字符串
WQLeftTag = 0   #如果更正后仍有错题，则错题标记为1

AwardImageURL1 = '/images/对勾16_16.png'
AwardImageURL2 = '/images/星.png'

FilePath = 'data/ExamRecords.json'
# ====================== 从表单中获取本次全部错题 ======================
try:
    # print(yate.para(form_data['WrongQuestions'].value))
    WrongQuestionList = json.loads(form_data['WrongQuestions'].value)
    for AnExamNum in sorted([int(x) for x in WrongQuestionList.keys()]):
        try:
            if(int(form_data[str(AnExamNum)].value) == WrongQuestionList[str(AnExamNum)][1]):
                ShowWrongQuestions.append('<span class="specfont">%d.</span>&nbsp;&nbsp;&nbsp;&nbsp;%s = &nbsp;&nbsp;%s&nbsp;&nbsp;&nbsp;&nbsp;%s'
                                          % (AnExamNum, WrongQuestionList[str(AnExamNum)][0], WrongQuestionList[str(AnExamNum)][1], yate.img_tag(AwardImageURL1)))
                WrongQuestionList[str(AnExamNum)][2] = 1

            else:
                ShowWrongQuestions.append('<span class="specfont">%d.</span>&nbsp;&nbsp;&nbsp;&nbsp;%s = &nbsp;&nbsp;%s'
                                          % (AnExamNum, WrongQuestionList[str(AnExamNum)][0], yate.create_inputs(str(AnExamNum), style='input_control')))
                WQLeftTag = 1
        except KeyError:
            if(WrongQuestionList[str(AnExamNum)][2]):
                ShowWrongQuestions.append('<span class="specfont">%d.</span>&nbsp;&nbsp;&nbsp;&nbsp;%s = &nbsp;&nbsp;%s&nbsp;&nbsp;&nbsp;&nbsp;%s'
                                          % (AnExamNum, WrongQuestionList[str(AnExamNum)][0], WrongQuestionList[str(AnExamNum)][1], yate.img_tag(AwardImageURL1)))
            else:
                ShowWrongQuestions.append('<span class="specfont">%d.</span>&nbsp;&nbsp;&nbsp;&nbsp;%s = &nbsp;&nbsp;%s'
                                          % (AnExamNum, WrongQuestionList[str(AnExamNum)][0], yate.create_inputs(str(AnExamNum), style='input_control')))
                WQLeftTag = 1

except KeyError:
    ShowWrongQuestions.append('没有错题')
    WQLeftTag = 2
except json.JSONDecodeError:
    ShowWrongQuestions.append('无法读取错题数据，请重试')
    WQLeftTag = 2

# 从表单中获取奖励值：
try:
    AwardCount = [int(x.value) for x in form_data['AwardCount']]
except KeyError:
    AwardCount = [0, 0]
except json.JSONDecodeError:
    AwardCount = []

#==================== 定义一个把json字符串转换为json对象的js ====================
JS_string = ''
#==================== 输出错题页面 ====================
print(yate.start_response())
print(yate.include_header_js('欢迎来到韦浩宇的算术运算训练营！', JS_string))
print(yate.header('<span style="color:#ff6666">下面是你本次测验的全部错题，赶紧进行更正吧，会有奖励哦！</span>', 2))
print(yate.start_form('WrongCorrect.py', 'formname'))

# 循环输出所有错题，已经修订正确的错题则不再显示输入框
for Astring in ShowWrongQuestions:
    print(yate.header(Astring, 2))

if(WQLeftTag == 1):
    # =====================更正后仍有错题，需要设置回传表单的内容=====================
    print(yate.input_hidden('WrongQuestions'))    #把所有错题传回表单
    print('<script>var jsonString = JSON.stringify(%s); document.formname.WrongQuestions.value=jsonString;</script>' % json.dumps(WrongQuestionList))  # 将json对象转换为JSON字符串
    print(yate.end_form('确定', 'sub'))
elif(WQLeftTag == 2):
    print('</form>')
else:
    # =====================更正后没有错题，无需再次提交表单=====================
    print('</form>')
    print(yate.header('恭喜您，所有错题都已经更正完毕，奖励 %s × 1, (10个 %s 可兑换1个 %s )'
                      % (yate.img_tag(AwardImageURL2), yate.img_tag(AwardImageURL2), yate.img_tag(AwardImageURL1)), 2))
    # ====================== 把奖励值写回文件 ======================
    # =================== 读取考试记录文件 ===================
    try:
        with open(FilePath, mode='r', encoding='utf-8') as ExamRecFile:
            try:
                ExamRecJson = json.loads(ExamRecFile.read().strip())
                FileExistTag = 1
            except json.JSONDecodeError:
                FileExistTag = 0

    except FileNotFoundError:
        FileExistTag = 0
    # =================== 把奖励值写入测验记录 ===================
    if(AwardCount):
        AwardCount[1] += 1
        if (FileExistTag):  # 当测验记录文件无法读取或文件不存在时，不去动原文件，以备文件恢复
            ExamRecJson['AwardCount'] = AwardCount
            with open(FilePath, mode='w', encoding='utf-8') as ExamRecFile:
                record_string = json.dumps(ExamRecJson)
                ExamRecFile.write(record_string)
        else:
            print('<script>alert(\'%s\')</script>' % '测验记录文件不存在或错误，奖励值保存失败，请联系管理员处理！')

# =====================设置页脚的链接（保持固定顺序）=====================
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['考题回顾'] = 'ExamRecords.py'
if(AwardCount):
    AwardString = yate.img_tag('/images/奖励.png') + '<span style="font-weight:bolder;color:#FF6666;"> × %s</span> ' % (AwardCount[0])\
                  + ' + ' + yate.img_tag('/images/星.png') + '<span style="font-weight:bolder;color:#FF6666;"> × %s</span> ' % (AwardCount[1])\
                  + '&nbsp;&nbsp;<span style="font-weight:bolder;color:#FF6666;">兑换奖励</span>'
    FooterString[AwardString] = 'AwardTable.py'
else:
    AwardString = '无法获取奖励值，请联系管理员查询！'
    FooterString[AwardString] = ''

print(yate.include_footer(FooterString))



