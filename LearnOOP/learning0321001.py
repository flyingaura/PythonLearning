# -*- coding: utf-8 -*-
# 学习lambda函数

import math

def str_join(slist,fn):
    sl1 = []
    for sx in slist:
        sl1.append(sx + fn(sx))
    return sl1


# ss = []
# for x in range(10):
#     ss.append(chr(ord('a') + x))
# print(str_join(ss,lambda x: x + ' hello world!'))

# fn = lambda x:(x + (x-5)j)
# for x in range(10):
#     print(fn(x))


# a = 7
# b = 3.2
# c = 2
# d = 3
# # print(chr(ord('a')+10))
# # print(float(a/b))
# print(a%b)
# print(c/d)
# print(help(math.pow))
numchar_list = ['0','1','2','3','4','5','6','7','8','9','.']
while(True):
    inum = input('请输入一个数字：(q退出)')
    if (inum == 'q'):
        print('The function is END !')
        break
    point_num = 0
    reinput_tag = 0
    for sstr in inum:
        if(sstr not in numchar_list):
            reinput_tag = 1
            break
        if(sstr == '.'):
            point_num = point_num + 1
    if(reinput_tag == 1):
        print('您输入的数字类型错误，请重新输入！')
    elif (point_num == 0):
       print('计算进行中...')
       result_num = ((int(inum) + 2) * 3 - 6)/3
       print('计算结果为：%d' %result_num)
    elif (point_num == 1):
        print('计算进行中...')
        result_num = ((float(inum) + 2) * 3 - 6) / 3
        print('计算结果为：%f' % result_num)


