# -*- coding: utf-8 -*-

import random
import math
# Alist = [random.randint(0,9) for x in range(20)]
# # Blist = []
# print(Alist)
# print(list(set(Alist)))
# # Alist = sorted(Alist)
# # if(len(Alist) <= 1):
# #     Blist = Alist
# # else:
# #     for i in range(len(Alist)-1):
# #         if(Alist[i] != Alist[i+1]):
# #             Blist.append(Alist[i])
# # Blist.append(Alist[-1])
# # print(Blist)
# i = 0
# while(i < len(Alist)):
#     j = i + 1
#     while(j < len(Alist)):
#         if (Alist[j] == Alist[i]):
#             Alist.pop(j)
#         else:
#             j += 1
#     i += 1
#
# print(Alist)

# print(random.randint(0,9))

# Astr = '12345'
# print(Astr,Astr[::-1])

# 输出9*9乘法表
#
# for i in range(1,10):
#     for j in range(1,i+1):
#         print('%3d * %3d = %3d' %(j,i,i*j),end = '\t')
#     print('\n')

# 输出N以内的全部素数

# def Cal_Shushu(N):
#     # init_list = list(range(2,N+1))
#     # ou_num = []   #非素数的集合
#     Shushu_list = []
#     for TestNum in range(2,N + 1):
#         if_tag = True
#         for i in range(2,int(math.sqrt(TestNum)) + 1):
#             if(TestNum % i == 0):
#                 if_tag = False
#                 break
#         if(if_tag):
#             Shushu_list.append(TestNum)
#     #     for j in range(i,int(N / 2) + 1):
#     #         Multi_Result = i * j
#     #         if (Multi_Result <= N):
#     #             ou_num.append(Multi_Result)
#     #
#     # Shushu_list = list(set(init_list).difference(set(ou_num)))
#     return Shushu_list
#
# print(Cal_Shushu(100))

# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？

def Add_Couple_Rabbits(Nmonth):     #Nmonth为月数
    try:
        Nmonth = int(Nmonth)
    except ValueError as e:
        raise ValueError('%s ---> 参数类型错误，必须为正整数' %e)
    if(Nmonth <= 0):
        raise ValueError('参数类型错误，必须为正整数')
    Count_Couple_Rabbits = 1
    if(Nmonth < 4):
        return Count_Couple_Rabbits
    else:
        for imonth in range(Nmonth - 3):
            Count_Couple_Rabbits = Count_Couple_Rabbits + Add_Couple_Rabbits(imonth + 1)
        return Count_Couple_Rabbits

while(1):
    Month_Num = input('请输入要计算的月数（必须为正整数，q退出）:')
    if(Month_Num.lower() == 'q'):
        print('程序结束!')
        break
    print('%d 个月内，总兔子数为：%d' %(int(Month_Num),Add_Couple_Rabbits(int(Month_Num))))










