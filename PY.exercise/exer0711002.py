# -*- coding: utf-8 -*-

"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

"""

def halfValue(N):
    try:
        N = abs(float(N))
    except ValueError as e:
        raise ValueError('%s ---> 参数错误，输入必须为整数' %e)

    return N / 2

initDistance = 100
initCount = 10
SumDistance = initDistance

for i in range(1,initCount):
    initDistance = halfValue(initDistance)
    SumDistance = SumDistance + 2 * initDistance


print('反弹10次的总距离为： %3f' %SumDistance)
print('第10次反弹的高度为： %3f' %halfValue(initDistance))