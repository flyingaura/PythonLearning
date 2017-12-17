# -*- coding: utf-8 -*-

# 构造一个扑克牌的类Card及其方法；构造一个扑克牌集合的类Deck及其方法

# 扑克牌类Card--> 花色suit:（黑桃:S,方块:D,红心:H,梅花:C）, 分值rank(1-13,代表A->K)
import random

class Card(object):

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    # 单张牌的输出表示
    def __str__(self):
        return '(%d,%s)' %(self.rank,self.suit)

    # 单张牌的标准输出表示（即1-->A,11-->J,12-->Q,13-->K）
    def standpre(self):
        standCard = {1:'A',11:'J',12:'Q',13:'K'}
        if(self.rank in standCard.keys()):
            print('(%s,%s)' %(standCard[self.rank],self.suit))
        else:
            print('(%s,%s)' %(str(self.rank),self.suit))


class Deck(Card):

    def __init__(self,CardsList = None):
        if (CardsList == None):
            self.DeckList = []
            for irank in range(1, 14):
                for isuit in 'SDHC':
                    Acard = Card(irank, isuit)
                    self.DeckList.append(Acard)
            for i in range(100):
                tempCard = self.DeckList[0]
                randIndex = random.randint(0, 51)
                self.DeckList[0] = self.DeckList[randIndex]
                self.DeckList[randIndex] = tempCard
        else:
            self.DeckList = CardsList

    def __str__(self):
        i = 1
        DeckStr = ''
        while(i < len(self.DeckList) + 1):
            if( i % 13 != 0):
                DeckStr = DeckStr + '(%d,%s)\t' %(self.DeckList[i - 1].rank,self.DeckList[i - 1].suit)
            else:
                DeckStr = DeckStr + '(%d,%s)\n' %(self.DeckList[i - 1].rank,self.DeckList[i - 1].suit)
            i += 1
        return DeckStr

    def shuffle(self):
        NumCards = len(self.DeckList)
        for i in range(100):
            tempCard = self.DeckList[0]
            randIndex = random.randint(0, NumCards-1)
            self.DeckList[0] = self.DeckList[randIndex]
            self.DeckList[randIndex] = tempCard
        return self.DeckList

    def fetch(self):
        return self.DeckList

    def deal(self):
        return self.DeckList.pop(random.randint(0,len(self.DeckList) - 1))


    def empty(self):
        if(len(self.DeckList) == 0):
            return True
        else:
            return False


# 初始化一局牌，得到全部牌的牌池
ADeckPool = Deck()
# print(ADeckPool)

# 按顺序初始化需要摆牌的7列牌，每列3张。只有最下面这一张显示，其他不显示。
Tableau = []
for i in range(7):
    FetchCards = []
    for j in range(3):
        FetchCards.append(ADeckPool.deal())
        FetchDeck = Deck(FetchCards)
    Tableau.append(FetchDeck)

# 把初始化的7列牌区域打印出来
for ADeck in Tableau:
    CardsList = ADeck.fetch()
    for ACards in CardsList[:-1]:
        print('(*,*)', end = '\t')
    print(CardsList[-1])

socket = ADeckPool
# print(socket)


# Acard = ADeck.deal()
# print(Acard)
# print('%s <--> %d' %(Acard.suit,Acard.rank))
