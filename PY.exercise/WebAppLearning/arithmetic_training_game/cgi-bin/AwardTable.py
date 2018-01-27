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
            AwardCount = [int(x) for x in ExamRecordJson['AwardCount']]
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
    AwardChange = 0
    try:
        AwardCost = int(formdata['awardcost'].value)
        AwardCount[0] = AwardCount[0] - AwardCost  # 如果有，则减去这个消费值后显示剩余消费值
        AwardChange = 1
    except KeyError:  # 如果表单中没有值，则什么也不发生
        pass
    # ====================== 尝试从表单中获取上次兑换的碎片值 ======================
    try:
        LittleAwardEx = int(formdata['ExChange'].value)
        AwardCount[1] = AwardCount[1] - LittleAwardEx * 10
        AwardCount[0] += LittleAwardEx
        AwardChange = 1
    except KeyError:  # 如果表单中没有值，则什么也不发生
        pass
    if(AwardChange):
        # ====================== 将剩余奖励值写回文件 ======================
        with open('data/ExamRecords.json', mode='w', encoding='utf-8') as recordfile:
            ExamRecordJson['AwardCount'] = AwardCount
            recordfile.write(json.dumps(ExamRecordJson))
    Header_string = '<span style="color:#cc00cc;text-decoration:underline">韦浩宇</span>同学，' \
                    '你现在共有奖励值：%s<span style="color:#cc6600"> × %d</span> + %s<span style="color:#cc6600"> × %d</span>' \
                    '&nbsp;&nbsp;请从下表中选择你想兑换的奖励' \
                    % (yate.img_tag('/images/奖励.png', '测验奖励'), AwardCount[0], yate.img_tag('/images/星.png', '奖励碎片'), AwardCount[1])
else:
    Header_string = '<span style="color:#cc00cc;">无法获取到奖励值，可能原因：</span>' \
                    '<ul><li>你尚未进行测验，点击 <a href="expresssion_set.py" style="font-size:100%;">开始测验</a> 来获取你的首个奖励吧！</li>' \
                    '<li>测验记录文件损坏，无法读取！</li></ul>'

# ====================== 设置奖励表格的显示内容，以便于接下来在页面上输出 ======================
AwardTable = OrderedDict()
AwardTable['1'] = {'AwardValue':'看电视1小时', 'AwardReq': 5}
AwardTable['2'] = {'AwardValue':'ipad游戏1小时', 'AwardReq': 10}
AwardTable['3'] = {'AwardValue':'15元以内冰淇淋一个', 'AwardReq': 20}
AwardTable['4'] = {'AwardValue':'100元以内外出吃饭一顿', 'AwardReq': 35}
AwardTable['5'] = {'AwardValue':'200元以内玩具一个', 'AwardReq': 60}

# ====================== 设置兑换用的js代码 =====================
#第一段JS：兑换奖品;后面三段JS：用来兑换碎片
js_string = 'function Awardconfirm(buttonid,valueid,AwardCountid){'\
                'var con1 = confirm("确定兑换？");'\
                'if(con1 === true){'\
                    'var AwardCountJS = parseInt(document.getElementById(AwardCountid).innerText);'\
                    'var AwardCostJS = parseInt(document.getElementById(valueid).innerText);'\
                    'alert("恭喜你， "+document.getElementById(buttonid).innerHTML+" 兑换成功。剩余奖励值为："+(AwardCountJS-AwardCostJS));'\
                    'document.formAward.awardcost.value=AwardCostJS;'\
                    'document.formAward.submit();'\
                '}}'\
            'function addone(minnum,maxnum) {'\
            'var Avalue = parseInt(document.formname.ExChange.value);'\
            'document.formname.ExChange.value = Avalue+1;'\
            'ExCase(minnum,maxnum);'\
            '}'\
            'function subone(minnum,maxnum) {'\
                'var Avalue = parseInt(document.formname.ExChange.value);'\
                'document.formname.ExChange.value = Avalue-1;'\
                'ExCase(minnum,maxnum);'\
            '}'\
            'function ExCase(minnum,maxnum) {'\
                'var nownum=parseInt(document.formname.ExChange.value);'\
                'var minValue = parseInt(parseInt(minnum)/10);'\
                'var maxValue=parseInt(parseInt(maxnum)/10);'\
                'if(nownum < minValue){'\
                    'alert("输入的值太小啦！");'\
                    'document.formname.substract.disabled=true;'\
                    'document.formname.Exbutton.disabled=true;'\
                    'document.formname.add.disabled=false;'\
                    'document.formname.ExChange.value=minValue;'\
                '}else if(nownum > maxValue){'\
                    'alert("输入的值太大啦");'\
                    'document.formname.add.disabled=true;'\
                    'document.formname.substract.disabled=false;'\
                    'document.formname.Exbutton.disabled=false;'\
                    'document.formname.ExChange.value=maxValue;'\
                '}else{'\
                    'document.formname.add.disabled=false;'\
                    'document.formname.substract.disabled=false;'\
                    'document.formname.Exbutton.disabled=false;'\
                '}}'\
            'function SubCase() {'\
                'var con1=confirm("确定要兑换"+document.formname.ExChange.value+"奖励值吗？");'\
                'if(con1===true){'\
                    'document.formname.submit();'\
                '}}'\
# ====================== 以下为奖励查询页面 =====================
print(yate.start_response())
print(yate.include_header_js('奖励查询和兑换', js_string))

# ====================== 碎片能够兑换成奖励值 =====================
if(AwardCount[1] >= 10):
    print(yate.header('<span style="color:#ff6666">你现在有 %d 个碎片可以先兑换成奖励值啦！</span>' % AwardCount[1], 2))
    print('<div><span style="color:#660066;font-size:18px;">请选择需要兑换的奖励值数量</span>')
    print(yate.start_form('AwardTable.py', 'formname'))
    print(yate.subbutton('-', 'subone(%d,%d)' % (0, AwardCount[1]), 'substract', status='disabled', style='buttonCS'))
    print('<input type="text" name="ExChange" value="0" onchange="ExCase(%d,%d)" class="input_control">' % (0, AwardCount[1]))
    print(yate.subbutton('+', 'addone(%d,%d)' % (0, AwardCount[1]), 'add', style='buttonCS'))
    print(yate.subbutton('兑换', 'SubCase()', 'Exbutton', status='disabled', style='AbuttonCS'))
    print('</form></div>')

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
if(AwardCount[1] < 0):
    RealAwardCount = (AwardCount[0] * 10 + AwardCount[1]) // 10
else:
    RealAwardCount = AwardCount[0]
for AwardLevel in AwardTable:
    if(RealAwardCount >= AwardTable[AwardLevel]['AwardReq']):
        style_string = 'sub_td'
        status_string = ''
    else:
        style_string = 'sub_td'
        status_string = 'disabled'
    print('<tr>%s%s%s%s%s</tr>' %(yate.td_tag('等级' + AwardLevel), yate.td_tag(AwardTable[AwardLevel]['AwardValue'],id='level' + AwardLevel),
                                yate.td_tag(img_string + '<span style="position:relative;top:-8px;left:2px"> × %d </span>' %AwardTable[AwardLevel]['AwardReq']),
                                yate.td_tag(AwardTable[AwardLevel]['AwardReq'],id='value' + AwardLevel, display=False),
                                yate.td_tag(yate.subbutton('兑换', 'Awardconfirm(\'%s\',\'%s\',\'%s\')' %('level' + AwardLevel, 'value' + AwardLevel, 'AwardCountid'), status= status_string, style= style_string))))
print('</table>')
print('<div id="AwardCountid" style="display:none;">%d</div>' % RealAwardCount)

# ======= 以下构造一个表单，将本次兑换花费奖励值传给后台 ========
print(yate.start_form('AwardTable.py', name='formAward'))
print(yate.input_hidden('awardcost'))
print('</form>')

# ======= 以下为页脚部分 ========
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['开始练习'] = 'expresssion_set.py'
print(yate.include_footer(FooterString))