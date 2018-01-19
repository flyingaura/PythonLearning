#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi, cgitb, yate, json
from collections import OrderedDict
cgitb.enable()

# ====================== 从ExamRecords文件中获取当前的奖励值 ======================
try:
    with open('data/ExamRecords.json', mode = 'r', encoding= 'utf-8') as recordfile:
        try:
            AwardCount = int(json.loads(recordfile.read().strip())['AwardCount'])
            filestatus = 1
        except json.decoder.JSONDecodeError:
            filestatus = 0
            AwardCount = 0
        except KeyError:
            filestatus = 0
            AwardCount = 0

except FileNotFoundError:
    filestatus = 0
    AwardCount = 0

# ====================== 设置奖励表格的显示内容，以便于接下来在页面上输出 ======================
AwardTable = OrderedDict()
AwardTable['1'] = {'AwardValue':'待定', 'AwardReq': 5}
AwardTable['2'] = {'AwardValue':'待定', 'AwardReq': 10}
AwardTable['3'] = {'AwardValue':'待定', 'AwardReq': 20}
AwardTable['4'] = {'AwardValue':'待定', 'AwardReq': 35}
AwardTable['5'] = {'AwardValue':'待定', 'AwardReq': 60}

# ====================== 设置兑换用的js代码 =====================
js_string = 'function Awardconfirm(buttonid,valueid) {'\
                'var con1 = confirm("确定兑换？");'\
                'if(con1 === true){'\
                    'alert("恭喜你， "+document.getElementById(buttonid).innerHTML+" 兑换成功");'\
                    'document.formname.awardcost.value=document.getElementById(valueid).innerText;'\
                    'document.formname.submit();'\
                '}}'\

# ====================== 以下为奖励查询页面 =====================
print(yate.start_response())
print(yate.include_header_js('奖励查询和兑换', js_string))

print(yate.header('<span style="color:#cc00cc;text-decoration:underline">韦浩宇</span>同学，'
                  '你现在共有奖励值：%s<span style="color:#cc6600"> × %d</span> &nbsp;&nbsp;请从下表中选择你想兑换的奖励'
                  %(yate.img_tag('/images/奖励.png', '测验奖励'), AwardCount), 2))

# ======= 以下为奖励兑换表格的HTML代码 ========
print('<table><tr><th>奖励等级</th><th style="width:240px">奖励内容</th><th>所需兑换值</th><th>是否兑换</th></tr>')
img_string = yate.img_tag('/images/奖励.png')
# ======= 通过循环方式自动生成奖励兑换表格HTML代码 ========
for AwardLevel in AwardTable:
    if(AwardCount >= AwardTable[AwardLevel]['AwardReq']):
        style_string = 'sub_td'
        status_string = ''
    else:
        style_string = ''
        status_string = 'disabled'
    print('<tr>%s%s%s%s%s</tr>' %(yate.td_tag('等级' + AwardLevel), yate.td_tag(AwardTable[AwardLevel]['AwardValue'],id='level' + AwardLevel),
                                yate.td_tag(img_string + '<span style="position:relative;top:-8px;left:2px"> × %d </span>' %AwardTable[AwardLevel]['AwardReq']),
                                yate.td_tag(AwardTable[AwardLevel]['AwardReq'],id='value' + AwardLevel, display=False),
                                yate.td_tag(yate.subbutton('兑换', 'Awardconfirm(\'%s\',\'%s\')' %('level' + AwardLevel, 'value' + AwardLevel), status= status_string, style= style_string))))
print('</table>')

# ======= 以下构造一个表单，将本次兑换花费奖励值传给后台 ========
print(yate.start_form('AwardTable.py',name='formname'))
print(yate.input_hidden('awardcost'))
print('</form>')

# ======= 以下从表单中取出所传的花费奖励值，并计算剩余奖励值后写回测验记录文件 ========
if(filestatus):    #验证文件状态是正常的测验记录文件
    try:
        AwardCost = int(cgi.FieldStorage()['awardcost'].value)
        AwardCost = AwardCount - AwardCost
        print(yate.header('兑换成功，您还剩余兑换值为：<span style="color:#cc6600">%d</span>'
                          % AwardCost, 2))
        with open('data/ExamRecords.json', mode='r+', encoding='utf-8') as recordfile:
            ExamRecordJson = json.loads(recordfile.read().strip())
            ExamRecordJson['AwardCount'] = AwardCost
            recordfile.seek(0)
            recordfile.write(json.dumps(ExamRecordJson))

    except KeyError:
        pass

# ======= 以下为页脚部分 ========
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['开始练习'] = 'expresssion_set.py'
print(yate.include_footer(FooterString))