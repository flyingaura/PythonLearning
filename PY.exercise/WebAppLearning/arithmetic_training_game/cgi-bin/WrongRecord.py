# -*- coding: utf-8 -*-

import yate,json,cgi

RecordFilePath = 'data/WrongRecord.json'   #指定错误题目记录文件路径
form_data = cgi.FieldStorage()

print(yate.start_response())
print(yate.include_header('韦浩宇的算术训练营 -- 错题回顾'))

try:
    with open(RecordFilePath, mode = 'r', encoding='utf-8') as readfile:
        jsonstring = json.loads(readfile.read().strip())
        WrongRecDict = {}
        for Arec in sorted(jsonstring.keys(), reverse = True):
            WrongRecDict[Arec] = Arec + '(<font color="red">' + str(len(jsonstring[Arec])) + '</font>)'

    print(yate.para('请选择查看哪天的错题？'))
    print(yate.start_form('WrongRecord.py'))
    print(yate.select_set('WrongRecSelect', WrongRecDict))
    print(yate.end_form('确定'))

    try:
        Recordkey = form_data['WrongRecSelect'].value
        print(yate.para(''))
        print(yate.header('以下为 <ins>%s</ins> 的错题记录（共 <ins>%d</ins> 道）：' %(Recordkey, len(jsonstring[Arec])), 2))
        print(yate.u_list(jsonstring[Recordkey]))
    except KeyError:
        pass
    finally:
        print(yate.header('', 2))

except FileNotFoundError:
    print(yate.header('目前没有错误记录，请继续努力！', 1))


print(yate.include_footer({'返回首页': '/index.html'}))