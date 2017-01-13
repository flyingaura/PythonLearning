# -*- coding: utf-8 -*-

from LearnModule import Func_StringSplit
fline_split = []
with open('C:/Users/flyingaura/Desktop/ZT_classNO.txt','rb') as init_file:
    for fline in init_file.readlines():
        fline_decode = fline.decode('utf-8')
        # print(fline_decode)
        if(fline_decode.strip() != ''):
            fline_split.append(Func_StringSplit.stringsplit(fline_decode.strip(),'\t'))
fline_split.pop(0)
    # print(list(fline_split))
    # print(len(fline_split))
NoName = {}
NNlist = []
for fkey in fline_split:
    no_temp = Func_StringSplit.stringsplit(fkey[0],';')
    name_temp = Func_StringSplit.stringsplit(fkey[1],';')
    for i in range(len(no_temp)):
        if(i < len(name_temp)):
            NoName[no_temp[i]] = name_temp[i]
        else:
            NoName[no_temp[i]] = ''
        NNlist.append({no_temp[i]:NoName[no_temp[i]]})
print('=========drop similar : %d =========' % len(NoName))
# print(list(NoName))
print('=========all : %d =========' % len(NNlist))
# print(list(NNlist))
similarkey = []
for i in range(len(NNlist)):
    for j in range(i+1,len(NNlist)):
        if(list(NNlist[i].keys()) == list(NNlist[j].keys())):
            similarkey.append(NNlist[i])
            break

print(len(similarkey))
print(list(similarkey))





