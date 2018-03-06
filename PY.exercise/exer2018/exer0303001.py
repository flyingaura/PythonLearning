#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

# 学习70个numpy－分组练习

import numpy as np
import random

# arr = np.arange(12)
# a = np.arange(12).reshape(3,-1)
# b = np.arange(12).reshape(3,-1)
# b[b % 2 == 1] = -1
#
# # arr_union = np.concatenate([a.reshape(2,-1),b.reshape(2,-1)],axis=0)
# # arr_union = np.vstack([a,b])
# # arr_union = np.c_[a,b]
# # arr_union = np.hstack([a,b])
# arr_union = np.concatenate([a,b], axis=1)
# # arr = np.full((3,3),1,dtype=bool)
# # arr = np.array(list(range(10)))
# # arr[arr % 2 == 1] = 2.81
# # print(np.where(arr % 2 == 1, -1 , arr))
# print(arr_union)
# out = arr.reshape(6, 2)
# print(arr)
# print(out)
#
# a = np.array([x for x in 'abcde'])
# arr = np.c_[np.repeat(a, 3), np.tile(a, 3)]
# print(arr)

def maxx(x, y):
    if(x > y):
        return x
    else:
        return y

a = np.array([random.randint(0, 20) for x in range(6)])
b = np.array([random.randint(0, 20) for x in range(6)])
print(a)
# print(np.intersect1d(a, b))
# print(np.setdiff1d(a, b))
# print(np.setdiff1d(b, a))
# while(len(np.where(a == b)[0]) < 3):
#     b = np.array([random.randint(0, 20) for x in range(6)])

print(b)
# AArrIndex = np.where((a>=5) & (a<=10))
# BArrIndex = np.where(np.logical_and(b>=10, b<=20))
# print(AArrIndex)
# print(a[AArrIndex])
# print(b[BArrIndex])
ListResult = []
for i in range(len(a)):
    ListResult.append(maxx(a[i], b[i]))

# print(ListResult)
print(np.array(ListResult))
print(np.vectorize(maxx,otypes=[int])(a, b))
# print(a[0],a[[0,1,2]])
