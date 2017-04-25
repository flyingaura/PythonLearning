# -*- coding: utf-8 -*-
"""
=========== 做作业 ==========
chapter 3.6
exercise 2  帕斯卡三角形
"""
from LearnModule import MY_math

# for i in range(10,100):
#     for j in range(100,1000):
#         if(MY_math.if_synnum(i) and MY_math.if_synnum(j)):
#             if(MY_math.if_synnum(i + j) and (i + j) >= 1000):
#                 print('第一个数为：%d，第二个数为：%d，第三个数为:%d' %(i,j,i + j))

# alist = [1,2,3]
# blist = [1,2,3,4,5,6]
#
# print(alist in blist)

# ====生成帕斯卡三角形并输出====

# 定义一个n高度的帕斯卡三角形
def PSC_triangle(n):
    try:
        int_n = int(n)
    except ValueError as e:
        raise ValueError('参数错误：%s ----> 输入参数必须为整数' %e)

    if(int_n <= 0):
        raise ValueError('参数错误 ----> 输入参数必须为正整数')

    num_PT = [0 for x in range(2*int_n + 1)]
    init_PT = num_PT[::]
    result_PT = []
    num_PT[int_n] = 1
    result_PT.append(num_PT)
    for i in range(int_n - 1):
        num_temp = init_PT[::]
        for j in range(1,2 * int_n):
            num_temp[j] = num_PT[j-1] + num_PT[j + 1]
        num_PT = num_temp
        result_PT.append(num_PT)

    return result_PT

PT_highth = 10
str_PT = []
for one_PT in PSC_triangle(PT_highth):
    # print(list(one_PT))
    for i in range(len(one_PT)):
        if(one_PT[i] == 0):
            one_PT[i] = ' '
        else:
            one_PT[i] = str(one_PT[i])
    str_PT.append(''.join(one_PT))

for astr in str_PT:
    print(astr)









