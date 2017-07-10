# -*- coding: utf-8 -*-

import math

def ReturnAdevNum(N):
    try:
        N = int(N)
    except ValueError as e:
        raise ValueError('%e ---> 参数错误，输入参数必须同为正整数')

    if(N <= 0):
        raise ValueError('参数错误，输入参数必须同为正整数')

    for i in range(2,int(math.sqrt(N))+1):
        if(N % i == 0):
            return i
    return N

def devisionNum(N):
    try:
        N = int(N)
    except ValueError as e:
        raise ValueError('%e ---> 参数错误，输入参数必须同为正整数')

    if(N <= 0):
        raise ValueError('参数错误，输入参数必须同为正整数')
    # if_tag = True
    devisionResult = []
    devideNum = N
    while(1):
        AdevNum = ReturnAdevNum(devideNum)
        devisionResult.append(AdevNum)
        if(AdevNum == devideNum):
            return devisionResult
        else:
            devideNum = devideNum / AdevNum
    # for i in range(2,int(math.sqrt(N))+1):
    #     if(N % i == 0):
    #         devisionResult.append(i)
    #         if_tag = False
    #         devisionNum(N / i)
    # if(if_tag):
    #     devisionResult.append(N)

    return devisionResult

while(1):
    initNum = input('请输入任意正整数（q退出）：')
    if(initNum.lower() == 'q'):
        print('Program END !')
        break
    devNumList = devisionNum(int(initNum))
    if(len(devNumList) == 1):
        print('%d = %d' %(int(initNum),devNumList[0]))
    else:
        print('%d = %s' %(int(initNum),'*'.join([str(x) for x in devNumList])))


