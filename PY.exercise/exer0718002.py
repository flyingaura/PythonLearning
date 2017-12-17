# -*- coding: utf-8 -*-
from collections import OrderedDict
import random
import json

d = OrderedDict()
# d = {}
# for key,value in {'a':1,'b':4,'c':6,'d':2}.items():
#     d[key] = value
for key in range(10):
    d[chr(ord('a') + key)] = random.randint(1,10)

print(json.dumps(d))
# print(sorted(d.items(),key = lambda s:s[1]))
