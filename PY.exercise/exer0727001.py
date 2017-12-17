# -*- coding: utf-8 -*-

import random

# 自己定义一个简单的列表排序方法Lsorted(list)

# 先定义一个堆排列函数（列表的第一个一定是最小（或最大）的值）
def heaplist(Nlist,reversed = False):
    if(not reversed):    #第一位最小值
        Ntemp = Nlist[0]
        for i in range(len(Nlist)):
            if(Ntemp > Nlist[i]):
                Nlist[0] = Nlist[i]
                Nlist[i] = Ntemp
                Ntemp = Nlist[0]
    else:
        Ntemp = Nlist[0]
        for i in range(len(Nlist)):
            if (Ntemp < Nlist[i]):
                Nlist[0] = Nlist[i]
                Nlist[i] = Ntemp
                Ntemp = Nlist[0]

    return None

def Lsorted(Nlist,sortedlistlen = None,reversed = False):
    SortedList = []
    if(sortedlistlen != None):
        while(sortedlistlen and Nlist):
            heaplist(Nlist, reversed = reversed)
            # print(Nlist)
            SortedList.append(Nlist[0])
            # print(SortedList)
            Nlist.pop(0)
            sortedlistlen -= 1
        return SortedList

    else:
        return Lsorted(Nlist, sortedlistlen = len(Nlist), reversed = reversed)




Alist = [random.randint(0,100) for i in range(10)]
print(Alist)
print(Lsorted(Alist,4))


