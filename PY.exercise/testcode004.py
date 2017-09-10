# -*- coding: utf-8 -*-
import random

# alist = [random.sample(list(range(10)),3) for i in range(10)]
alist = []
bdict = {}
for i in range(10):
    bdict[str(i)] = random.sample(list(range(10)),3)
    # alist.append(blist)
print(bdict)

key0 = list(bdict.keys())[0]
print(key0)