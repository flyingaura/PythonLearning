# -*- coding: utf-8 -*-

from LearnModule import StringSplit

KLcatlist = []

with open('F:/documents/python/learning2017/ESP_project/data_knowledge/学科分类11.dat', mode = 'rb') as infile:
    for aline in infile.readlines():
        aline_decode = aline.decode('utf-8').strip()
        if(aline_decode != ''):
            Arecord = StringSplit.stringsplit(aline_decode,' ')
           # print(Arecord)
            if(len(Arecord[0]) == 2):
                Acatlvl1 = Arecord[1]
            if(len(Arecord[0]) == 4):
                Acatlvl2 = Arecord[1]
            if(len(Arecord[0]) == 6):
                Acatlvl3 = Arecord[1]
                Acatlog = Acatlvl1 + '\\' + Acatlvl2 + '\\' + Acatlvl3
                KLcatlist.append(Acatlog)

with open('F:/documents/python/learning2017/ESP_project/data_knowledge/学科分类22.dat', mode = 'wb') as outfile:
    for arecord in KLcatlist:
        outfile.write(arecord.encode('utf-8'))
        outfile.write('\n'.encode('utf-8'))



