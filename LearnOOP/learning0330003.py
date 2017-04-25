# -*- coding: utf-8 -*-
"""
=========== 做作业 ==========
chapter 3.6
question 56
"""
import math
from LearnModule import MY_math
import time
#定义一个判断该数是否为完全平方数的函数
def if_fullsquare(n):
    try:
        n = int(n)
    except ValueError as e:
        raise('参数错误：%s -->输入参数必须为正整数或能转换为正整数的字符串')
    if(n <= 0):
        return False
    for i in range(int(math.sqrt(n))+1):
        if(i * i == n):
            return True

    return False

num_list = [x for x in range(1,19)]
fullsquare_list = []
result_list = []
start_time = time.time()
print('==== 开始计算 ==== @ %s' %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))))
for alist in MY_math.fetch_in_list(num_list,2):
    if(if_fullsquare(alist[0] + alist[1])):
        fullsquare_list.append((alist[0],alist[1]))

# print(len(fullsquare_list))
# print(fullsquare_list)
# print(MY_math.combination(18,9))

for alist in MY_math.fetch_in_list(fullsquare_list,9):
    # print(alist)
    one_list = []
    for atuple in alist:
        one_list.append(atuple[0])
        one_list.append(atuple[1])
    print(one_list)
    if(sorted(one_list) == num_list):
        result_list.append(alist)
        # print('满足要求的配对方式为：',alist)
        # break
end_time = time.time()
print('==== 完成计算 ==== @ %s' %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))))
print('共计算得出 %d 组结果-->' %(len(result_list)))
for i in range(len(result_list)):
    print('第 %d 组结果为：' %(i+1),result_list[i])



