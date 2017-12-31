import yate, cgi, json

form_data = cgi.FieldStorage()
score = 0    #初始化考试成绩
RightNum = 0
# =================== 下面是实例化考试成绩判断对象 ===================
print(yate.start_response())
print(yate.include_header('欢迎来到韦浩宇的算术运算训练营！'))

print(yate.para('所用时间为%s秒' %(form_data['totaltime'].value)))
instance_ER_List = []
try:
    exam_exist = 1
    # testJson = '{"1": ["9 + 4", 13], "2": ["16 - 10", 6], "3": ["14 - 1", 13], "4": ["16 - 5", 11], "5": ["8 - 4", 4], "6": ["10 + 2", 12], "7": ["0 + 9 - 5", 4], "8": ["16 + 3", 19], "9": ["7 - 4", 3], "10": ["( 8 - ( 8 - 8 ) )", 8], "11": ["8 + 8", 16], "12": ["12 - 11 + 7", 8], "13": ["5 + 2", 7], "14": ["3 + ( 18 - 12 )", 9], "15": ["18 - 16", 2], "16": ["10 + 5 + 5", 20], "17": ["7 + ( 9 - 12 )", 4], "18": ["( 15 - 4 - 4 )", 7], "19": ["( 15 - ( 7 + 3 ) )", 5], "20": ["11 + 15 - 11", 15]}'
    # ExpressList = json.loads(form_data['ExpressListJson'].value, encoding='utf-8')
    # print(yate.para(form_data['ExamData'].value))
    # print(yate.para(testJson))
    for AnRecord in form_data['ExamData']:
        Aninstance = json.loads(AnRecord.value, encoding='utf-8')
        print(yate.para())

    # ExpressList = json.loads(form_data['ExamData'].value)
    # for AnExp in ExpressList:
    #     print(yate.para(str(ExpressList[AnExp])))

except KeyError:
    exam_exist = 0

# =====================设置页脚的链接（保持固定顺序）=====================
FooterString = OrderedDict()
FooterString['返回首页'] = '/index.html'
FooterString['考题回顾'] = '#'
print(yate.include_footer(FooterString))



JS_string = 'var time=new Date();time.setHours(0);time.setMinutes(0);time.setSeconds(10);var downtime = 1;var timeOutText="";function countdown(){var timeshow=document.getElementById("timeshow");var hour=time.getHours();var min=time.getMinutes();var second=time.getSeconds();setTimeout("countdown()",1000);if(downtime==1){time.setSeconds(second-1);timeshow.style.color="#0099CC";}else{time.setSeconds(second+1);timeOutText="你已超时  ";timeshow.style.color="#CC0033";}if(hour=="0"&&min=="0"&&second=="1"){downtime=0;}hour<10?hour="0"+hour:hour;min<10?min="0"+min:min;second<10?second="0"+second:second;timeshow.innerHTML=timeOutText+hour+":"+min+":"+second;}var timer=setTimeout("countdown()",1000);'