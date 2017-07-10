# -*- coding: utf-8 -*-
import numpy
import pylab

# 定义一个直方图函数showbar(value_dic)
def showbar(data_list):

    if(not isinstance(data_list,(list,tuple))):
        raise ValueError('参数错误，参数必须为成对的值列表！')

    keylist = []
    valuelist = []
    barwidth = 0.5
    for Adata in data_list:
        keylist.append(Adata[0])
        valuelist.append(Adata[1])
    xVals = numpy.arange(len(data_list))
    pylab.xticks(xVals, keylist, rotation = 0)
    pylab.bar(xVals, valuelist, width = barwidth, color = 'b')
    pylab.xlabel('keywords')
    pylab.ylabel('Frequence')
    pylab.title('Keywords and its Frequence in the text')

    pylab.show()

    return None

# 定义一个从文本文件中分析汉字与字频的函数
def chineseword_fre(filepath):

    exclude = ['', '', '”', '“', '，', '：', '；', '）', '（', '《', '》', '～', '【', '】', '、', '。', '①', '③', '②', '④', '⑤',
               '⑥', '⑦', '⑧', '⑨']  #中文符号排除列表

    word_freq_dict = {}
    with open(filepath, mode = 'rb') as init_file:
        try:
            file_text = init_file.read().decode('utf-8')
        except UnicodeDecodeError:
            init_file.seek(0)
            file_text = init_file.read().decode('gbk')

    for Aword in file_text:
        if(ord(Aword) > 127 and Aword not in exclude):
            if(Aword not in word_freq_dict):
                word_freq_dict[Aword] = 1
            else:
                word_freq_dict[Aword] += 1

    return word_freq_dict

# =======主程序=======

filepath = 'F:/documents/python/测试数据/test_text.dat'

#按字频大小对统计结果进行排序
CNword_freq = sorted(chineseword_fre(filepath).items(), key = lambda d:d[1], reverse = True)

total_count = 0
for word in CNword_freq:
    total_count = total_count + word[1]


print('%10s|%10s|%10s|' %('字','字频','出现比率'))
for Aword in CNword_freq[:30]:
    print('%10s|%10d|%10.2f%%|' %(Aword[0],Aword[1],Aword[1]/total_count * 100))

# 取前15条结果进行图形展示
showbar(CNword_freq[:15])