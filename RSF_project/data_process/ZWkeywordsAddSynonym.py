# -*- coding: utf-8 -*-

infilepath1 = r'F:\documents\python\learning2017\RSF_project\data\政务主题词表1024.txt'
# infilepath2 = r'F:\documents\python\learning2017\RSF_project\data\电子政务同义词表1024.txt'
infilepath2 = r'F:\documents\python\learning2017\RSF_project\data\国务院组织机构同义词表1027.txt'
outfilepath = r'F:\documents\python\learning2017\RSF_project\data\国务院组织机构补充词表1101.txt'

KeyWordList1 = set()
KeyWordList2 = set()
with open(infilepath1, mode = 'r', encoding= 'utf-8') as infile1:
    for Aword in infile1.readlines():
        KeyWordList1.add(Aword.strip().split('\t')[0])

with open(infilepath2, mode = 'r', encoding= 'utf-8') as infile2:
    for Aline in infile2.readlines():
        for Aword in Aline.strip().split('\t'):
            if(Aword):
                KeyWordList2.add(Aword)

DiffWords = KeyWordList2.difference(KeyWordList1)
# print(len(KeyWordList1))
# print(len(KeyWordList2))
print(len(DiffWords))
with open(outfilepath, mode = 'w', encoding= 'utf-8') as outfile:
    for Aword in DiffWords:
        outfile.write('%s\t%s\t%d' %(Aword.strip(),'zw',1000))
        outfile.write('\n')



