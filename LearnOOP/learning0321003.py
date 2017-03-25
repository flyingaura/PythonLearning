# -*- coding: utf-8 -*-

# 第一章的作业

# question 22 in chapter 1

# No.22
# question:
"""
利用圆括号可以改变运算顺序。例如a+b*c、(a+b)*c和a+(b*c)。
一般来说，这些表达式中有两个是相同的，另有一个有所不同。
经过反复试验，找到a、b和c的整数集合，使所有三个表达式得到相同的价值，并且a！=b！=c。
"""
#
# sstr = '25 ． 一 天 有86400 秒 （ 2 4*60*60 )。 给 定 一 个 范 围 I ~ 86400 ， 输 出 当 前 时 间 ， 格 式 为 小 时 ， 分 钟 和 秒 ， 以 24 小 时 表 示 。 例 如 ： 70000 秒 为 19 小时 ， 26 分 钟 和40 秒 。 '
# rstr = ''
# with open('C:/Users/flyingaura/Desktop/aaa.txt', mode = 'w') as result_file:
#     for stemp in sstr:
#         if(stemp != ' '):
#             rstr = rstr + stemp
#     result_file.write(rstr)

# def Aexp(a,b,c):
#     return a + b * c
#
# def Bexp(a,b,c):
# #     return (a + b) * c
# ANumList = []
# BNumList = []
# for a in range(1,100):
#     for b in range(1,100):
#         for c in range(1，100):
#             if ((a + b * c) == ((a + b) *c) ):
#                 ANumList.append([a,b,c])
#                 if(a != b and b != c and c != a):
#                     BNumList.append([a,b,c])
#
# print('满足条件1的答案为：',list(ANumList))
# print('满足条件2的答案为：',list(BNumList))


# No.22
# # question:
# """25．一天有86400秒（24*60*60)。
# 给定一个范围1~86400，输出当前时间，格式为小时，分钟和秒，以24小时表示。
# 例如：70000秒为19小时，26分钟和40秒。
# """

def Sec2Time(sec_num):
    days = 0
    while(sec_num > 86400):
        sec_num = sec_num - 86400
        days = days + 1  #超过86400的则算多少天

    hours = int(sec_num/3600) + days * 24  #超过1天的要加上每天24小时
    minutes = int((sec_num%3600)/60)
    seconds = (sec_num%3600)%60

    return [hours,minutes,seconds]

while(True):
    run_tag = 1
    secs = input('请输入秒数（q退出）：')
    if(str.lower(secs) == 'q'):
        print('程序结束！')
        break
    try:
        secstime = Sec2Time(int(secs))
    except ValueError as e:
        print('错误类型：%s —— 输入秒数的类型错误，必须为正整数 ！' %e)
        run_tag = 0
    if(run_tag):
        print('转换后的时间为：%d 小时 %d 分钟 %d 秒' %(secstime[0],secstime[1],secstime[2]))
    else:
        print('请重新输入！')



