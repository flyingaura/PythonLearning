# -*- coding: utf-8 -*-
import json

infilepath = r'F:\memory\python-learning\learning2017\ESP_project\data_news\搜狐新闻语料库.json'
outfilepath = r'F:\memory\python-learning\learning2017\ESP_project\data_news\news_test.json'

i = 0
testCount = 100
with open(outfilepath, mode = 'w',encoding= 'utf-8') as outfile:
    with open(infilepath, mode = 'r',encoding= 'utf-8') as infile:
        while(i < testCount):
            # alineJson = json.load(infile.readline().strip())
            outfile.write(infile.readline())
            # outfile.write('\n')
            i += 1
