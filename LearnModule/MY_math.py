# -*- coding: utf-8 -*-
import random
import math

"""
1、定义一个全奇数生成器,可以支持全序列和切片序列
2、定义一个判断是否为回数的函数
3、定义一个阶乘函数  factorial(n)
4、定义一个组合函数  combination（n,m）
5、定义一个从N个数的序列中取出M个数字的所有情况组合函数  fetch_in_list(n,m)
6、定义一个从N个数的序列中取出M个数字的所有情况排列函数  array_in_list(n,m)
7、定义一个从N个数的序列中遍历取M次的所有情况排列函数（M可大于N）　through_in_list(n,m)
8、定义一个从0~N数据范围中随机取出指定M个数据的随机数函数   RandomFetch(N,M)
9、定义一个取两个正整数最大公约数的函数   CalGCD(N1,N2)
10、定义一个取两个正整数最小公倍数的函数  CalLCM(N1,N2)

"""

def oddNum(n = None):
    Num = 1
    if(n == None):
        while True:
            yield Num
            Num = Num + 2
    elif(isinstance(n,int)):
        while (Num <= n):
            yield Num
            Num = Num + 2
    # elif(isinstance(n,slice)):
    #     nstart = slice.start
    #     nstop = slice.stop
    #     if(nstart == None and nstop == None):
    #         while True:
    #             yield Num
    #             Num = Num + 2
    #     elif (nstart == None and nstop != None):
    #         while (Num <= nstop):
    #             yield Num
    #             Num = Num + 2
    #     elif(nstart != None and nstop == None):
    #         while True:
    #             if(Num >= nstart):
    #                 yield Num
    #             Num = Num + 2
    #     else:
    #         while(Num <= nstop):
    #             if(Num >= nstart):
    #                 yield Num
    #             Num = Num + 2
    #

    else:
        raise ValueError('The type of parameters is not int !')


# "定义一个偶数生成器"
def evenNum(n = None):
    Num = 2
    if (n == None):
        while True:
            yield Num
            Num = Num + 2
    elif (not isinstance(n, int)):
        raise ValueError('The type of parameters is not int !')
    else:
        while (Num <= n):
            yield Num
            Num = Num + 2

# "定义一个素数生成器"
def primes_filter(n):  #定义一个素数的过滤方法
    return lambda x: x % n > 0

def primesNum(n = None):  #定义一个素数生成器
    yield 2
    it = oddNum()
    if (n == None):
        while True:
            outnum = next(it)
            if(outnum > 2):
                yield outnum
                it = filter(primes_filter(outnum),it)
    elif (not isinstance(n, int)):
        raise ValueError('The type of parameters is not int !')
    else:
        outnum = next(it)
        while (outnum <= n):
            if(outnum > 2):
                yield outnum
                it = filter(primes_filter(outnum),it)
            outnum = next(it)


def if_synnum(n):
    try:
        str_n = str(n)
    except ValueError as e:
        raise ValueError('输入参数错误：%s' %e)

    # reserve_num = ''
    # for astr in str(n):
    #     reserve_num = astr + reserve_num
    if(str_n[::-1] == str_n):
        return True
    else:
        return False

def factorial(n):
    # ============参数校验=============
    try:
        int_n = int(n)
    except ValueError as e:
        raise ValueError('参数错误 ：%s --> 输入参数必须为正整数' %e)

    if(int_n < 0):
        raise ValueError('参数错误 --> 输入参数必须为正整数')

    # ============开始计算=============
    if(int_n == 0 or int_n == 1):
        return 1
    result_facn = int_n * factorial(int_n-1)
    return result_facn

def combination(n,m):
    # ============参数校验=============
    try:
        int_n = int(n)
        int_m = int(m)
    except ValueError as e:
        raise ValueError('参数错误 ：%s --> 两个输入参数都必须为正整数' % e)

    if(int_n < 1 or int_m < 1):
        raise ValueError('参数错误 --> 输入参数必须为正整数')

    if(int_n < int_m):
        raise ValueError('参数错误 --> 第一个参数必须大于等于第二个参数')

    # ============开始计算=============

    return int(factorial(n)/(factorial(m) * factorial(n-m)))

def fetch_in_list(nlist,m):
    """
    定义一个从N个数的序列中取出M个数字的所有情况组合函数  NewFetch_in_list(nlist,m)
    """
    # ============参数校验=============
    if(not isinstance(nlist,(str,list,tuple))):
        raise ValueError('参数错误 --> 第一个输入参数必须为序列类型（list或者tuple）')

    try:
        # int_n = int(n)
        int_m = int(m)
    except ValueError as e:
        raise ValueError('参数错误 ：%s --> 输入取数数量参数都必须为正整数' % e)

    if(len(nlist) < int_m):
        raise ValueError('参数错误 --> 输入的取数数量参数不能大于序列长度')

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


# 6、定义一个从N个数的序列中取出M个数字的所有情况排列函数  array_in_list(n,m)

def array_in_list(nlist,m):
    # ============参数校验=============
    if(not isinstance(nlist,(str,list,tuple))):
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
    # ============定义退出条件=============
    num_list = []
    if (m == 1):
        for n in nlist:
            num_list.append([n])
        return num_list

        # ============递归计算=============
    for i in range(len(nlist)):
        temp_num = nlist[i]
        temp_numlist = nlist.copy()
        temp_numlist.pop(i)
        for temp_list in array_in_list(temp_numlist, m - 1):  # 从序列中取一个，从剩下序列中取剩下几个
            temp_list.insert(0, temp_num)
            num_list.append(temp_list)

    return num_list

# 7、定义一个从N个数的序列中遍历取M次的所有情况排列函数（M可大于N）　through_in_list(n,m)
def through_in_list(strlist,m):
    if (not isinstance(strlist, (str, list, tuple))):
        raise ValueError('参数错误 --> 第一个输入参数必须为序列类型（list或者tuple）')

    try:
        # int_n = int(n)
        int_m = int(m)
    except ValueError as e:
        raise ValueError('参数错误 ：%s --> 第二个参数必须为正整数' % e)

    result_list = []
    if(m == 1):
        for astr in strlist:
            result_list.append([astr])
        return result_list

    for astr in strlist:
        for aresult in through_in_list(strlist,m - 1):
            aresult.insert(0,astr)
            result_list.append(aresult)

    return result_list

#8、定义一个从0~N数据范围中随机取出指定M个数据的随机数函数
def RandomFetch(N,M):
    """
    从0~N数据范围中随机取出指定M个数据的随机数函数，如果 N <= M，则直接返回set(range(N + 1))
    """
    try:
        N = int(N)
        M = int(M)
    except ValueError as e:
        raise ValueError('%s --> 参数错误，无法转换为整数' %e)

    RandomSet = set()

    if(N <= M):
        RandomSet = set(range(N + 1))
    else:
        while(len(RandomSet) < M):
            RandomSet.add(random.randint(0,N))

    return RandomSet

# 9、定义一个取两个正整数最大公约数的函数   CalGCD(N1,N2)
# def CalGCD(N1,N2):
#     if(N1 <= 0 or N2 <= 0):
#         raise ValueError('两个输入参数必须为正整数！')
#     N_gcd = 1
#     if(N1 == 1 or N2 == 1):
#         return N_gcd
#     if(N1 <= N2):
#         Ntemp = N1
#     else:
#         Ntemp = N2
#
#     for i in range(2,Ntemp + 1):
#         if(N1 % i == 0 and N2 % i == 0):
#             N_gcd = i
#
#     return N_gcd

def CalGCD(N1,N2):

    if(not isinstance(N1,int) or not isinstance(N2,int)):
        raise ValueError('所输入参数必须为整数！')
    N1 = abs(N1)
    N2 = abs(N2)

    if(N1 > N2):
        N1, N2 = N2, N1

    while(N1):
        N1, N2 = N2 % N1, N1

    return N2

    # if(N1 == 0):
    #     return N2
    #
    # N_Gcd = CalGCD(N1, N2 % N1)
    #
    # return N_Gcd

# 10、定义一个取两个整数最小公倍数的函数  CalLCM(N1,N2)
def CalLCM(N1,N2):
    if (not isinstance(N1, int) or not isinstance(N2, int)):
        raise ValueError('所输入参数必须为整数！')

    return int((N1 * N2) / CalGCD(N1,N2))

