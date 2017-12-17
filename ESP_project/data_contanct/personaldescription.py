# -*- coding: utf-8 -*-
import random

personaldesc = []
with open('F:\documents\python\learning2017\program data\personaldescription', mode = 'rb') as outfile:
    for aline in outfile.readlines():
        aline_decode = aline.decode('utf-8','ignore').strip()
        if(aline_decode != ''):
            personaldesc.append(aline_decode)

# print(len(personaldesc))
# for arecord in personaldesc:
#     print(arecord)

personaldesclist = []
for i in range(121):
    randindex = random.randint(0,25)
    if(randindex > len(personaldesc) - 1):
        personaldescContent = ''
    else:
        personaldescContent = personaldesc[randindex]

    personaldesclist.append(personaldescContent)
# print(personaldesclist)
# print(len(personaldesclist))
#
with open('C:/Users/flyingaura/Desktop/公司通讯录数据(个性说明）.dat', mode = 'w') as infile:
    infile.write('\n' + '=' * 20 +'<个性说明>' + '=' * 20 + '\n')
    for Adesc in personaldesclist:
        infile.write('%s\n' %Adesc)
