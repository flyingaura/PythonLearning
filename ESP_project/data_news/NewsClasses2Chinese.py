# -*-coding: utf-8 -*-
# 将分析出来的新闻类型转化为中文

from LearnModule import StringSplit

infilepath = r'F:\memory\python-learning\learning2017\ESP_project\data_news\NewsCalsses.json'

RestClasses = []
with open(infilepath, mode = 'r', encoding= 'utf-8') as infile:
    for aline in infile.readlines():
        if('auto' in StringSplit.stringsplit(aline, '\t')[1]):
            continue
        else:
            print(aline)
            RestClasses.append(aline)

# print(len(RestClasses))
