#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import json, cgi, yate, time, sys, cgitb
from collections import OrderedDict
sys.path.append('/Users/flyingauraMac/PycharmProjects/PythonLearning/LearnModule/')
import cal_time
cgitb.enable()

# =================== 定义一个判断考试成绩的类 ===================
class ExamResult(object):
    def __init__(self, ExpNum, ArithmeticExpress, FactResult, CalResult):
        self.ExpNum = ExpNum
        self.ArithmeticExpress = ArithmeticExpress
        self.FactResult = FactResult
        self.CalResult = CalResult

    def IfRight(self):
        if(self.CalResult != None):
            if(self.CalResult == self.FactResult):
                return True
            else:
                return False
        else:
            return False

    def ShowCalResult(self):
        if(self.CalResult == None):
            return '没有提交答案'
        return str(self.CalResult)

# =================== 初始化数据 ===================
form_data = cgi.FieldStorage()
score = 0    #初始化考试成绩
RightNum = 0
ExamTimeInit = (0,10,0)    #初始化考试时间
FilePath = 'data/ExamRecords.json'
WrongExpList = []   #放置错题的列表
# =================== 下面是实例化考试成绩判断对象 ===================
instance_ER_List = []
try:
    exam_exist = 1
    for Anum in range(int(form_data['ExamCount'].value)):
        ExamDataNum = 'ExamData' + str(Anum + 1)
        ExamData = form_data[ExamDataNum]
        if(len(ExamData) < 4):
            CalResult = None
        else:
            CalResult = int(ExamData[3].value)
        instance_ER = ExamResult(int(ExamData[0].value), ExamData[1].value, int(ExamData[2].value), CalResult)
        instance_ER_List.append(instance_ER)
except KeyError:
    exam_exist = 0

# =================== 下面是输出考试成绩页面 ===================
print(yate.start_response())
print(yate.include_header('欢迎来到韦浩宇的算术运算训练营！'))

if(exam_exist):
    # =================== 读考试记录文件，判断文件是否存在并初始化考试奖励值 ===================
    data_string = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    try:
        with open(FilePath, mode='r', encoding='utf-8') as ExamRecFile:
            try:
                ExamRecJson = json.loads(ExamRecFile.read().strip())
                AwardCount = int(ExamRecJson['AwardCount'])
            except json.JSONDecodeError:
                ExamRecJson = {}
                AwardCount = 0
            except KeyError:
                AwardCount = 0

    except FileNotFoundError:
        ExamRecJson = {}
        AwardCount = 0

    # =================== 逐题判断答题结果是否正确并输出答题结果 ===================
    for AnInstance in instance_ER_List:
        if(AnInstance.IfRight()):
            score += 5
            RightNum += 1

    ExamTimeActSeconds = int(form_data['totaltime'].value)
    ExamTimeInitSeconds = ExamTimeInit[0] * 3600 + ExamTimeInit[1] * 60 + ExamTimeInit[2]
    ExamTimeAct = cal_time.seconds2time(ExamTimeActSeconds)
    CostTimeText = '<span style="color:#009966; font-size:150%%;">%d小时%d分%d秒</span>' % (ExamTimeAct[0], ExamTimeAct[1], ExamTimeAct[2])
    if(ExamTimeActSeconds > ExamTimeInitSeconds):
        CostTime = cal_time.seconds2time(ExamTimeActSeconds - ExamTimeInitSeconds)
        CostTimeText = CostTimeText + '(已超时<span style="color:#FF6666; font-size:150%%;">%d小时%d分%d秒</span>)' % (CostTime[0], CostTime[1], CostTime[2])

    print(yate.header(
        '<span style="text-decoration:underline; color:#333333; font-size:150%%">韦浩宇</span>小朋友，'
        '本次考试你做对了<span style="color:#009966; font-size:150%%"> %d </span>道题，'
        '做错了 <span style="color:#FF0033; font-size:150%%"> %d </span> 道题，'
        '得分 <span style="color:#FF6600; font-size:150%%; text-decoration:underline">%d</span> ，考试用时&nbsp;&nbsp;%s&nbsp;&nbsp;，请继续努力哦！'
        % (RightNum, len(instance_ER_List) - RightNum, score, CostTimeText), 2))

    # ====== 判断答题奖励情况：全部正确且不超时，给一个奖励; 如果答题时间小于规定时间一半，则给两个奖励 ======
    if(RightNum == len(instance_ER_List) and int(form_data['numlist'].value) >= 40 and len(form_data['operator']) >= 2 and int(form_data['level'].value) >= 3):
        ThisExamAward = 0
        if(ExamTimeActSeconds <= ExamTimeInitSeconds):
            AwardCount += 1
            ThisExamAward += 1
        if(ExamTimeActSeconds <= ExamTimeInitSeconds // 2):
            AwardCount += 1
            ThisExamAward += 1
        if(ThisExamAward):
            print(yate.header('<span style="color:#FF6600; font-size:120%%;">这次考试在规定时间内全对，恭喜您获得奖励&nbsp;&nbsp;<img src="/images/奖励.png"> × %d</span>' % ThisExamAward, 2))

    # ====== 列出所有考试题和回答结果以及判分情况 ======
    # for AnInstance in sorted(instance_ER_List, key= lambda x:int(x.ExpNum)):
    for AnInstance in instance_ER_List:
        if(AnInstance.IfRight()):
            imgURL = '/images/对勾16_16.png'
        else:
            imgURL = '/images/叉叉16_16.png'
            WrongExpList.append(AnInstance)
        print(yate.header('<span class="specfont">%d.</span>&nbsp;&nbsp;&nbsp;&nbsp;%s' % (
        AnInstance.ExpNum, AnInstance.ArithmeticExpress + ' = &nbsp;&nbsp;' + AnInstance.ShowCalResult() + '&nbsp;' * 4 + yate.img_tag(imgURL)), 2))

    print(yate.header('<span style="text-decoration:underline;">韦浩宇</span>小朋友，'
                      '本次考试你做对了<span style="color:#009966; font-size:150%%"> %d </span>道题，'
                      '做错了 <span style="color:#FF0033; font-size:150%%"> %d </span> 道题，'
                      '得分 <span style="color:#FF6600; font-size:150%%"> %d </span> ，请继续努力哦！'
                      %(RightNum, len(instance_ER_List) - RightNum, score), 4))

# =================== 下面是将错题保存到文件模块 ===================
    with open(FilePath, mode = 'w', encoding='utf-8') as ExamRecFile:
        try:
            ExamNum = sorted([int(x) for x in ExamRecJson['ExamRecords'][data_string].keys()])[-1] + 1
            ExamRecJson['ExamRecords'][data_string][str(ExamNum)] = {'WrongRecords': []}
        except KeyError:
            ExamNum = 1
            ExamRecJson['ExamRecords'] = {data_string: {str(ExamNum):{'WrongRecords': []}}}

        if(len(WrongExpList) != 0):
            for Arecord in WrongExpList:
                ExamRecJson['ExamRecords'][data_string][str(ExamNum)]['WrongRecords'].append((Arecord.ExpNum, Arecord.ArithmeticExpress, Arecord.ShowCalResult()))  #保存题号、算术表达式、输入结果
        ExamRecJson['ExamRecords'][data_string][str(ExamNum)]['ExamCount'] = int(form_data['ExamCount'].value)    #保存测验题目数
        ExamRecJson['ExamRecords'][data_string][str(ExamNum)]['ExamTime'] = (ExamTimeInitSeconds, ExamTimeActSeconds)   #保存考试规定用时和实际用时
        ExamRecJson['AwardCount'] = AwardCount      #保存奖励数量
        record_string = json.dumps(ExamRecJson)
        ExamRecFile.write(record_string)

else:
    print(yate.header('本次考试出问题啦，请点击&nbsp;' + yate.a_link('/index.html', '返回首页') + '&nbsp;重新生成试题', 1))
    AwardCount = 0

# =================== 下面是将算术题参数回传 ===================
print(yate.start_form('exam.py'))
print(yate.input_hidden('numlist', form_data['numlist'].value))
for Operator in [x.value for x in form_data['operator']]:
    print(yate.input_hidden('operator', Operator))
print(yate.input_hidden('level', form_data['level'].value))
print(yate.input_hidden('NewSetting', form_data['NewSetting'].value))

print(yate.end_form('再来一次测验', 'sub'))

# =====================设置页脚的链接（保持固定顺序）=====================
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['考题回顾'] = 'ExamRecords.py'
AwardString = yate.img_tag('/images/奖励.png') + '<span style="font-weight:bolder;color:#FF6666;"> × %d</span>' %(AwardCount)\
              + '&nbsp;&nbsp;<span style="font-weight:bolder;color:#FF6666;">兑换奖励</span>'
FooterString[AwardString] = 'AwardTable.py'
print(yate.include_footer(FooterString))


