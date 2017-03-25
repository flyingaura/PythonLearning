# -*- coding: utf-8 -*-

"""
做作业
chapter 2
program 1
program 4
"""

# program 1 :发明国际象棋的价值

from LearnModule import Num2Chinese
#
# num = 1
# sum_num = 0
#
# for i in range(64):
#     sum_num = sum_num + num
#     print('第 %d 格，放 %d 粒小麦，总计小麦粒数 %d (%s 粒) ' %(i+1,num,sum_num,Num2Chinese.Num2Chinese(sum_num)))
#     num = num * 2
#
# mai_weight = float(sum_num*50)/1000/1000   #单位为千克
# print('全部放满棋盘所需的小麦总重量为： %f (%s 千克)' %(mai_weight,Num2Chinese.Num2Chinese(mai_weight)))
#
# volume_weight = 750   #每立方米小麦为750千克
#
# total_volume = float(mai_weight/volume_weight)  #单位为立方米
#
# China_area = 9600000  #中国国土面积，单位为平方千米
#
# mai_deepth = total_volume/(China_area * 1000 * 1000)   #单位为米
#
# print('全部放满棋盘所需的小麦总体积为 %f 立方米，放满中国国土面积后，将覆盖 %f 米深' %(total_volume,mai_deepth))

# program 4：古怪的乘法——“俄国农民”和“古埃及”乘法

def strange_multi(n,m):
    try:
        int_n = int(n)
        int_m = int(m)
    except ValueError as e:
        print('参数错误：%s' %e)
        return None

    sum_num = int_n
    step_num = []
    used_num = [int_n]
    while(int_m > 0):
        step_num.append([int_n,int_m])
        int_n = int_n * 2              #古怪乘法的规则:
        int_m = int(int_m / 2)         #...
        if(int_m % 2 == 1):              #...
            sum_num = sum_num + int_n    #...
            used_num.append(int_n)
    return [sum_num,used_num,step_num]    #返回乘法结果、所用的乘数以及所有步骤的中间数

# # 正式开始运行古怪乘法的游戏
# confirm_str = ['y','yes']
# confirm_button = 'y'
# while(str.lower(confirm_button) in confirm_str):
#     stop_tag = 0
#     while(True):
#         Anum_str = input('请输入第一个乘数（q退出）:')
#         if(str.lower(Anum_str) == 'q'):
#             # print('程序结束')
#             stop_tag = 1
#             break
#         try:
#             Anum = int(Anum_str)
#         except ValueError as e:
#             print('输入错误： %s --> 输入乘数必须为正整数' %e)
#             continue
#         if(Anum <= 0):
#             print('输入错误，输入乘数必须为正整数！')
#             continue
#         break
#     if(stop_tag):
#         print('程序结束 !')
#         break
#     while (True):
#         Bnum_str = input('请输入第二个乘数（q退出）:')
#         if (str.lower(Bnum_str) == 'q'):
#             stop_tag = 1
#             break
#         try:
#             Bnum = int(Bnum_str)
#         except ValueError as e:
#             print('输入错误： %s --> 输入乘数必须为正整数' % e)
#             continue
#         if (Bnum <= 0):
#             print('输入错误，输入乘数必须为正整数！')
#             continue
#         break
#     if (stop_tag):
#         print('程序结束 !')
#         break
#
#     result_sm = strange_multi(Anum,Bnum)
#     # print(list(result_sm))
#     print('古怪乘法的所有步骤如下：')
#     i = 0
#     for ilist in result_sm[2]:
#         i = i + 1
#         print('第 %d 步： A --> %d || B --> %d' %(i,ilist[0],ilist[1]))
#     print('==========================================================')
#     add_str = ''
#     if(len(result_sm[1]) == 1):
#         add_str = result_sm[1][0]
#     else:
#         for i in range(len(result_sm[1])-1):
#             add_str = add_str + str(result_sm[1][i]) + ' + '
#         add_str = add_str + str(result_sm[1][-1])
#     print('乘数 %d 和乘数 %d 的古怪乘法结果为：%s = %d' %(Anum,Bnum,add_str,result_sm[0]))
#     normal_multi = Anum * Bnum
#     if(result_sm[0] > normal_multi):
#         print('古怪乘法的乘积%d 大于 正常乘法乘积 %d * %d = %d' %(result_sm[0],Anum,Bnum,normal_multi))
#     elif (result_sm[0] < normal_multi):
#         print('古怪乘法的乘积%d 小于 正常乘法乘积 %d * %d = %d' % (result_sm[0], Anum, Bnum, normal_multi))
#     else:
#         print('完美!!古怪乘法的乘积%d 等于 正常乘法乘积 %d * %d = %d' % (result_sm[0], Anum, Bnum, normal_multim))
#
#     print('==========================================================')
#     confirm_button = input('还想继续算吗？Y继续，其他任意字符退出 >>> ')

# 改造上述程序，使其输出两个乘数都是100以内，古怪乘法乘积分别为大于、等于、小于正常乘积乘法的乘数对
equal_list = []
bigger_list = []
smaller_list = []
for i in range(1,100):
    for j in range(1,100):
        normal_multi = i * j
        result_sm = strange_multi(i,j)
        out_list = [i,j,result_sm[0],normal_multi]
        if(result_sm[0] > normal_multi):
            bigger_list.append(out_list)
        elif(result_sm[0] < normal_multi):
            smaller_list.append(out_list)
        else:
            equal_list.append(out_list)
with open('C:/Users/flyingaura/Desktop/aaa.txt', mode = 'w') as result_file:
    result_file.write('================ 古怪乘法乘积 等于 正常乘法乘积 总计 %d 组 ================ \n\n' %(len(equal_list)))
    result_file.write('|%-10s|%-10s|%-10s|%-10s| \n' %('NumA','NumB','Str_result','Nor_result'))
    for ilist in equal_list:
        result_file.write('|%-10d|%-10d|%-10d|%-10d| \n' %(ilist[0],ilist[1],ilist[2],ilist[3]))
    result_file.write('\n\n')
    result_file.write('================ 古怪乘法乘积 大于 正常乘法乘积 总计 %d 组 ================ \n\n'%(len(bigger_list)))
    result_file.write('|  乘数A  |  乘数B  |  古怪乘积  |  正常乘积  | \n')
    for ilist in bigger_list:
        result_file.write('|  %d  |  %d  |  %d  |  %d  | \n' % (ilist[0], ilist[1], ilist[2], ilist[3]))
    result_file.write('\n\n')
    result_file.write('================ 古怪乘法乘积 小于 正常乘法乘积 总计 %d 组 ================ \n\n' %(len(smaller_list)))
    result_file.write('|  乘数A  |  乘数B  |  古怪乘积  |  正常乘积  | \n')
    for ilist in smaller_list:
        result_file.write('|  %d  |  %d  |  %d  |  %d  | \n' % (ilist[0], ilist[1], ilist[2], ilist[3]))



