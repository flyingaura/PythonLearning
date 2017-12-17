# -*- coding: utf-8 -*-
"""
编写一个对词频统计的直方图展示程序
"""

from LearnModule import StringSplit
import pylab
import numpy

# ====== 定义一个获取特殊字符的函数 ======
def special_character(Nstr):
    SC_str = []
    Letter_str = 'abcdefghigklmnopqrstuvwxyz1234567890'
    for astr in Nstr:
        if(astr.lower() not in Letter_str):
            SC_str.append(astr)
    return SC_str

# ====== 定义一个从文本中分析出单词以及单词出现次数的函数 ======
def wordlist(Atext,split_list = ' '):   #split_list （单词间的分隔符以及需要过滤字符，默认为空格）
    word_list = {}
    for Aword in StringSplit.stringsplit(Atext,split_list):
        lower_word = Aword.lower()
        if (lower_word not in word_list):
            word_list[lower_word] = 1
        else:
            word_list[lower_word] = word_list[lower_word] + 1
    return word_list

# ====== 定义一个从文本中分析出字母以及字母出现次数的函数 ======
def Letterlist(Atext,init_letter_list = None):   #split_list （单词间的分隔符以及需要过滤字符，默认为空格）

    Letter_list = {}
    if(init_letter_list):
        if(not isinstance(init_letter_list,str,list,tuple,set)):
            raise ValueError('参数错误--->第二个参数必须为字符串、列表或集合类型！')
        filter_letter_list = init_letter_list
    else:
        filter_letter_list = 'abcdefghigklmnopqrstuvwxyz'

    for Aletter in Atext:
        lower_letter = Aletter.lower()
        if(lower_letter in filter_letter_list):
            if (lower_letter not in Letter_list):
                Letter_list[lower_letter] = 1
            else:
                Letter_list[lower_letter] = Letter_list[lower_letter] + 1
    return Letter_list

# ====== 定义一个基于(key,value)元组的直方图形展示函数 ======
def barGraphic(WC_list):
    keylist = []
    valuelist = []
    for one_dupe in WC_list:
        keylist.append(one_dupe[0])
        valuelist.append(one_dupe[1])

    barwidth = 0.5
    xVals = numpy.arange(len(keylist))
    # print(xVals)
    pylab.xticks(xVals, keylist, rotation = 45)
    pylab.bar(xVals,valuelist,width = barwidth,color = 'g')
    pylab.xlabel('Keywords')
    pylab.ylabel('Frequences %')
    pylab.title('Keywords and its Frequence in the text')
    pylab.show()

# ====== 主函数段，操作文件 ======

with open(r'F:\memory\python-learning\learning2017\program data\text_en.txt', mode = 'r') as init_file:
    fulltext = init_file.read()

# split_list = special_character(fulltext)
# WC_dict = wordlist(fulltext,split_list)
# WC_analysis = []
# for key in WC_dict:
#     if(len(key) > 3 and WC_dict[key] > 2):
#         WC_analysis.append((key,WC_dict[key]))
#         # print('(%s,%d)' %(key,WC_dict[key]))
#
# for oneword in sorted(WC_analysis,key = lambda d:d[1],reverse = True):
#     print('(%s,%3d)' %(oneword[0],oneword[1]))

LC_analysis = []
Lcount = 0
for value in Letterlist(fulltext).values():
    Lcount = Lcount + value

for key in sorted(Letterlist(fulltext).items(),key = lambda d:d[0]):
    print('%s --> %5d | %5.3f%%' %(key[0],key[1],key[1] / Lcount * 100))
    LC_analysis.append((key[0],key[1] / Lcount * 100))

barGraphic(sorted(LC_analysis,key = lambda d:d[1], reverse = True))
# barGraphic(sorted(WC_analysis,key = lambda d:d[1],reverse = True))



