# -*- coding: utf-8 -*-

"""
做作业：
chapter 2
question 17
question 24
question 25
question 26
"""
import math
from LearnModule import MY_math

# ======== question 17 =========
# while(True):
#     num_str = input('请输入一个大于2的数字（q退出）：')
#     if(str.lower(num_str) == 'q'):
#         print('程序结束！')
#         break
#     try:
#         Anum = float(num_str)
#     except ValueError as e:
#         print('格式错误：%s ---> 输入必须为大于2的数字')
#         continue
#     if(Anum < 2):
#         print('输入错误，输入数字必须要大于2')
#     else:
#         print('开始计算！数值为：%.3f ' %Anum)
#         count = 0
#         while(Anum > 2):
#             count = count + 1
#             Anum = math.sqrt(Anum)
#             print('==第 %d 次 平方根 ==> %.3f' %(count,Anum))

# ======== question 24 =========
# init_num = 100000
# while(True):
#
#     # numstr = str(init_num)
#     num1 = init_num % 10000
#     num2 = (init_num + 1) % 100000
#     num3 = str(init_num + 2)[1:5]
#     num4 = init_num + 3
#
#     if(MY_math.if_synnum(num1) and MY_math.if_synnum(num2)
#        and MY_math.if_synnum(num3) and MY_math.if_synnum(num4)):
#         print('最开始的里程数为：%d' %init_num)
#         break
#     init_num = init_num + 1

# ======== question 25 =========

# result_list = []
# for i in range(10,1000):
#     power2 = i * i
#     if(power2 < 1000000 ):
#         if(str(power2)[-3:] == str(i)):
#             result_list.append([i,power2])
#     else:
#         break
#
# count = 0
# for i in result_list:
#     count = count + 1
#     print('No.%d == 满足条件的数为：%d ,乘方值为: %d ==' %(count,i[0],i[1]))


# ======== question 26 =========

# 判断一个字符串所有位数都不相同的函数
def all_diff(n):
    num_str = str(n)
    str_list = []
    for astr in num_str:
        str_list.append(astr)
    while(len(str_list) > 1):
         for astr in str_list[1:]:
             if(str_list[0] == astr):
                 return False
         str_list.pop(0)
    return True

diff_num = []
add_num = []
result_num = []
for i in range(1000,10000):
    if(all_diff(i)):
        diff_num.append(i)

# print(list(diff_num))
# print(len(diff_num))

for inum in diff_num:
    for jnum in diff_num:
        if(str(jnum)[3] == str(inum)[1]):
            addstr = str(jnum)[:3] + str(inum)[0] + str(inum)[2:]
            if(all_diff(addstr)):
                add_num.append([inum,jnum])

# print(list(add_num))
# print(len(add_num))

#
for addnum in add_num:
    sum_num = addnum[0] + addnum[1]
    if(len(str(sum_num)) == 5):
        temp_str = str(addnum[1])[0:2] + str(addnum[0])[2] + str(addnum[0])[1]
        if(str(sum_num)[0:4] == temp_str):
            result_num.append(addnum)
#
print('满足条件的结果为：',list(result_num))






# print(list(diff_num))


