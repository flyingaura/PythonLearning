# -*- coding: utf-8 -*-
"""
用于扑克牌类游戏的基本属性定义，包含几个类和函数：
1、扑克牌类 PukeCard;
2、定义一幅完整的扑克牌 initPukeCards(NeedGhost = 0)   NeedGhost 表示这幅牌里需不需要大小王,0表示不需要
2、洗牌函数 shuffer(CardsList)
3、判断是否为大小顺序但花色混接的函数  ifMashup(cardlist,onecard)

"""

__author__ = 'Flyingaura_wl'
__edittime__ = '20170812'

import random

class Poker(object):

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    # 单张牌的输出表示,标准输出表示（即1-->A,11-->J,12-->Q,13-->K）
    def __str__(self):
        standPoker = {1: 'A', 11: 'J', 12: 'Q', 13: 'K', 98: 'joker', 99: 'joker'}
        if (self.rank in standPoker.keys()):
            return '(%s,%s)' % (standPoker[self.rank], self.suit)
        else:
            return '(%s,%s)' % (str(self.rank), self.suit)

    #定义一个为方便空当接龙游戏的牌型显示方法（红和黑花用一个显目符号区别标识）
    def GameShow(self):
        standPoker = {1: 'A', 11: 'J', 12: 'Q', 13: 'K', 98: 'joker', 99: 'joker'}
        SuitClass = {'黑桃':'●', '红心':'○', '方块':'○', '梅花':'●'}
        if (self.rank in standPoker.keys()):
            return '(%s,%s,%s)' % (standPoker[self.rank], self.suit,SuitClass[self.suit])
        else:
            return '(%s,%s,%s)' % (str(self.rank), self.suit,SuitClass[self.suit])

    # # 定义一个将扑克牌对象转换为str类型的方法
    # def tostr(self):
    #     standPoker = {1: 'A', 11: 'J', 12: 'Q', 13: 'K', 98: 'joker', 99: 'joker'}
    #     if (self.rank in standPoker.keys()):
    #         return '(%s,%s)' % (standPoker[self.rank], self.suit)
    #     else:
    #         return '(%s,%s)' % (str(self.rank), self.suit)

def initPokerCards(NeedGhost = 0):
    AllCardslist = []
    SuitValue = ['黑桃','红心','方块','梅花']
    for i in range(1,14):
        for Asuit in SuitValue:
            OnePokerCard = Poker(i,Asuit)
            AllCardslist.append(OnePokerCard)

    if(NeedGhost == True):
        AllCardslist.append(Poker(98,'小王'))
        AllCardslist.append(Poker(99, '大王'))

    return AllCardslist


def shuffer(CardsList):
    CountCards = len(CardsList)
    for i in range(100):
        TempCard = CardsList[0]
        CardIndex = random.randint(0,CountCards - 1)
        CardsList[0] = CardsList[CardIndex]
        CardsList[CardIndex] = TempCard

    return CardsList

# 判断两张牌是否满足空当接龙条件的函数
def ifMashup(CardA,CardB):   #CardA往CardB下方接
    diff_dict = {'黑桃': 1, '红心': 2, '方块': 2, '梅花': 1}
    if(CardB == None):   #当接收牌为空时，必然能接上
        return True
    if((CardA.rank == CardB.rank - 1) and (diff_dict[CardA.suit] != diff_dict[CardB.suit])):
        # CardsList.append(OneCard)
        return True
    else:
        # print('无法将<--',OneCard,'-->放到该列牌后')
        return False

# for apoke in initPokerCards():
#     print('aaa:',apoke)
# 以字符串方式显示一组牌的函数
def ShowCardsList(CardsList):
    Str_CardsList = ''
    for ACard in CardsList:
        Str_CardsList = Str_CardsList + ACard.__str__() + ' '
    return Str_CardsList