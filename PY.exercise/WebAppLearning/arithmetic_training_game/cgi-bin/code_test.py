# -*- coding: utf-8 -*-

import json

with open('../data/ExamRecords.json', mode= 'r', encoding='utf-8') as jsonfile:
    testJson = json.loads(jsonfile.read().strip())
    for Akey in testJson:
        print('%s:' %Akey)
        for Bkey in testJson[Akey]:
            print('%s:' %Bkey, end = '')
            print(testJson[Akey][Bkey])