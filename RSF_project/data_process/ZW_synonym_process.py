# -*- coding: utf-8 -*-

import csv

infilepath = r'F:\documents\python\learning2017\RSF_project\data\电子政务及公文主题词表（包括同义词及上位词） 2017.10.24.csv'
outfilepath = r'F:\documents\python\learning2017\RSF_project\data\电子政务同义词表1024.txt'

synonym_datalist = {}
with open(infilepath, mode = 'r', encoding= 'utf-8') as infile:
    infile.readline()
    i = 0
    for Adata in csv.reader(infile):
        if(Adata[3]):
            if(Adata[2] in synonym_datalist.keys() and synonym_datalist[Adata[2]] != Adata[3]):
                i += 1
                print(Adata[2],synonym_datalist[Adata[2]],Adata[3])
                synonym_datalist[Adata[2]] = synonym_datalist[Adata[2]] + '\t' + Adata[3]
            else:
                synonym_datalist[Adata[2]] = Adata[3]

print(len(synonym_datalist))
print(i)

with open(outfilepath, mode = 'w', encoding= 'utf-8') as outfile:

    for key in synonym_datalist:
        outfile.write('%s\t%s' %(key,synonym_datalist[key]))
        outfile.write('\n')

        # if(i < 20):
        #     print(Adata)
        #     i += 1
        # else:
        #     break