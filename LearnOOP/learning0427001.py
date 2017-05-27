# -*- coding: utf-8 -*-

import os


# <---定义一个描述文件的类--->
class file_attribute(object):

    def __init__(self,filepath,filename,suffixname):
        self.filepath = filepath
        self.filename = filename
        self.suffixname = suffixname

#     定义一个获取完整文件基础信息的函数
    def file_info(self):
        return os.path.join(self.filepath,(self.filename + self.suffixname))

# 定义一个读取文本类文件，并查询是否有特定内容的函数
def search_text(keywords,fileobject):
    with open(fileobject, mode = 'rb') as init_file:
        try:
            fulltext = init_file.read().decode('utf-8')
        except UnicodeDecodeError:
            init_file.seek(0)
            fulltext = init_file.read().decode('gbk')
            # print(fulltext)
    # try:
    #     search_tag = fulltext.find(keywords)
    # except UnicodeDecodeError:
    #     # print(fileobject)
    #     search_tag = 0
    if(fulltext.find(keywords) >= 0):
        return True
    else:
        return False

# =========以下为主程序=========

# print(os.getcwd())
# os.chdir('F:\documents\python')
# print(os.listdir())
file_list = []
txtfile_list = []

for dir_info in os.walk('F:\documents\python'):
    if(dir_info[2]):
        for Afile in dir_info[2]:
            file_Base = os.path.splitext(Afile)
            file_list.append(file_attribute(dir_info[0],file_Base[0],file_Base[1]))

# print(len(file_list))
for Afile_info in file_list:
    if(Afile_info.suffixname == '.txt'):
        txtfile_list.append(Afile_info)
        # print(Afile_info.file_info())
# print(txtfile_list)

while(True):
    search_result = {}
    result_count = 0
    keyword = input('请输入一个搜索关键词：(-1退出)')
    if(keyword != '-1'):
        for Afile in txtfile_list:
            if(search_text(keyword, Afile.file_info())):
                result_count = result_count + 1
                if(Afile.filepath not in search_result):
                    search_result[Afile.filepath] = [Afile.filename + Afile.suffixname]
                else:
                    search_result[Afile.filepath].append(Afile.filename + Afile.suffixname)
    else:
        break
    if(search_result):
        print('总计 %d 文件中,搜索 \"%s\" ,结果 %d 条,列表如下：' %(len(file_list),keyword,result_count))
        for key in search_result:
            for Afilename in search_result[key]:
                print('所在目录：%s --> 文件名：%s' %(key,Afilename))
    else:
        print('抱歉没有搜索到结果!')
    print('\n')







