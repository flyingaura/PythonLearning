# -*- coding: utf-8 -*-

from collections import OrderedDict
import random
import json

TestDict = OrderedDict()

for i in range(5):
    Astr = ''
    for j in range(random.randint(1,5)):
        Astr = Astr + chr(random.randint(ord('A'),ord('z')))

    TestDict[Astr] = random.randint(0,100)

print(TestDict)
print(json.dumps(TestDict))

