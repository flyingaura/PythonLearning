# -*- coding: utf-8 -*-

import json,xlrd,time

infilepath = r'C:\Users\flyingauraHome\Desktop\科研项目管理系统\国务院公报 refined V1.0.refined-V1.1.xlsx'
outfilepath = r'C:\Users\flyingauraHome\Desktop\科研项目管理系统\publicreport1106.json'
starttime = time.time()
print('========== 程序开始:%s==========' %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(starttime))))
Adata = {}
xlsfile = xlrd.open_workbook(infilepath)
datatable = xlsfile.sheets()[0]
# print(xlsfile.sheet_names())
# print(datatable.name)
# print('%d,%d' %(datatable.ncols,datatable.nrows))
keylist = [Akey for Akey in datatable.row(0)]
with open(outfilepath, mode = 'wb') as outfile:
    BeginWorkTime = time.time()
    print('========== 文件加载完成，耗时 %d 秒==========' %(BeginWorkTime - starttime))
    print('========== 数据开始写入文件 ==========')
    for i in range(1,datatable.nrows):
        for j in range(datatable.ncols):
        #     Adata[keylist[j].value] = datatable.row(i)[j].value.strip()
            Avalue = datatable.row(i)[j].value
            if(not isinstance(Avalue,str)):
                Avalue = str(Avalue)
            Adata[keylist[j].value] = Avalue.strip()
        # print(Adata)
        if(not Adata['发布日期']):
            try:
                TimeValue = Adata['发刊时间'].split('：')[1].split(' ')[0].split('.')
                strTag = '《' * 5
            except IndexError:
                TimeValue = Adata['发刊时间'].split(' ')[0].split('·')
                TimeValue.append('01')
                strTag = '*' * 5
                # for key in Adata:
                #     if(key != '正文源码' and key != '全文-refine'):
                #         print('%s : %s' %(key,Adata[key]))
                # print('%s:%s' %('发刊时间',Adata['发刊时间']))
                # print(Adata)
                # break
            finally:
                Adata['发布日期'] = '/'.join(TimeValue)
                print('%s%s----%s----%s' %(strTag,Adata['发布日期'],Adata['发刊时间'],Adata['标题-refine']))
        if(i % 1000 == 0):
            endtime = time.time()
            print('=========== 已写入 %d 条数据，用时 %d 秒 ============' %(i, endtime - BeginWorkTime))
        outfile.write(json.dumps(Adata, ensure_ascii= False).encode('utf-8'))
        outfile.write('\n'.encode('utf-8'))

endtime = time.time()
print('=========== 完成 %d 条数据写入，用时 %d 秒 ============' %(i, endtime - BeginWorkTime))
print('========== 程序结束:%s==========' %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(endtime))))
