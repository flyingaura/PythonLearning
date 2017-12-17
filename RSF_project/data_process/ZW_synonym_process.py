# -*- coding: utf-8 -*-

import csv

infilepath = r'F:\documents\python\learning2017\RSF_project\data_process\国务院组织机构 2017.10.24.csv'
outfilepath = r'F:\documents\python\learning2017\RSF_project\data\国务院组织机构同义词表1027.txt'

synonym_datalist = []
with open(infilepath, mode = 'r', encoding= 'utf-8') as infile:
    infile.readline()
    # i = 0
    for Adata in csv.reader(infile):
        linestr = ''
        for aword in Adata[:3]:
            for bword in aword.split(';'):
                linestr = linestr + bword.strip() + '\t'
        synonym_datalist.append(linestr)
        # if(Adata[3]):
        #     if(Adata[2] in synonym_datalist.keys() and synonym_datalist[Adata[2]] != Adata[3]):
        #         i += 1
        #         print(Adata[2],synonym_datalist[Adata[2]],Adata[3])
        #         synonym_datalist[Adata[2]] = synonym_datalist[Adata[2]] + '\t' + Adata[3]
        #     else:
        #         synonym_datalist[Adata[2]] = Adata[3]

print(len(synonym_datalist))
# print(i)

with open(outfilepath, mode = 'w', encoding= 'utf-8') as outfile:

    for Aword in synonym_datalist:
        outfile.write('%s' %(Aword))
        outfile.write('\n')

        # if(i < 20):
        #     print(Adata)
        #     i += 1
        # else:
        #     break