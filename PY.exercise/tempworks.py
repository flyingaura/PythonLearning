# -*- coding: utf-8 -*-

import csv
infilepath = r'C:\Users\flyingaura\Desktop\111222.csv'
# outfilepath = r''

datalist = []
datadict = {}
astr = ''
with open(infilepath, mode = 'r', encoding= 'utf-8') as infile:
    for Aline in csv.reader(infile):
        if(Aline[1]):
            # datadict[Aline[0].strip()] = Aline[1].strip()
        #   astr = 'doc[\'%s\'] = doc[\'%s\'];' %(Aline[0].strip(),Aline[1].strip())
        # datalist.append(astr)
            astr = astr + 'trim(' + '`' + Aline[0] +'`' + ')' + ' as ' +Aline[1] + ' , '

# for astr in datadict:
#     print('%s:%s' %(astr,datadict[astr]))
print(astr)