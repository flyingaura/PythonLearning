# -*- coding: utf-8 -*-
# 完全数计算

"""
完全数计算
完全数是由古人创造的一种整数，它至少可以追到公元前3年左右的欧几里得时期。
完全数是一个整数．其因数的和（不含本身的因素）加起来就是数字本身。
如：
6 = 1 + 2 + 3
28 = 1 + 2 + 4 + 7 + 14
"""
#
# sstr = '完 全 数 是 由 古 人 创 造 的 一 种 整 数 ， 它 至 少 可 以 追 到 公 元 前 3 年 左 右 的 欧 几 里 得 时 期 。 完 全 数 是 一 个 整 数 ． 其 因 数 的 和 （ 不 含 本 身 的 因 素 ） 加 起 来 就 是 数 字 本 身 。  '
# rstr = ''
# with open('C:/Users/flyingaura/Desktop/aaa.txt', mode = 'w') as result_file:
#     for stemp in sstr:
#         if(stemp != ' '):
#             rstr = rstr + stemp
#     result_file.write(rstr)

# 定义一个能被整除的过滤函数
def division_filter(n):
    return lambda x: n % x == 0

# 定义一个求某个自然数所有因数的函数
def facal_num(n):
    if(n == 0):
        print('请输入大于零的整数！')
        return None
    abs_n = abs(n)
    facal_list = filter(division_filter(n),range(1,abs_n+1))
    return facal_list

# ret = facal_num(101)
# print(list(ret))

# 定义一个判定是否为完全数的函数
def perfect_num(n):
    sumofdivisor = 0
    addstr = ''

    for i in facal_num(n):
        if(i < n):
            sumofdivisor = sumofdivisor + i
            addstr = addstr + str(i) + ' + '   #处理完全数的输出结果
    # for astr in addstr:
    #     out_num.append(astr)
    # out_num[-1] = '='
    out_str = addstr[:len(addstr)-3]    #处理完全数的输出结果

    if(sumofdivisor == n):
        print('%d 是一个完全数！---> %s = %d' %(n,out_str,n))
        return True
    elif(sumofdivisor > n):
        print('%d 是一个丰沛数！---> %s > %d' %(n,out_str,n))
        return False
    else:
        print('%d 是一个不足数！---> %s < %d' %(n,out_str,n))

per_numlist = []
n = 1000
for i in range(1,n):
    if(perfect_num(i)):
        per_numlist.append(i)
print('%d 以内的完全数有：' %n,list(per_numlist))