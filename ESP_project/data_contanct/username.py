# -*- coding: utf-8 -*-

import random
from LearnModule import StringSplit

usernamelist = []

with open('F:\documents\python\learning2017\program data\测试用人员名单.dat', mode = 'rb') as outfile:
    outfile.readline()
    for aline in outfile.readlines():
        aline_decode = aline.decode('utf-8').strip()
        Auser = StringSplit.stringsplit(aline_decode,'\t')
        # print(Auser)
        inserttag = 1
        try:
            username = Auser[3]
        except IndexError as e:
            print('%s-->第%s条有问题' %(e,Auser[0]))
            inserttag = 0
        except TypeError as e:
            print('有问题')
            inserttag = 0
        if(inserttag):
            usernamelist.append(username)

usernameset = set()
usernamelistlen= len(usernamelist)
while(len(usernameset) < 121):
    usernameset.add(usernamelist[random.randint(0,usernamelistlen -1)])

# print(usernamelist)

with open('C:/Users/flyingaura/Desktop/公司通讯录数据(组织机构）.dat', mode = 'a') as infile:
    infile.write('\n' + '=' * 20 +'<用户姓名>' + '=' * 20 + '\n')
    for Auser in usernameset:
        infile.write('%s\n' %Auser)