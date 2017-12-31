# -*- coding: utf-8 -*-
# 测试能否从整个HTML网页中提取出正文部分的HTML原码

from html.parser import HTMLParser

# print(dir(HTMLParser))

class MyHtmlPasrser(HTMLParser):
    def __init__(self,specifyTag = None,specifyValue = None):
        HTMLParser.__init__(self)
        self.specifyTag = specifyTag
        self.specifyValue = specifyValue
        self.HtmlText = False
        self.datalist = {}
        self.index = 0

    def handle_starttag(self, tag, attrs):

        if(tag == 'td'):
            # print(attrs)
            if(len(attrs)):
                for attrdata in attrs:
                    if(attrdata[0] == self.specifyTag and attrdata[1] == self.specifyValue):
                        self.HtmlText = True
                        self.index += 1
                        # print(self.handle_data(data))
                        break
            # self.HtmlText = True
    def handle_endtag(self, tag):
        if(tag == 'tbody'):
            self.HtmlText = False

    def handle_data(self, data):
        if(self.HtmlText):
            print(data)
            print('********')
        #     # return data
        #     self.datalist[self.index] = data
        # return self.datalist


infilepath = r'F:\documents\python\learning2017\RSF_project\data\htmlcodetest001.txt'

with open(infilepath, mode = 'r', encoding= 'utf-8') as infile:
    HtmlCode = infile.read()

# testcode = '<sada>啊啊啊</sada><a href="http://click.union.360buy.com/JdClick /?unionId=75" class="f1"  style="padding-left:13px; padding-right:14px">京东商城</a></td><td><a href="http://www.letao.com /?source=hao123" class="f1">乐淘网上鞋城</a></td><td><a href="http://www.lashou.com/cl_today/w_3001" class="f2">拉手团购</a></td><td><a href="http://www.amazon.cn/?tag=2009hao123famousdaohang" class="f2">亚马逊</a></td><td><a href="http://www.vancl.com/?source=hao123mp"  class="f1">凡客诚品</a></td><td><a href="http://reg.jiayuan.com/st/?id=3237&url=/st /main.php" class="f1">世纪佳缘'

AHtmlCode = MyHtmlPasrser('b12c""')
AHtmlCode.feed(HtmlCode)
AHtmlCode.close()
# for key in AHtmlCode.datalist:
#     print('%d: %s' %(key, AHtmlCode.datalist[key]))
#
# print(AHtmlContent)