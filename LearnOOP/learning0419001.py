# -*- coding: utf-8 -*-

from LearnModule import StringSplit
from LearnModule import MY_math
import math
# from LearnModule import String_func
#
# origin_str = 'when you are thinking how to spend several hard-won lepta, when you are wondering whether new money'
# print(String_func.MY_replace(origin_str,'are','<-->',1))

# aset = set('abcde')
# bset = set('befjhtya')

# print(aset.intersection(bset))
# print(aset.union(bset))
# print(aset.difference(bset))
# print(aset.symmetric_difference(bset))
#
# aset.add('56')
# # print(aset)
#
# print(aset.remove('56'),aset)
#
alist = [x for x in range(6)]
# four_combined = set()
result_combined = []
for A_num in alist:
    for B_num in alist:
        for C_num in alist:
            for D_num in alist:
                four_combined = set([A_num,B_num,C_num,D_num])
                if(len(four_combined) == 4 and four_combined not in result_combined):
                    result_combined.append(four_combined)

for nlist in result_combined:
    print(nlist)
print(len(result_combined),MY_math.combination(len(alist),4))
# #
# aset = [set([1,2,3,4])]
# # bset = set([3,2,1,4])
#
# print({3,4,2,1} in aset)

