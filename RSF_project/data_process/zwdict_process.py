# -*- coding: utf-8 -*-
outfilepath = r'F:\documents\python\learning2017\RSF_project\data\“十九大”政务新词词表（导入用）.txt'

infilepath = r'F:\documents\python\learning2017\RSF_project\data\“十九大”政务新词词表.txt'

WordDict = []
NeedProWord= []
# OneWordList = []
# DupWordList = []

with open(infilepath, mode = 'r', encoding= 'utf-8') as infile:
    for aline in infile.readlines():
        Aword = aline.strip()
        if(Aword[0] == '“' and Aword[-1] == '”'):
            NeedProWord.append(Aword)
            Aword = Aword[1:-1]
        WordDict.append(Aword)

        # if(len(Aword) == 1):
        #     OneWordList.append(Aword)
        # elif(Aword not in WordDict):
        #     WordDict.append(Aword)
        # else:
        #     DupWordList.append(Aword)
# print('========== 单个字的词个数：%d ===========' % len(OneWordList))
# print('========== 重复词个数：%d ===========' % len(DupWordList))
# print('========== 有效词个数：%d ===========' % len(WordDict))
for word in NeedProWord:
    print(word)
with open(outfilepath, mode = 'w', encoding= 'utf-8') as outfile:
    for Aword in WordDict:
        outfile.write(Aword + '\t' + 'dzzw' + '\t' + '1500' + '\n')
