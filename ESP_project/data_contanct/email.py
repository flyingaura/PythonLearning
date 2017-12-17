# -*- coding: utf-8 -*-

import random

letters = [chr(i) for i in range(ord('a'),ord('z') + 1)] + [chr(i) for i in range(ord('A'),ord('Z') + 1)]
letters = letters + [str(i) for i in range(0,10)]
letterslen = len(letters)

EmailList = []
for i in range(121):
    randlen = random.randint(3,12)
    mailstr = ''
    while(len(mailstr) < randlen):
        mailstr = mailstr + letters[random.randint(0,letterslen - 1)]

    mailstr = mailstr + '@infcn.com.cn'
    EmailList.append(mailstr)

with open('C:/Users/flyingaura/Desktop/公司通讯录数据(组织机构）.dat', mode = 'a') as infile:
    infile.write('\n' + '=' * 20 +'<邮件地址>' + '=' * 20 + '\n')
    for Amail in EmailList:
        infile.write('%s\n' %Amail)
