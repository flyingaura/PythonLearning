# -*- coding: utf-8 -*-

import random

viewcounts = [random.randint(0,200) for i in range(121)]
randindex = set()
while(len(randindex) < 43):
    randindex.add(random.randint(0,120))

for i in randindex:
    viewcounts[i] = 0


with open('C:/Users/flyingaura/Desktop/公司通讯录数据(组织机构）.dat', mode = 'a') as infile:
    infile.write('\n' + '=' * 40 + '\n')
    for icount in viewcounts:
        infile.write('%d\n' %icount)