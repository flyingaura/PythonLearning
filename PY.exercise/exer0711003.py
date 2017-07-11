# -*- coding: utf-8 -*-

"""
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，
请编程序找出三队赛手的名单。
"""

from LearnModule import MY_math
#  定义一个从两个序列中进行1对1配对的所有可能函数。两个序列长度可以不一样。
def matchPlays(Alist,Blist):

    matchResult = []
    OneMatchPlayers = {}
    # 定义退出条件：
    if(len(Alist) == 1):
        for Bone in Blist:
            OneMatchPlayers[Alist[0]] = Bone
            OneMatchTemp = OneMatchPlayers.copy()
            matchResult.append(OneMatchTemp)
        return matchResult

    if(len(Blist) == 1):
        for Aone in Alist:
            OneMatchPlayers[Aone] = Blist[0]
            OneMatchTemp = OneMatchPlayers.copy()
            matchResult.append(OneMatchTemp)
        return matchResult
    # ===递归计算所有可能情况===
    for i in range(len(Blist)):
        OneMatchPlayers[Alist[0]] = Blist[i]
        # matchResult.append({Alist[0]:Blist[i]})
        templist = Blist.copy()
        templist.pop(i)
        for APlayMatch in matchPlays(Alist[1:],templist):
            for key in APlayMatch:
                OneMatchPlayers[key] = APlayMatch[key]
            OneMatchTemp = OneMatchPlayers.copy()
            matchResult.append(OneMatchTemp)

    return matchResult

Ateam = [x for x in 'abc']
Bteam = [x for x in 'xyz']

# print(Ateam)
# print(Bteam)
# 输出所有配对

AllMatchResult = matchPlays(Ateam,Bteam)
print('所有配对情况为 %d 种：' %len(AllMatchResult))
print(AllMatchResult)

# AllArrayResult = MY_math.array_in_list(Bteam,3)
# print('所有排列情况为 %d 种：' %len(AllArrayResult))
# print(AllArrayResult)

# 根据题目要求输出配对结果-- a说他不和x比，c说他不和x,z比
SpecialMatch = []
for oneMatch in AllMatchResult:
    if(oneMatch['a'] != 'x' and oneMatch['c'] != 'x' and oneMatch['c'] != 'z'):
        SpecialMatch.append(oneMatch)

print('题目要求的配对结果数为%d' %(len(SpecialMatch)))
print(SpecialMatch)