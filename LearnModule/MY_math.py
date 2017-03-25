# -*- coding: utf-8 -*-

"""
1、定义一个全奇数生成器,可以支持全序列和切片序列
2、定义一个判断是否为回数的函数
3、定义一个阶乘函数  factorial(n)
4、定义一个组合函数  combination（n,m）
5、定义一个从N个数的序列中取出M个数字的所有情况组合函数  fetch_in_list(n,m)
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
        int_num = int(n)
    except ValueError as e:
        raise ValueError('输入参数错误：%s' %e)

    reserve_num = ''
    for astr in str(n):
        reserve_num = astr + reserve_num
    if(reserve_num == str(n)):
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

# L = []
# for n in oddNum:
#     if(n < 100):
#         L.append(n)
#     else:
#         break
# print(list(L))

# # print(list(evenNum('1000')))
# for n in primesNum():
#     if (n < 100):
#         L.append(n)
#     else:
#         break
# #
# print(list(L))
# print(list(primesNum(100)))
