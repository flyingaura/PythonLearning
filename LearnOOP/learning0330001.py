# -*- coding: utf-8 -*-

# zero_list = [0] * 100
# print(len(zero_list),zero_list)

# even_num = [2 * x for x in range(20)]
# print(even_num)
# text = ''
# for i in range(1,6):
#     text = text.join(str(i))
#     print(text)
# print(text,text.center(10))
# str_list = [str(x) for x in range(1,6)]
# str_list = '1'
# print(str_list)
# text = 'one'.join(str_list)
# print(text)

# char_list = [chr(i) for i in range(ord('a'),ord('z')+1)]
# Pchar_list = []
# for i in range(len(char_list)):
#     Pchar_list.append(char_list[-(i + 1):])
#
# print(Pchar_list)
#
# while(True):
#     in_str = input('请输入一个字符串(q退出)：')
#     if(in_str.lower() == 'q'):
#         print('程序结束')
#         break
#     # astr_list = [astr for astr in in_str]
#     # out_str =
#     print('排序后的字符串为：%s' %(''.join(sorted([astr for astr in in_str]))))

# 用元组表示分数，并实现分数相加和分数相乘

# fraction_num = (2,3)  fraction_num[0]-->分子，fraction_num[1]-->分母

# 定义一个输出最大公约数的函数cal_GCD(a,b)
def cal_GDC(a,b):
    try:
        a = int(a)
        b = int(b)
    except ValueError as e:
        raise ValueError('参数错误: %s-->所输入参数必须为整数' %e)

    if (a == 0 or b == 0):
        return 0
    if(a <= b):
        temp_divisor = a
    else:
        temp_divisor = b

    # GCD_result = 0
    for i in range(temp_divisor,0,-1):
        if(a % i == 0 and b % i == 0):
            return i

# 定义一个输出标准分数的函数，标准分数：分子和分母的最大公约数是1
def st_fraction(a,b):
    try:
        a = int(a)
        b = int(b)
    except ValueError as e:
        raise ValueError('参数错误: %s-->所输入参数必须为整数' %e)
    if(b == 0):
        raise ZeroDivisionError('严重错误，0不能做为分母！')

    GCD_num = cal_GDC(a,b)         #计算两个数的最大公约数
    return (int(a / GCD_num),int(b / GCD_num))

# 两个分数的加法函数
def fraction_add(fca,fcb):
    if(not isinstance(fca,tuple) or not isinstance(fcb,tuple)):
        raise ValueError('参数错误-->两个参数必须为元组类型(分子，分母）!')
    fractions = (fca[0]*fcb[1] + fcb[0]*fca[1])  #分数加法中分子计算公式
    numerator = fca[1] * fcb[1]              #分数加法中分母计算公式
    return st_fraction(fractions,numerator)    #将计算出的分子分母进行标准化再输出

# 两个分数的乘法函数
def fraction_multi(fca,fcb):
    if (not isinstance(fca, tuple) or not isinstance(fcb, tuple)):
        raise ValueError('参数错误-->两个参数必须为元组类型(分子，分母）!')

    fractions = fca[0] * fcb[0]              #分数乘法中分子计算公式
    numerator = fca[1] * fcb[1]              #分数乘法中分母计算公式
    return st_fraction(fractions,numerator)    #将计算出的分子分母进行标准化再输出

a = (5,8)
b = (12,16)
print('第一个分数为：',a)
print('第二个分数为：',b)
print('两个分数相加结果为：',fraction_add(a,b))
print('两个分数相乘结果为：',fraction_multi(a,b))





