# -*- coding: utf-8 -*-

import yate,json,cgi,sys
from collections import OrderedDict
sys.path.append('F:/memory/python-learning/learning2017/LearnModule/')
import cal_time

RecordFilePath = 'data/ExamRecords.json'   #指定测验历史记录文件路径
form_data = cgi.FieldStorage()
WrongCount = 0

print(yate.start_response())
print(yate.include_header_js('韦浩宇的算术训练营 -- 测验回顾', ''))

try:
    with open(RecordFilePath, mode = 'r', encoding='utf-8') as readfile:
        jsonstring = json.loads(readfile.read().strip())
        ExamRecDict = OrderedDict()
        for Arec in sorted(jsonstring.keys(), reverse = True):
            for AnExam in jsonstring[Arec]:
                WrongCount = WrongCount + len(jsonstring[Arec][AnExam]['WrongRecords'])
            ExamRecDict[Arec] = Arec + '(%d | %d)' %(len(jsonstring[Arec]), WrongCount)

    print('<div id="topfixed">')
    print(yate.header('韦浩宇的算术训练营 -- 测验回顾', 1))
    print(yate.para('请选择查看哪天的测验？'))
    print(yate.start_form('ExamRecords.py'))
    print(yate.select_set('ExamRecSelect', ExamRecDict))
    print(yate.end_form('确定', 'sub'))

    try:
        Recordkey = form_data['ExamRecSelect'].value
        print(yate.para(''))
        print(yate.header('以下为 <ins>%s</ins> 的测验记录（共 <ins>%d</ins> 次）：' %(Recordkey, len(jsonstring[Recordkey])), 2))
        print('</div>')
        print('<div style="margin-top:220px">')
        for AnExam in sorted(jsonstring[Recordkey].keys()):
            ExamWrongList = jsonstring[Recordkey][AnExam]['WrongRecords']
            ExamTime = jsonstring[Recordkey][AnExam]['ExamTime']
            ExamTimeAct = cal_time.seconds2time(int(ExamTime[1]))
            CostTimeText = '<span style="color:#009966;">%d小时%d分%d秒</span>' % (ExamTimeAct[0], ExamTimeAct[1], ExamTimeAct[2])
            if(int(ExamTime[0]) < int(ExamTime[1])):
                CostTime = cal_time.seconds2time(int(ExamTime[1]) - int(ExamTime[0]))
                CostTimeText = CostTimeText + '(已超时<span style="color:#FF6666;">%d小时%d分%d秒</span>)' % (CostTime[0], CostTime[1], CostTime[2])

            # print('<hr color="#CCCCCC">')
            if(len(ExamWrongList)):
                DescText = '<span style="color:#0066CC">%s.</span>&nbsp;&nbsp;本次测验共 <span style="color:#009966">%d</span> 道题，' \
                           '做错了 <span style="color:#FF6600; text-decoration:underline">%d</span> 道题，共用时 %s ' \
                           % (AnExam, int(jsonstring[Recordkey][AnExam]['ExamCount']), len(ExamWrongList), CostTimeText)
                print(yate.header(DescText, 3))
                print('<ul>')
                for AnWrongExp in ExamWrongList:
                    print('<li><span style="color:#CCCCCC; font-size:80%%">%s.</span>&nbsp;&nbsp;%s = <span style="color:#FF6666; text-decoration:underline">%s</span></li>'
                          % (AnWrongExp[0], AnWrongExp[1], AnWrongExp[2]))
                print('</ul>')
            else:
                DescText = '<span style="color:#0066CC">%s.</span>&nbsp;&nbsp;本次测验共<span style="color:#009966">%d</span> 道题，你全做对啦！共用时 %s &nbsp;&nbsp;%s&nbsp;&nbsp;你真棒，请继续努力哦！' \
                           % (AnExam, int(jsonstring[Recordkey][AnExam]['ExamCount']), CostTimeText, yate.img_tag('/images/奖励.png'))
                print(yate.header(DescText, 3))
            print(yate.header('', 2))
            print('</div>')
    except KeyError:
        # print(yate.para(''))
        # print(yate.header('抱歉，您所选的测验记录不存在，请重新选择！', 2))
        print('</div>')
        pass
    # finally:
    #     print(yate.header('', 2))

except FileNotFoundError:
    print(yate.img_tag('/images/miao1.jpg', title= '抱歉，目前没有测验记录！', align='center'))
    print(yate.header('%s目前没有测验记录！点击' + yate.a_link('expresssion_set.py', '开始一次测验吧'), 1))


# =====================设置页脚的链接（保持固定顺序）=====================
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['开始测验'] = 'expresssion_set.py'
print(yate.include_footer(FooterString))