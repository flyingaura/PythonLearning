# -*- coding: utf-8 -*-

"""
应用巴比伦算法计算一个整数的平方根
 巴 比 伦 平 方 根 算 法 ：
(a) 猜 测 数 字 的 平 方 根 。
(b) 用 猜 测 的 数 字 除 原 数 。
(c) 计 算 步 骤 (b) 的 商 与 猜 测 数 的 平 均 值 。
(d) 对 第 （c） 步 的 平 均 值 再 作 猜 测 。
(e) 如 果 新 的 猜 测 值 与 旧 的 猜 测 值 不 同 ， 则 回 到 第 (b) 步 ； 否 则 ， 停 止 。
"""

# 定义一个利用巴比伦算法计算整数平方根的函数

def Cal_Square(n,guess_m = None,tolerance = 0.0000001):
#n为需要计算平方根的数；guess_m为猜测数，可不输入；tolerance为公差数，默认值为10e-7
    #==============参数校验===============
    if(guess_m == None):
        guess_m = int(n/2)
    try:
        int_n = int(n)
    except ValueError as e:
        raise ValueError('参数类型错误：%s --> 输入第1个参数必须为整数' %e)
    try:
        float_guess = abs(float(guess_m))    #猜测数转换为正数
    except ValueError as e:
        raise ValueError('参数类型错误：%s --> 输入第2个参数必须为非零浮点数' %e)
    if(float_guess == 0):
        raise ZeroDivisionError('参数类型错误 --> 输入第2个参数不能为零')

    negtive_tag = 0
    if(int_n < 0):
        negtive_tag = 1         #如果需要计算平方根的数为负数，则需要先做一个标记
    int_n = abs(int_n)

    #开始应用巴比伦算法计算平方根了
    root_num = 0.0
    count_int = 0
    while(abs(float_guess - root_num) > tolerance):
        root_num = float_guess
        float_guess = (int_n / float_guess + float_guess)/2
        count_int = count_int + 1

    if(negtive_tag):
        print('%d 的平方根为 ' %int(n),complex(0,float_guess))
        print('猜测数为 %f，计算次数为 %d' %(float(guess_m),count_int))
        return complex(0,float_guess)
    else:
        print('%d 的平方根为 %f' % (int(n), float_guess))
        print('猜测数为 %f，计算次数为 %d' % (float(guess_m), count_int))
        return float_guess

while(True):
    #=================需要计算平方根的数的输入控制==================
    exit_tag = 0
    while(True):
        num_str = input('请输入需要平方根的整数(q退出):')
        if(str.lower(num_str) == 'q'):
            exit_tag = 1
            break
        try:
            int_num = int(num_str)
        except ValueError as e:
            print('输入错误: %s --> 请输入整数' %e)
            continue
        break
    if(exit_tag):
        print('程序结束！')
        break
    # =================计算平方根所需猜测数的输入控制==================
    exit_tag = 0
    while (True):
        guess_str = input('请输入计算平方根所需要的猜测数(q退出):')
        if (str.lower(guess_str) == 'q'):
            exit_tag = 1
            break
        try:
            float_guess = float(guess_str)
        except ValueError as e:
            print('输入错误: %s --> 请输入任一实数' % e)
            continue
        break
    if (exit_tag):
        print('程序结束！')
        break

    root_value = Cal_Square(int_num,float_guess)
    Cal_Square(int_num)



