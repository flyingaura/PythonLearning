# # -*- coding: utf-8 -*-
#
# # L1 = [1,3,5]
# # L2 = [2,4,6,8,10]
# #
# # print(list(L1))
# # print(list(L2))
# #
# # L1 = L2
# # print(list(L1))
#
# # print(list(range(2)))
# #
# # for x in range(0):
# #     print(x)
#
# alist = [1,2,3,4,5,6,7]
# print(alist[1:1])
#
# print(int(len(alist)/2))
#
# SH_CN = {'鼠':'shu','牛':'niu','虎':'hu', '兔':'tu', '龙':'long', '蛇':'she', '马':'ma', '羊':'yang', '猴':'hou', '鸡':'ji', '狗':'gou', '猪':'zhu'}
# #
# for key in SH_CN.items():
#     print(key)

# print(list(SH_CN.items()))
from enum import Enum,unique
import time
shenxiao = Enum('生肖',('鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪'))


print(shenxiao['猴'].value)

n = 2011
one_sh = shenxiao((n+8)%12+1)
for key in shenxiao.__members__:
    print(key)
print(one_sh.name ,'==>',one_sh.value)
print(list(shenxiao.__members__))
print(shenxiao((n+8)%12+1).name)