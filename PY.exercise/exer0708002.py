# -*- coding: utf-8 -*-

def sumlists(listA,listB):
    if(len(listA) > len(listB)):
        Nlength = len(listB)
    else:
        Nlength = len(listA)
    return [listA[i] + listB[i] for i in range(Nlength)]

listA = [1,2,3,4,5]
listB = [3,4,5,6]

print(sumlists(listA,listB))