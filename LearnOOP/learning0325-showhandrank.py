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
from LearnModule import StringSplit
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

#定义一个判断是否同花的函数
def flush_poker(onehand):    #onehand里必须存放Apoker类的实例
    # ============参数校验=============
    if(not isinstance(onehand,(list,tuple))):
        raise ValueError('参数错误 --> 参数必须为序列类型（list 或者 tuple）')
    # ============参数校验=============
    for onepoker in onehand:
        if(onepoker.Pflower != onehand[0].Pflower):
            return False
    return True

# 定义一个判断是否顺子的函数
def Straight_poker(onehand):   #onehand里必须存放Apoker类的实例
    # poker_value = []
    # for onepoker in onehand:
    #     poker_value.append(onepoker.Pvalue)
    onehand = sorted(onehand,key = lambda poker: poker.Pvalue)
    for i in range(len(onehand)-1):
        if(onehand[i+1].Pvalue - onehand[i].Pvalue != 1):
            return False
    return True

# 定义一个数对子（包括三对，四对）的函数
def count_pairs(onehand):   #onehand里必须存放Apoker类的实例
    save_pairs = []
    pairs_num = 0
    onehand = sorted(onehand, key=lambda poker: poker.Pvalue)
    for i in range(len(onehand) - 1):
        if(onehand[i].Pvalue == onehand[i+1].Pvalue):
            pairs_num = pairs_num + 1
        elif(pairs_num != 0):
            save_pairs.append(pairs_num)
            pairs_num = 0
    if(pairs_num != 0):
        save_pairs.append(pairs_num)
    return save_pairs


# 定义10种牌型的分别对应的列表
showhand_rank0 = []  # 0         空手（Nothing in hand）     没有牌
showhand_rank1 = []  # 1         一对（One Pair）            在5张牌中有1对大小相同
showhand_rank2 = []  # 2         两对（Two Pairs）           在5张牌中有2对大小相同
showhand_rank3 = []  # 3         三条（Three of a kind）     在5张牌中有3张为相同值
showhand_rank4 = []  # 4         顺子（Straight）            5张牌按顺序排列，没有间隔
showhand_rank5 = []  # 5         同花（Flush）               5张牌为同一花色
showhand_rank6 = []  # 6         满堂彩（Full house）        一对加上3张相同分值的牌
showhand_rank7 = []  # 7         四条（Four of a kind）      在5张牌中有4张为相同值
showhand_rank8 = []  # 8        同花顺(Straight flush)        同花顺
showhand_rank9 = []  # 9        皇家同花顺（Rowya flush）    [A,K,Q,J,10] + flush

rank_table = {'0':'空手（Nothing in hand）','1':'一对（One Pair）','2':'两对（Two Pairs）','3':'三条（Three of a kind）',
              '4':'顺子（Straight）','5':'同花（Flush）','6':'满堂彩（Full house）','7':'四条（Four of a kind）',
              '8':'同花顺(Straight flush)','9':'皇家同花顺（Rowya flush）'}     #定义一个牌面等级说明对应表
# 打开梭哈扑克牌面文件 showhand_pokers.dat
with open('C:/Users/flyingauraHome/Desktop/showhand_pokers.dat', mode = 'r') as showhandfile:
    showhandfile.readline()

    #===========================开始计算各种牌面类型===========================
    start_time = time.time()
    print('============== Showhand Pokers Aggregations by Ranks! Now Starting Calculation @ %s =============='
          % time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)))
    showhand_count = 0
    for line in showhandfile.readlines():     #每一行:[A(1),Heart]	[A(1),Spade]	[A(1),Diamond]	[A(1),Club]	[2(2),Heart]
        error_tag = 0
        onehand = []
        for mpoker in StringSplit.stringsplit(line.strip(),('[',']','\t')):    #分解成5个独立的poker牌字符串:A(1),Heart
            ppoker = StringSplit.stringsplit(mpoker,('(',')',','))  #每个poker牌字符串分解成poker的三种属性:A,1,Heart
            try:
                onehand.append(Apoker(int(ppoker[1]),ppoker[2]))
            except ValueError as e:
                print('ValueError:%s' %e)
                error_tag = 1
                # showhand_count = showhand_count - 1
        # for onepoker in onehand:
        #     print('[%s(%d),%s]' % (onepoker.Value_show(), onepoker.Pvalue, onepoker.Pflower), end='\t')
        # print('\n')
        if(error_tag):
            continue
        straight_tag = 0
        pairs_poker = count_pairs(onehand)
        if(pairs_poker == []):
            if(Straight_poker(onehand)):
                showhand_rank4.append(onehand)
                straight_tag = 1
            if(flush_poker(onehand)):
                showhand_rank5.append(onehand)
                if(straight_tag):
                    showhand_rank8.append(onehand)
                    for onepoker in onehand:
                        if(onepoker.Pvalue == 14):
                            showhand_rank9.append(onehand)
            elif(not straight_tag):
                showhand_rank0.append(onehand)
        elif(len(pairs_poker) == 1):
            if(pairs_poker[0] == 1):
                showhand_rank1.append(onehand)
            elif(pairs_poker[0] == 2):
                showhand_rank3.append(onehand)
            else:
                showhand_rank7.append(onehand)
        else:
            twopairs_tag = 1
            for num in pairs_poker:
                if(num > 1):
                    showhand_rank6.append(onehand)
                    twopairs_tag = 0
            if(twopairs_tag):
                    showhand_rank2.append(onehand)
        showhand_count = showhand_count + 1
    end_time = time.time()
    print('============== Showhand Pokers %d hands Aggregations by Ranks Completed ! @ %s || used time: %f seconds =============='
        %(showhand_count,time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time)),end_time - start_time))

all_showhand = [showhand_rank0,showhand_rank1,showhand_rank2,showhand_rank3,showhand_rank4,showhand_rank5,
                showhand_rank6,showhand_rank7,showhand_rank8,showhand_rank9]
# ==================== 开始写入梭哈扑克牌等级文件 showhand_rank.dat ====================
startw_time = time.time()
with open('C:/Users/flyingauraHome/Desktop/showhand_rank.dat', mode = 'w') as outfile:
    print('======================= 开始写入文件 @ %s ======================='
          %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(startw_time))))
    outfile.write('========== showhand pokers total hands: %d ==========\n' %showhand_count)
    index_num = sorted(list(range(10)),reverse = True)
    for i in index_num:
        showhand_length = len(all_showhand[i])
        print('========== showhand pokers rank %d - %s --> total count: %d | Fetch rate：%f %%==========\n'
                      % (i, rank_table[str(i)], showhand_length, 100 * showhand_length / showhand_count))
        outfile.write('\n========== showhand pokers rank %d - %s --> total count: %d | Fetch rate：%f %%==========\n'
                      %(i,rank_table[str(i)],showhand_length,100 * showhand_length / showhand_count))
        for onehand in all_showhand[i]:
            for onepoker in onehand:
                outfile.write('[%s(%d),%s]\t' %(onepoker.Value_show(),onepoker.Pvalue,onepoker.Pflower))
            outfile.write('%d \n' %i)

    endw_time = time.time()
    print('======================= 文件写入完毕 @ %s || used time: %f seconds======================='
          %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(endw_time)),endw_time - startw_time))

print('======================= 程序运行完毕 @ %s || 总用时: %f seconds======================='
          %(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())),endw_time - start_time))



# for ahand in showhand_rank0:
#     for onepoker in ahand:
#     # for onepoker in sorted(ahand,key = lambda poker: poker.Pvalue,reverse = True):
#         print('[%s(%d),%s]' %(onepoker.Value_show(),onepoker.Pvalue,onepoker.Pflower),end = '\t')
#     print('\n')







