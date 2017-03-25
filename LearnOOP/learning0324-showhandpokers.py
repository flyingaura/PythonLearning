# -*- coding: utf-8 -*-
"""
生成扑克牌——梭哈游戏的所有牌型，并输出到文件‘showhand_pokers.dat’中
"""
from LearnModule import MY_math
import time

#定义一个扑克牌的类
class Apoker(object):
    def __init__(self,Pvalue,Pflower):       #一张扑克牌由牌面值和花色组成
        self.Pvalue = Pvalue
        self.Pflower = Pflower

    def Value_show(self):                   #定义扑克牌（J,Q,K,A，大小王）六个牌值
        ValueName = {'14':'A','11':'J','12':'Q','13':'K','99':'LK','100':'BK'}
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
for i in range(2,15):
    for fstr in poker_flower:
        one_poker = Apoker(i,fstr)
        All_pokers.append(one_poker)

# all_showhand = MY_math.combination(All_pokers,5)

#生成所有梭哈牌面，并输出到showhand_pokers.dat文件中
with open('C:/Users/flyingauraHome/Desktop/showhand_pokers.dat', mode = 'w') as outfile:
    icount = 0
    start_time = time.time()
    print(('<------Showhand Pokers Calculating Start : %s ------>'
                  %time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start_time))))
    outfile.write('<------Showhand Pokers Calculating Start : %s ------>\n'
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

