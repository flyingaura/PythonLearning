# -*- coding: utf-8 -*-

import random

mpnumlist = []

# numberlist = [str(i) for i in range(0,10)]

for i in range(121):
    mpnumber = '1'
    for j in range(10):
        mpnumber = mpnumber + str(random.randint(0,9))
    mpnumlist.append(mpnumber)

with open('C:/Users/flyingaura/Desktop/公司通讯录数据(组织机构）.dat', mode = 'a') as infile:
    infile.write('\n' + '=' * 20 +'<手机号码>' + '=' * 20 + '\n')
    for Ampnum in mpnumlist:
        infile.write('%s\n' %Ampnum)

