# -*- coding：utf-8 -*-

"""
1、猜数字的游戏

2、冰雹序列数字
冰 雹 序 列 所 用 公 式 如 下 ：
· 如 果 数 字 是 偶 数 ， 除 以 2 。
· 如 果 数 字 是 奇 数 ， 乘 以 3 ， 再 加1 。
· 当 数 等 于 1 时 ， 退 出 程 序 。

"""
# import random
#
# Anum = random.randint(0,100)
#
# guess_turns = 1
# while(True):
#     guess = input('第 %d 次：请输入一个0-100内的数字（q退出）：' %guess_turns)
#     run_tag = 1
#     if(str.lower(guess) == 'q'):
#         print('The game END!')
#         break
#     try:
#         guess_num = int(guess)
#     except ValueError as e:
#         print('类型错误:%s --->必须要输入0-100内的数字' %e)
#         run_tag = 0
#     if(run_tag):
#         if(0 <= guess_num <= 100):
#            if(guess_num < Anum):
#                print('猜得太小了！')
#            elif(guess_num > Anum):
#                print('猜得太大了')
#            else:
#                print('你猜对了！正确的数字是：%d。<--你猜了 %d 次-->' %(Anum,guess_turns))
#                print('The game END!')
#                break
#            guess_turns = guess_turns + 1
#         else:
#             print('所输入数字范围不正确，请输入0-100内的数字！')

#冰雹序列数字生成
import matplotlib
import numpy
from matplotlib import pylab

def Hailstone(n):
    Hseq = [n]
    while(n != 1):
        if(n % 2 == 0):
            n = int(n / 2)
        else:
            n = n * 3 + 1
        Hseq.append(n)
    return Hseq

while(True):
    numstr = input('请输入任意一个整数（q退出）：')
    # run_tag = 1
    if(str.lower(numstr) == 'q'):
        print('程序结束！')
        break
    try:
        Anum = abs(int(numstr))
    except ValueError as e:
        print('输入类型错误：%s --> 必须输入整数')
        continue
    # if(run_tag):
    Hailstone_seq = Hailstone(Anum)
    print('%d 的冰雹序列为：' %Anum,list(Hailstone_seq))
    print('======程序继续执行=======')

    # pylab.plot(Hailstone_seq)
    # pylab.show()