# -*- coding: utf-8 -*-
'''
尝试编写一个空当接龙游戏
'''

from LearnModule import CardsGame
import random
from LearnModule import MY_math
from LearnModule import StringSplit

# 定义一个牌桌类，牌桌包含四个部分：游戏区GameArea、临时区TempArea、结果区ResultArea和操作提示区PromptArea,并定义牌桌显示方法
class PokerTable(object):
    def __init__(self,GamePokersList, TempPokersList, ResultPokersList, menu):    #GameVolumn表示游戏区分成几列，默认为8列
        self.GamePokersList = GamePokersList
        self.TempPokersList = TempPokersList
        self.ResultPokersList = ResultPokersList
        self.menu = menu

    # 找出GamePokers中最长那一列
    def findMaxColumn(self):
        Columnlenlist = [len(CardsList) for CardsList in self.GamePokersList]
        Columnlenlist.sort()
        return Columnlenlist[-1]

    # 显示当前牌桌的方法
    def ShowTable(self):
        print('=' * 64 + '||' + '=' * 64)
        print('临时区' + ' ' * 58 + '||' + '结果区')

        for apoker in self.TempPokersList:
            if(apoker == ''):
                print('|' + ' ' * 11 + '|', end='\t')
            else:
                print('|' + apoker.GameShow() + '|', end='\t')
        print('||', end='')
        for apoker in self.ResultPokersList:
            if (apoker == ''):
                print('|' + ' ' * 11 + '|', end='\t')
            else:
                print('|' + apoker.GameShow() + '|', end='\t')

        print('\n')
        print('=' * 64 + '||' + '=' * 64)
        print('游戏区')
        for i in range(len(self.GamePokersList)):
            print('|  第%2d 列  |' %(i + 1), end='\t')
        print('\n')

        for i in range(self.findMaxColumn()):
            for j in range(len(self.GamePokersList)):
                if(i < len(self.GamePokersList[j])):
                    if(self.GamePokersList[j][i] == ''):
                        print('|' + ' ' * 11 + '|', end='\t')
                    else:
                        print('|' + self.GamePokersList[j][i].GameShow()+ '|', end='\t')
                else:
                    print('|' + ' ' * 11 + '|', end='\t')
            print('\n')
        # for i in range(len(self.GamePokersList)):
        #     print('| 第%d列  |' %(i + 1), end='\t')
        # print('\n')
        print('=' * 64 + '||' + '=' * 64)
        print('游戏操作提示：')
        print(self.menu)

# 定义游戏牌初始化函数（重新洗出一幅完整的牌，并按游戏要求进行分组）
def initTableParameter():

    # 游戏牌初始化
    GamePokersList = []
    GameColumn = 8
    TotalPokers = CardsGame.shuffer(CardsGame.initPokerCards())
    # 进行全部扑克牌初始化分组
    grouplen = int(len(TotalPokers) / GameColumn)
    StartPostion = 0
    for i in range(GameColumn):
        CardsGroup = TotalPokers[StartPostion:StartPostion + grouplen]
        StartPostion = StartPostion + grouplen
        GamePokersList.append(CardsGroup[:])

    RestPokers = TotalPokers[StartPostion:]
    GroupIndex = list(MY_math.RandomFetch(GameColumn - 1, len(RestPokers)))
    # print(GroupIndex)
    for i in range(len(RestPokers)):
        GamePokersList[GroupIndex[i]].append(RestPokers[i])

    return GamePokersList

# 定义从游戏区往临时区移动的函数
def Game2Temp(GamePokersList,TempPokersList,num):

    try:
        num = int(num)
    except ValueError:
        print('输入操作指令错误，请输入正确的数字（%d - %d）' %(1,len(GamePokersList)))
        return False

    # SuccessTag = 1

    if(num < 1 or num > len(GamePokersList)):
        print('输入操作指令错误，请输入正确的数字（%d - %d）' % (1, len(GamePokersList)))
        return False

    try:
        moveposition = TempPokersList.index('')
    except ValueError:
        print('<-------------临时区已经没有位置可以放牌了------------->')
        # SuccessTag = 0
        return False

    # if(SuccessTag):
    TempPokersList[moveposition] = GamePokersList[num - 1][-1]
    GamePokersList[num - 1].pop(-1)
    print('<-------------%s已成功移至临时区------------->' %(TempPokersList[moveposition].__str__()))

    return True

# # 定义一个判断两张牌是否满足空当接龙条件的函数
# def ifMashup(PokerA,PokerB):
#     if(PokerA.suit)
# 定义一个从临时区往游戏区移动的函数（必须符合空当接龙的条件才能移动）
def Temp2Game(TempPokersList,GamePokersList,TempPosition,GameColumn):
    try:
        TempPosition = int(TempPosition)
    except ValueError:
        print('输入操作指令错误，请输入正确的数字（%d - %d）' % (1, 4))
        return False
    try:
        GameColumn = int(GameColumn)
    except ValueError:
        print('输入操作指令错误，请输入正确的数字（%d - %d）' % (1, len(GamePokersList)))
        return False

    if(TempPosition < 1 or TempPosition > 4 ):
        print('输入操作指令错误，请输入正确的数字（%d - %d）' % (1, 4))
    elif(GameColumn < 1 or GameColumn > len(GamePokersList)):
        print('输入操作指令错误，请输入正确的数字（%d - %d）' % (1, len(GamePokersList)))
    else:
        if(GamePokersList[GameColumn - 1] == []):
            TargetPoker = None
        else:
            TargetPoker = GamePokersList[GameColumn - 1][-1]
        if(CardsGame.ifMashup(TempPokersList[TempPosition - 1],TargetPoker)):
            GamePokersList[GameColumn - 1].append(TempPokersList[TempPosition - 1])
            TempPokersList[TempPosition - 1] = ''
            print('<-------------%s已成功移至游戏区第 %d 列牌------------->' %(GamePokersList[GameColumn - 1][-1].__str__(), GameColumn))
            return True
        else:
            print('<-------------无法将%s放到游戏区第 %d 列牌后------------->' %(TempPokersList[TempPosition - 1].__str__(), GameColumn))

    return False

# 定义一个从游戏区移到结果区的函数(必须从一个花色的A开始从小到大顺序移动过去）
def Game2Result(GamePokersList,ResultPokersList,GameColumn):
    try:
        GameColumn = int(GameColumn)
    except ValueError:
        print('输入操作指令错误，请输入正确的数字（%d - %d）' % (1, len(GamePokersList)))
        return False

    if(GameColumn < 1 or GameColumn > len(GamePokersList)):
        print('输入操作指令错误，请输入正确的数字（%d - %d）' % (1, len(GamePokersList)))
        return False

    SuccessTag = 0

    if(GamePokersList[GameColumn - 1][-1].rank == 1):
        moveposition = ResultPokersList.index('')
        ResultPokersList[moveposition] = GamePokersList[GameColumn - 1][-1]
        GamePokersList[GameColumn - 1].pop(-1)
        print('<-------------游戏区第 %d 列的%s已成功移至结果区第 %d 列------------->'
              % (GameColumn, ResultPokersList[moveposition].__str__(), moveposition + 1))
        SuccessTag = 1
    else:
        for i in range(len(ResultPokersList)):
            if(ResultPokersList[i] == ''):
                break
            if(ResultPokersList[i].suit == GamePokersList[GameColumn - 1][-1].suit and ResultPokersList[i].rank == GamePokersList[GameColumn - 1][-1].rank - 1):
                ResultPokersList[i] = GamePokersList[GameColumn - 1][-1]
                GamePokersList[GameColumn - 1].pop(-1)
                print('<-------------游戏区第 %d 列的%s已成功移至结果区第 %d 列------------->'
                      %(GameColumn, ResultPokersList[i].__str__(), i + 1))
                SuccessTag = 1
                break

    if(SuccessTag):
        return True
    else:
        print('<-------------无法将%s放到结果区------------->' %(GamePokersList[GameColumn - 1][-1].__str__()))
        return False

# 定义一个从临时区移到结果区的函数(必须从一个花色的A开始从小到大顺序移动过去）
def Temp2Result(TempPokersList,ResultPokersList,CardPosition):
    try:
        CardPosition = int(CardPosition)
    except ValueError:
        print('输入操作指令错误，请输入正确的数字（%d - %d）' % (1, len(TempPokersList)))
        return False

    if(CardPosition < 1 or CardPosition > len(TempPokersList)):
        print('输入操作指令错误，请输入正确的数字（%d - %d）' % (1, len(TempPokersList)))
        return False

    SuccessTag = 0

    if(TempPokersList[CardPosition - 1].rank == 1):
        moveposition = ResultPokersList.index('')
        ResultPokersList[moveposition] = TempPokersList[CardPosition - 1]
        TempPokersList[CardPosition - 1] = ''
        print('<-------------临时区第 %d 列的%s已成功移至结果区第 %d 列------------->'
              % (CardPosition, ResultPokersList[moveposition].__str__(), moveposition + 1))
        SuccessTag = 1
    else:
        for i in range(len(ResultPokersList)):
            if(ResultPokersList[i] == ''):
                break
            if(ResultPokersList[i].suit == TempPokersList[CardPosition - 1].suit and ResultPokersList[i].rank == TempPokersList[CardPosition - 1].rank - 1):
                ResultPokersList[i] = TempPokersList[CardPosition - 1]
                TempPokersList[CardPosition - 1] = ''
                print('<-------------临时区第 %d 列的%s已成功移至结果区第 %d 列------------->'
                      %(CardPosition, ResultPokersList[i].__str__(), i + 1))
                SuccessTag = 1
                break

    if(SuccessTag):
        return True
    else:
        print('<-------------无法将%s放到结果区------------->' %(TempPokersList[CardPosition - 1].__str__()))
        return False

# 定义一个从一组牌中最出满足空当接龙条件的最长可用牌组的函数
def MaxValidCards(PokersList):
    if(PokersList == []):
        return PokersList
    i = len(PokersList) - 1
    if(i == 0):
        return PokersList
    else:
        while(i > 0):
            if(CardsGame.ifMashup(PokersList[i],PokersList[i - 1])):
                i -= 1
            else:
                break
        return PokersList[i:]

# 定义一个判断最大可以移动的牌数的函数
def MaxMoveNum(GamePokersList, TempPokersList):
    MaxNum = 1
    for APokersList in GamePokersList:
        if (APokersList == []):
            MaxNum = MaxNum + 2

    for APoker in TempPokersList:
        if (APoker == ''):
            MaxNum = MaxNum + 1

    return MaxNum

# 定义一个从游戏区A列往游戏区B列往动的函数
# 满足以下条件：
# 1、必须符合空当接龙的条件才能移动，即从大到小依次排序且花色红黑相间
# 2、可以移动一张或一组牌，移动的这组牌必须自身满足空当接龙条件
# 3、移动一组牌的数量按照规则有限制，限制规则参看 MaxMoveNum 函数


def Game2Game(GamePokersList,TempPokersList,SPosition,TPosition,MoveCount = 1):
    try:
        SPosition = int(SPosition)
        TPosition = int(TPosition)
    except ValueError:
        print('输入操作指令错误，请输入正确的数字（%d - %d）' % (1, len(GamePokersList)))
        return False
    try:
        MoveCount = int(MoveCount)
    except ValueError:
        print('输入操作指令错误，移动组牌数量参数必须为数字或不输入')
        return False

    if (SPosition == TPosition):
        print('输入操作指令错误，移动牌时起点和终点不允许是同一列牌')
        return False

    if (SPosition < 1 or SPosition > len(GamePokersList) or TPosition < 1 or TPosition > len(GamePokersList)):
        print('输入操作指令错误，请输入正确的数字（%d - %d）' % (1, len(GamePokersList)))
        return False

    if(GamePokersList[SPosition - 1] == []):
        print('输入操作指令错误，所要移动牌列为空，无法移动！')
        return False

    if(GamePokersList[TPosition - 1] == []):   #所移目标列牌为空时，必然能移动
        TargetPoker = None
    else:
        TargetPoker = GamePokersList[TPosition - 1][-1]


    if(MoveCount == 1):
        if(CardsGame.ifMashup(GamePokersList[SPosition - 1][-1],TargetPoker)):
            GamePokersList[TPosition - 1].append(GamePokersList[SPosition - 1][-1])
            GamePokersList[SPosition - 1].pop(-1)
            print('<-------------游戏区第 %d 列的%s已成功移至结果区第 %d 列------------->'
                  % (SPosition, GamePokersList[TPosition - 1][-1].__str__(), TPosition))
            return True
        else:
            print('<-------------错误！不符合空当接龙条件，游戏区第 %d 列的%s无法移至结果区第 %d 列------------->'
                  % (SPosition, GamePokersList[SPosition - 1][-1].__str__(), TPosition))
            return False

    else:
        MaxValidPokers = MaxValidCards(GamePokersList[SPosition - 1])  #调用取最长可用牌组的函数，取出源牌组中符合空当接龙的最长牌组
        CountList = [MoveCount,len(MaxValidPokers),MaxMoveNum(GamePokersList,TempPokersList)]
        CountList.sort()     #取三者的最小值做为所能移动的牌组数

        MovePokersList = MaxValidPokers[(len(MaxValidPokers) - CountList[0]):]

        if(CardsGame.ifMashup(MovePokersList[0],TargetPoker)):
            GamePokersList[TPosition - 1].extend(MovePokersList)
            GamePokersList[SPosition - 1] = GamePokersList[SPosition - 1][:(len(GamePokersList[SPosition - 1]) - len(MovePokersList))]
            print('<-------------游戏区第 %d 列的%s已成功移至结果区第 %d 列------------->'
              % (SPosition, CardsGame.ShowCardsList(MovePokersList), TPosition))
            return True
        else:
            print('<-------------错误！不符合空当接龙条件，游戏区第 %d 列的%s无法移至结果区第 %d 列------------->'
                  % (SPosition, CardsGame.ShowCardsList(MovePokersList), TPosition))
            return False


# 定义一个判断游戏胜利的函数
def ifVictory(GamePokersList):
    for Alist in GamePokersList:
        if(Alist != []):
            return False
    return True

# <=============主程序开始=============>
# 开始进行游戏，移动牌面直到胜利或放弃退出
# 调用牌桌初始化参数函数
print('命令行版空当接龙--游戏开始 ！')
 # 传入初始化参数，进行牌桌初始化
menutext = ' ' * 2 + '1.输入1（列号A，列号B,牌数N），表示将游戏区A列最下面的一组牌N张移动到游戏区B列最下面，N不输则为1张　\n' + \
           ' ' * 2 + '2.输入2（列号A），表示将游戏区A列最下面的一张牌移动到临时区空位置处　\n' + \
           ' ' * 2 + '3.输入3（列号A，列号B），表示从临时区将第A列牌移动到游戏区第B列最下面　\n' + \
           ' ' * 2 + '4.输入4（列号A），表示将游戏区A列最下面的一张牌移动到结果区对应位置处　\n' + \
           ' ' * 2 + '5.输入5（列号A），表示将临时区A列最下面的一张牌移动到结果区对应位置处　\n' + \
           ' ' * 2 + '6.输入R，重新进行一局游戏　\n' + \
           ' ' * 2 + '7.输入Q，退出游戏　\n'

CurrentTable = PokerTable(initTableParameter(),[''] * 4, [''] * 4,menutext)
CurrentTable.ShowTable()

while (not ifVictory(CurrentTable.GamePokersList)):
    GameOperating = input('请按上述菜单输入操作指令')

    if(GameOperating.lower() == 'q'):
        print('游戏结束 ! ')
        break
    elif(GameOperating.lower() == 'r'):
        print('开始一局新游戏 ！')
        CurrentTable = PokerTable(initTableParameter(), [''] * 4, [''] * 4, menutext)
        CurrentTable.ShowTable()
    else:
        Operation = StringSplit.stringsplit(GameOperating,('(',')',','))
        # print(Operation)
        if(Operation[0] == '1'):   #输入1（列号A，列号B,牌数N），表示将游戏区A列最下面的一组牌N张移动到游戏区B列最下面，N不输则为1张
            ExcuteTag = 1
            if(len(Operation) == 3):
                MoveCount = 1
            elif(len(Operation) == 4):
                MoveCount = Operation[3]
            else:
                print('请按上述菜单要求输入正确的操作指令')
                ExcuteTag = 0

            if(ExcuteTag):
                if(Game2Game(CurrentTable.GamePokersList,CurrentTable.TempPokersList,Operation[1],Operation[2],MoveCount)):
                    CurrentTable.ShowTable()

        elif(Operation[0] == '2'):   #输入2（列号A），表示将游戏区A列最下面的一张牌移动到临时区空位置处
            if(len(Operation) == 2):
                if(Game2Temp(CurrentTable.GamePokersList,CurrentTable.TempPokersList,Operation[1])):
                    # CurrentTable = PokerTable(CurrentTable.GamePokersList,CurrentTable.TempPokersList,CurrentTable.ResultPokersList,menutext)
                    CurrentTable.ShowTable()
            else:
                print('请按上述菜单要求输入正确的操作指令')

        elif (Operation[0] == '3'):  # 输入3（列号A，列号B），表示从临时区将第A列牌移动到游戏区第B列最下面
            if (len(Operation) == 3):
                if (Temp2Game(CurrentTable.TempPokersList, CurrentTable.GamePokersList, Operation[1], Operation[2])):
                    CurrentTable.ShowTable()
            else:
                print('请按上述菜单要求输入正确的操作指令')

        elif(Operation[0] == '4'):  #输入4（列号A），表示将游戏区A列最下面的一张牌移动到结果区对应位置处
            if (len(Operation) == 2):
                if (Game2Result(CurrentTable.GamePokersList, CurrentTable.ResultPokersList, Operation[1])):
                    CurrentTable.ShowTable()
            else:
                print('请按上述菜单要求输入正确的操作指令')

        elif(Operation[0] == '5'):   #输入5（列号A），表示将临时区A列最下面的一张牌移动到结果区对应位置处
            if (len(Operation) == 2):
                if (Temp2Result(CurrentTable.TempPokersList, CurrentTable.ResultPokersList, Operation[1])):
                    CurrentTable.ShowTable()
            else:
                print('请按上述菜单要求输入正确的操作指令')
        else:
            print('请按上述菜单要求输入正确的操作指令')

print('你赢了，游戏结束')
# 游戏初始化
