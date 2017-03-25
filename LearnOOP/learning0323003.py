# -*- coding: utf-8 -*-

"""
一些特殊格式的算术例子输出
"""

with open('C:/Users/flyingaura/Desktop/aaa.txt', mode = 'w+') as out_file:

    num = 0
    for i in range(1,10):
        num = num * 10 + i
        num_exp = num * 8 + i
        print('%d * 8 + %d = %d' %(num,i,num_exp))
        out_file.write('%d * 8 + %d = %d \n' %(num,i,num_exp))
    out_file.write('============================================== \n\n')
        # out_file.write('\n')

    num = 0
    for i in range(1,10):
        num = num * 10 + i
        num_exp = num * 9 + (i + 1)
        print('%d * 9 + %d = %d' % (num, i+1, num_exp))
        out_file.write('%d * 9 + %d = %d \n' % (num, i+1, num_exp))
    out_file.write('============================================== \n\n')

    num = 0
    reserve_list = []
    for i in range(2,10):
        reserve_list.insert(0,i)
    for i in reserve_list:
        num = num * 10 + i
        num_exp = num * 9 + (i -2)
        print('%d * 9 + %d = %d' % (num, i - 2, num_exp))
        out_file.write('%d * 9 + %d = %d \n' % (num, i - 2, num_exp))
    out_file.write('============================================== \n\n')

    num = 0
    for i in range(9):
        num = num * 10 + 1
        num_exp = num * num
        print('%d * %d = %d' % (num, num, num_exp))
        out_file.write('%d * %d = %d \n' % (num, num, num_exp))
    out_file.write('============================================== \n\n')


