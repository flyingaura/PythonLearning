#! /usr/local/bin/python3
# -*- coding: utf-8 -*-
'''
定义一个程序，用来解答一张中国警察考的刑侦科试题。
具体试题内容见“/Users/flyingauraMac/PycharmProjects/PythonLearning/PY.exercise/data/刑侦考试题.jpeg”
'''

import time

# 定义一个组合函数，用来生成所有可能的答案组合
def all_answers(TitleCount,AnsList):
    AnswersCollection = []
    try:
        AnsCount = len(AnsList)
    except TypeError :
        raise TypeError('第二个参数类型错误，必须为字符串、列表或元组类型！')
    if(not isinstance(TitleCount, int)):
        raise TypeError('第一个参数类型错误，必须为整数！')
    if(TitleCount == 1):
        for i in range(AnsCount):
            AnswersCollection.append({'title' + str(TitleCount): AnsList[i]})
        return AnswersCollection
    elif(TitleCount > 1):
        for AnAnswerGroup in all_answers(TitleCount - 1, AnsList):
            for i in range(AnsCount):
                AnAnswerGroup['title' + str(TitleCount)] = AnsList[i]
                AnswersCollection.append(AnAnswerGroup.copy())
        return AnswersCollection
    else:
        raise ValueError('第一个参数值域错误，必须为>1的正整数！')

# 定义一个对答案中字母出现次数的排序函数
def sort_answer_count(AnswerList):
    LetterNum = {}
    for Avalue in AnswerList.values():
        if(Avalue not in LetterNum.keys()):
            LetterNum[Avalue] = 0
        else:
            LetterNum[Avalue] = LetterNum[Avalue] + 1
    return sorted(LetterNum.items(),key=lambda d:d[1])

# 下面是判断每道题的答案是否正确

def if_title1_right(AnswerList):
    #title1:这道题的答案是：A.A  B.B C.C D.D
    return True

def if_title2_right(AnswerList):
    #title2:第5题的答案是：A.C  B.D  C.A  D.B
    option = {'A':'C', 'B':'D', 'C':'A', 'D':'B'}
    if(option[AnswerList['title2']] == AnswerList['title5']):
        return True
    else:
        return False

def if_title3_right(AnswerList):
    #title3:以下选项中哪一题的答案与其他三项不同：A.第3题 B.第6题 C.第2题 D.第4题
    option = {'A':3,'B':6,'C':2, 'D':4}
    for Aletter in 'ABCD':
        if(Aletter != AnswerList['title3']):
            if(AnswerList['title' + str(option[Aletter])] == AnswerList['title' + str(option[AnswerList['title3']])]):
                return False
    return True

def if_title4_right(AnswerList):
    #title4:以下选项中哪两题的答案相同：A.第1，5题  B.第2，7题  C.第1，9题  D.第6，10题
    option = {'A':[1,5], 'B':[2,7], 'C':[1,9], 'D':[6,10]}
    if(AnswerList['title' + str(option[AnswerList['title4']][0])] == AnswerList['title' + str(option[AnswerList['title4']][1])]):
        return True
    else:
        return False

def if_title5_right(AnswerList):
    #title5:以下选项中哪一题的答案与本题相同：A.第8题  B.第4题  C.第9题  D.第7题
    option = {'A':8, 'B':4, 'C':9, 'D':7}
    if(AnswerList['title5'] == AnswerList['title' + str(option[AnswerList['title5']])]):
        return True
    else:
        return False

def if_title6_right(AnswerList):
    #title6:以下选项中哪两题的答案与第8题相同：A.第2，4题  B.第1，6题  C.第3，10题  D.第5，9题
    option = {'A':[2,4], 'B':[1,6], 'C':[3,10], 'D':[5,9]}
    if(AnswerList['title' + str(option[AnswerList['title6']][0])] == AnswerList['title' + str(option[AnswerList['title6']][1])] and
       AnswerList['title' + str(option[AnswerList['title6']][0])] == AnswerList['title8']):
        return True
    else:
        return False

def if_title7_right(AnswerList):
    #title7:在此十道题中，被选中次数最少的选项字母为：A.C  B.B  C.A  D.D
    SortedAnsList = sort_answer_count(AnswerList)
    if(len(SortedAnsList) < 4):
        for Aletter in 'DCBA':
            ExistTag = 0
            for Acouple in SortedAnsList:
                if(Aletter == Acouple[0]):
                    ExistTag = 1
                    break
            if(not ExistTag):
                SortedAnsList.insert(0,(Aletter,0))

    option = {'A':'C', 'B':'B', 'C':'A', 'D':'D'}
    if(option[AnswerList['title7']] == SortedAnsList[0][0]):
        return True
    else:
        return False

def if_title8_right(AnswerList):
    #title8:以下选项中哪一题的答案与第1题的答案在字母中不相邻：A.第7题  B.第5题  C.第2题  D.第10题
    option = {'A':7, 'B':5, 'C':2, 'D':10}
    if(abs(ord(AnswerList['title' + str(option[AnswerList['title8']])]) - ord(AnswerList['title1'])) == 1):
        return False
    else:
        return True

def if_title9_right(AnswerList):
    #title9:已知“第1题与第6题的答案相同”与“第X题与第5题的答案相同”的真假性相反，那么X为：A.第6题  B.第10题  C.第2题  D.第9题
    option = {'A':6, 'B':10, 'C':2, 'D':9}
    if(AnswerList['title1'] == AnswerList['title6']):
        condition1 = True
    else:
        condition1 = False

    if(AnswerList['title' + str(option[AnswerList['title9']])] == AnswerList['title5']):
        condition2 = True
    else:
        condition2 = False

    if((condition1 and not condition2) or (not condition1 and condition2)):
        return True
    else:
        return False

def if_title10_right(AnswerList):
    #title10:在此10道题中，ABCD四个字母出现次数最多与最少者的差为：A.3  B.2  C.4  D.1
    option = {'A':3, 'B':2, 'C':4, 'D':1}
    SortedAnsList = sort_answer_count(AnswerList)
    GapValue = SortedAnsList[-1][1] - SortedAnsList[0][1]
    if(option[AnswerList['title10']] == GapValue):
        return True
    else:
        return False

# 下面是解题的主程序（10道题，10种判断条件）
print('-------->  开始答题')
starttime = time.time()
icount = 1
TitlesCount = 10
for AnAnswerGroup in all_answers(TitlesCount,'ABCD'):
    if(icount % 1000 == 1):
        print('--------> 已执行 %d 次运算' %(icount-1))
    RightTag = 1
    for i in range(TitlesCount):
        if(not eval('if_title%d_right(AnAnswerGroup)' % (i + 1))):
            RightTag = 0
            break

    if(RightTag):
        break

    icount += 1
endtime = time.time()
if(RightTag):
    print('-------->   完成答题，运行 %d 步运算，耗时 %d 秒, 正确答案为：' %(icount, endtime - starttime))
    print(AnAnswerGroup)
else:
    print('-------->  完成全部 %d 次运算，耗时 %d 秒, T_T，真奇怪，居然没有正确答案！' %(icount - 1, endtime - starttime))





