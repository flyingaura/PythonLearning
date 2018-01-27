#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

import yate, cgi, json, cgitb
from collections import OrderedDict

cgitb.enable()
form_data = cgi.FieldStorage()
score = 0    #初始化考试成绩
RightNum = 0
# =================== 下面是实例化考试成绩判断对象 ===================
print(yate.start_response())
print(yate.include_header('欢迎来到韦浩宇的算术运算训练营！'))

print(yate.start_form('page_test.py'))
print(yate.input_hidden('testlist', 'apple'))
print(yate.input_hidden('testlist', 'banana'))
print(yate.end_form('确定', 'sub'))

try:
    for Afruit in form_data['testlist']:
        print(yate.header('这是一个%s' % Afruit.value, 2))

except KeyError:
    print('<script>alert(\'%s\')</script>' % ('发生错误，没有获取到任何一个水果！---->'))

# =====================设置页脚的链接（保持固定顺序）=====================
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['考题回顾'] = '#'
print(yate.include_footer(FooterString))



JS_string = 'var time=new Date();time.setHours(0);time.setMinutes(0);time.setSeconds(10);var downtime = 1;var timeOutText="";function countdown(){var timeshow=document.getElementById("timeshow");var hour=time.getHours();var min=time.getMinutes();var second=time.getSeconds();setTimeout("countdown()",1000);if(downtime==1){time.setSeconds(second-1);timeshow.style.color="#0099CC";}else{time.setSeconds(second+1);timeOutText="你已超时  ";timeshow.style.color="#CC0033";}if(hour=="0"&&min=="0"&&second=="1"){downtime=0;}hour<10?hour="0"+hour:hour;min<10?min="0"+min:min;second<10?second="0"+second:second;timeshow.innerHTML=timeOutText+hour+":"+min+":"+second;}var timer=setTimeout("countdown()",1000);'