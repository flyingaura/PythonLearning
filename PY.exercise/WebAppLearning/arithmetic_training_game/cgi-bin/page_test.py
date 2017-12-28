# -*- coding: utf-8 -*-

import yate,json,os
#
# page_header = yate.include_header('aaaa')
# print('*' * 40)
# print(page_header)

RecordFilePath = '../data/WrongRecord.json'

# with open(RecordFilePath,mode = 'w+', encoding= 'utf-8') as outfile:
#     # json.dump({'aa':123},outfile)
#     # outfile.seek(0)
#     # print(outfile.read())
#     # jsonstring = json.loads(outfile.read())

# print(os.path.isfile(RecordFilePath))

Form_JS = '<script type="text/javascript">\
function addAction(){\
    document.name.action="指向的连接";\
    document.name.submit();\
}\
function deleteAction(){\
    document.name.action="指向的连接";\
    document.name.submit();\
}\
function saveAction(){\
    document.name.action="指向的连接";\
    document.name.submit();\
}\
 function searchAction(){\
    document.name.action="指向的连接";\
    document.name.submit();\
}\
</script>'

print(yate.include_header_js('设置算术表达式的生成参数！', Form_JS))