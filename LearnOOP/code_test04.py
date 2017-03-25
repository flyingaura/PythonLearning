# -*- coding: utf-8 -*-

import time
from LearnModule import MY_math
#
# print(MY_math.combination(52,5))

# nlist = (1,2,3)
# print(type(nlist))
# print(isinstance(nlist,(list,tuple)))
#
# # print(nlist[1:])
#
# nlist = [1,2,3,4,5]
#
# result_list = MY_math.fetch_in_list(nlist,3)
# for nl in result_list:
#     print(nl)
from LearnModule import MY_math
def fetch_in_list(nlist,m):
    # ============参数校验=============
    if(not isinstance(nlist,(list,tuple))):
        raise ValueError('参数错误 --> 第一个输入参数必须为序列类型（list或者tuple）')

    try:
        # int_n = int(n)
        int_m = int(m)
    except ValueError as e:
        raise ValueError('参数错误 ：%s --> 两个输入参数都必须为正整数' % e)

    if(len(nlist) < int_m):
        raise ValueError('参数错误 --> 输入的序列长度不能小于第二个值')

    if(int_m < 1):
        raise ValueError('参数错误 --> 输入参数必须为正整数')

    # ============开始计算=============
    # ============定义两个退出条件=============
    num_list = []
    if(m == 1):
        for n in nlist:
            num_list.append([n])
        return num_list
    if(len(nlist) == m):
        num_list.append(nlist)
        return num_list

    # while(m > 1):
        # for n in nlist[:-(m-1)]:
    # ============递归计算=============
    for temp_list in fetch_in_list(nlist[1:],m-1):
        temp_list.insert(0,nlist[0])
        num_list.append(temp_list)
    for temp_list in fetch_in_list(nlist[1:],m):
        num_list.append(temp_list)

    return num_list
#
#
# nlist = list(range(1,21))
#
# result = fetch_in_list(nlist,5)
# countf = MY_math.combination(len(nlist),5)
# for templist in result:
#     print(templist)
# # print(len(result),countf)
#
# astr = 'abc'
# for achar in astr:
#     print(achar in ('a','b'))
#
# # print('当前时间为 %s' %time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# a1 = time.time()
# print(a1)
# time.sleep(3)
# a2 = time.time()
# print(a2)
# print(a2 - a1)

# alist = [1,2,3,4,5]
# print(alist[-5] == alist[0])

# index_num = sorted(list(range(10)),reverse = True)
# print(list(index_num))
print(len([[]]))