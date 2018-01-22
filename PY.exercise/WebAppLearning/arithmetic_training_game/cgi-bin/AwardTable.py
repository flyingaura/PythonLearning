#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import cgi, cgitb, yate, json
from collections import OrderedDict
cgitb.enable()
formdata = cgi.FieldStorage()

# ====================== 从ExamRecords文件中获取当前的奖励值 ======================
alerttag = 0
try:
    with open('data/ExamRecords.json', mode = 'r', encoding= 'utf-8') as recordfile:
        recordfileText = recordfile.read().strip()
        print(yate.para(recordfileText))
        try:
            ExamRecordJson = json.loads(recordfileText)
            AwardCount = int(ExamRecordJson['AwardCount'])
            filestatus = 1
        except json.decoder.JSONDecodeError:
            filestatus = 0
            AwardCount = 0
            # alerttag = 1
        except KeyError:
            filestatus = 0
            AwardCount = 0
            # alerttag = 2

except FileNotFoundError:
    filestatus = 0
    AwardCount = 0
    # alerttag = 3

if(filestatus):
    # ====================== 尝试从表单中获取上次消费的奖励值 ======================
    try:
        AwardCost = int(formdata['awardcost'].value)
        AwardCount = AwardCount - AwardCost  # 如果有，则减去这个消费值后显示剩余消费值
        # ====================== 将剩余奖励值写回文件 ======================
        with open('data/ExamRecords.json', mode= 'w', encoding= 'utf-8') as recordfile:
            ExamRecordJson['AwardCount'] = AwardCount
            recordfile.write(json.dumps(ExamRecordJson))
    except KeyError:  # 如果表单中没有值，则什么也不发生
        pass
    Header_string = '<span style="color:#cc00cc;text-decoration:underline">韦浩宇</span>同学，' \
                    '你现在共有奖励值：%s<span style="color:#cc6600"> × %d</span> &nbsp;&nbsp;请从下表中选择你想兑换的奖励' \
                    % (yate.img_tag('/images/奖励.png', '测验奖励'), AwardCount)
else:
    Header_string = '<span style="color:#cc00cc;">无法获取到奖励值，可能原因：</span>' \
                    '<ul><li>你尚未进行测验，点击 <a href="expresssion_set.py" style="font-size:100%;">开始测验</a> 来获取你的首个奖励吧！</li>' \
                    '<li>测验记录文件损坏，无法读取！</li></ul>'

# ====================== 设置奖励表格的显示内容，以便于接下来在页面上输出 ======================
AwardTable = OrderedDict()
AwardTable['1'] = {'AwardValue':'ipad游戏一小时', 'AwardReq': 5}
AwardTable['2'] = {'AwardValue':'动画电影一场', 'AwardReq': 10}
AwardTable['3'] = {'AwardValue':'15元以内冰淇淋一个', 'AwardReq': 20}
AwardTable['4'] = {'AwardValue':'100元以内外出吃饭一顿', 'AwardReq': 35}
AwardTable['5'] = {'AwardValue':'200元以内玩具一个', 'AwardReq': 60}

# ====================== 设置兑换用的js代码 =====================
js_string = 'function Awardconfirm(buttonid,valueid,AwardCountid) {'\
                'var con1 = confirm("确定兑换？");'\
                'if(con1 === true){'\
                    'var AwardCountJS = parseInt(document.getElementById(AwardCountid).innerText);'\
                    'var AwardCostJS = parseInt(document.getElementById(valueid).innerText);'\
                    'alert("恭喜你， "+document.getElementById(buttonid).innerHTML+" 兑换成功。剩余奖励值为："+(AwardCountJS-AwardCostJS));'\
                    'document.formname.awardcost.value=AwardCostJS;'\
                    'document.formname.submit();'\
                '}}'\
# ====================== 以下为奖励查询页面 =====================
print(yate.start_response())
print(yate.include_header_js('奖励查询和兑换', js_string))

# if(alerttag == 1):
#     alertstring = 'json错误'
# elif(alerttag == 2):
#     alertstring = 'key错误'
# elif(alerttag == 3):
#     alertstrin = '文件错误'
# else:
#     alertstring = '没有错误'
# print('<script>alert(\'%s\')</script>' % alertstring)
print(yate.header(Header_string, 2))

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
                                yate.td_tag(yate.subbutton('兑换', 'Awardconfirm(\'%s\',\'%s\',\'%s\')' %('level' + AwardLevel, 'value' + AwardLevel, 'AwardCountid'), status= status_string, style= style_string))))
print('</table>')
print('<div id="AwardCountid" style="display:none;">%d</div>' % AwardCount)

# ======= 以下构造一个表单，将本次兑换花费奖励值传给后台 ========
print(yate.start_form('AwardTable.py', name='formname'))
print(yate.input_hidden('awardcost'))
print('</form>')

# ======= 以下为页脚部分 ========
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['开始练习'] = 'expresssion_set.py'
print(yate.include_footer(FooterString))