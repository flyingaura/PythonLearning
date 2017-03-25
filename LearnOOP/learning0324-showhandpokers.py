# -*- coding: utf-8 -*-
"""
计算扑克牌——梭哈游戏的所有可能性以及各种牌面概率
    等级           牌面名称                  规则
    9        皇家同花顺（Rowya flush）    [A,K,Q,J,10] + flush
    8        同花顺(Straight flush)        同花顺
    7         四条（Four of a kind）      在5张牌中有4张为相同值
    6         满堂彩（Full house）        一对加上3张相同分值的牌
    5         同花（Flush）               5张牌为同一花色
    4         顺子（Straight）            5张牌按顺序排列，没有间隔
    3         三条（Three of a kind）     在5张牌中有3张为相同值
    2         两对（Two Pairs）           在5张牌中有2对大小相同
    1         一对（One Pair）            在5张牌中有1对大小相同
    0         空手（Nothing in hand）     没有牌
"""
from LearnModule import MY_math
import time

#定义一个扑克牌的类
class Apoker(object):
    def __init__(self,Pvalue,Pflower):       #一张扑克牌由牌面值和花色组成
        self.Pvalue = Pvalue
        self.Pflower = Pflower

    def Value_show(self):                   #定义扑克牌（J,Q,K,A，大小王）六个牌值
        ValueName = {'1':'A','11':'J','12':'Q','13':'K','99':'LK','100':'BK'}
        if(str(self.Pvalue) in ValueName.keys()):
            poker_vn = ValueName[str(self.Pvalue)]
        else:
            poker_vn = str(self.Pvalue)
        return poker_vn

# onepoker = Apoker(12,'redheart')
# print(onepoker.Pvalue,onepoker.Pflower,onepoker.Value_show())

#定义打扑克牌四种花色：红心-->Heart，黑桃-->Spade，方块-->Diamond，梅花-->Club
poker_flower = ['Heart','Spade','Diamond','Club']
#初始化所有扑克牌
All_pokers = []
for i in range(1,14):
    for fstr in poker_flower:
        one_poker = Apoker(i,fstr)
        All_pokers.append(one_poker)

# all_showhand = MY_math.combination(All_pokers,5)

#生成所有梭哈牌面，并写入到showhand_pokers.txt文件中
with open('C:/Users/flyingauraHome/Desktop/showhand_poker.txt', mode = 'w') as outfile:
    icount = 0
    start_time = time.time()
    print(('<------Showhand Pokers Calculating Start : %s ------>'
                  %time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time))))
    outfile.write('<------Showhand Pokers Calculating Start : %s ------>'
                  %time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time)))  #记录计算开始时间

    for onehand in MY_math.fetch_in_list(All_pokers,5):  #引用组合函数进行计算
        # print('<------ 开始写文件：%s ------>' %time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        icount = icount + 1
        for onepoker in onehand:
            outfile.write('[%s(%d),%s]\t' %(onepoker.Value_show(),onepoker.Pvalue,onepoker.Pflower))
        outfile.write('\n')
    end_time = time.time()
    outfile.write('<------Showhand Pokers %d kinds, Calculating END : %s  used time %f seconds------>'
                  %(icount,time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)),end_time - start_time))

    print('<------Showhand Pokers %d kinds, Calculating END : %s  used time %f seconds------>'
                  %(icount,time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)),end_time - start_time))


# print('[牌面，花色] 共有 %d 张牌' %(len(All_pokers)))
# for apoker in All_pokers:
#     print('[%s ,%s]' %(apoker.Value_show(),apoker.Pflower))

