# -*- coding: utf-8 -*-
"""
=========== 做作业 ==========
chapter 3.6
question 57
question 58
"""
import math
import random
import time
from LearnModule import MY_math
# =========== question 57 ===========
#
# from LearnModule import MY_math
# operators = ['+','-','*','/','**']
# ope_nums = [2,3,4,5]
# result_num = 26
# express_str = ''
# for operateor in MY_math.array_in_list(operators,3):
#     for num in MY_math.array_in_list(ope_nums,4):
#         express_str = str(num[0]) + operateor[0] + str(num[1]) + operateor[1] \
#                       + str(num[2]) + operateor[2] + str(num[3])
#         # print('%s = %d' %(express_str,eval(express_str)))
#         if(eval(express_str) == result_num):
#             print('%s = %d' %(express_str,result_num))

# =========== question 58 ===========

init_str = '123456789'
operator_str = '+-*/'
equal_num = 100
num_list = []   #用于判断生成的数字切分序列是否重复
result_list = []
end_count = 0
start_time = time.time()
# cal_count = 1
str_length = len(init_str)
print('=========== Starting Calculation @ %s ===========' %(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time))))
operator_list = []
# 初始化所有可能的操作符序列
print('============开始初始化所有可能的操作符序列==============')
for i in range(1,len(init_str)):
    # -----> 调用序列遍历函数来生成所有可能的操作符组合operator_list
    operator_list.append(MY_math.through_in_list(operator_str,i))

print('============操作符序列初始化完成==============')

while(len(result_list) < 100):
    step_num = 0
    split_list = []

    # operator_list = []
    # -----> 使用随机数来生成对数字的切分序列split_list
    while(step_num < str_length):
        fragment = step_num + random.randint(1,str_length-1)
        split_list.append(init_str[step_num:fragment])
        step_num = fragment

    if(split_list not in num_list):  #重复序列不再计算，以提高计算效率
        num_list.append(split_list)
        # print(list(split_list))

    # -----> 将数字切分序列split_list与操作符组合operator_list组装起来，形成表达式express_str
        # -----> 根据数字切分序列split_list的长度来选择对应的操作符组合operator_list序列
        for one_operators in operator_list[len(split_list) - 2]:
            express_str = split_list[0]
            for i in range(len(one_operators)):
                express_str = express_str + one_operators[i] + split_list[i + 1]

            # print(express_str)
    # for num_str in split_list[:-1]:
    #     express_str = express_str + num_str + operator_str[random.randint(0,3)]
    # express_str = express_str + split_list[-1]
    # express_str = ' + '.join(split_list)
    # print('%s = %d' %(express_str,eval(express_str)))

        # -----> 开始计算表达式的值，是否满足指定值
            if(eval(express_str) == equal_num):
                result_list.append(express_str)
                print('T%d : %s = %d' %(len(result_list),express_str,equal_num))

print('===============Calculation END! @ %s =================' %time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# 开始写入文件
print('\n=========开始写入文件=========')
with open('C:/Users/flyingaura/Desktop/answer.txt',mode = 'w') as out_file:
    # i = 0
    for i in range(len(result_list)):
        out_file.write('%d. %-5s \n' %(i+1,result_list[i]))

end_time = time.time()
print('\n============程序结束，共耗时 %d 秒! ===============' %(end_time - start_time))

