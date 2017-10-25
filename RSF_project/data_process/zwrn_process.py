# -*- coding: utf-8 -*-

infilepath = r'F:\documents\python\learning2017\RSF_project\data\政务人名词表1024.txt'
outfilepath = r'F:\documents\python\learning2017\RSF_project\data\政务人名词表1024_P.txt'

ZWRNData = []
with open(infilepath, mode = 'r', encoding= 'utf-8') as infile:
    for Aline in infile.readlines():
        Adata = Aline.strip().split('\t')
        NewStr = ''
        for Astr in Adata[0]:
            if(Astr != '　'):
                NewStr = NewStr + Astr
            else:
                print(Adata)

        Adata[0] = NewStr
        ZWRNData.append(Adata)
print(len(ZWRNData))

with open(outfilepath,mode = 'w', encoding= 'utf-8') as outfile:

    for Adata in ZWRNData:
        outfile.write('%s\t%s\t%s' %(Adata[0],Adata[1],Adata[2]))
        outfile.write('\n')

