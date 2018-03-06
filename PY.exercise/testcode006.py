#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

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

OptionList = 'ABCD'
TitleCount = 3
icount = 0
for AnAnswerList in all_answers(TitleCount, OptionList):
    print(AnAnswerList)
    icount += 1
print(icount)

