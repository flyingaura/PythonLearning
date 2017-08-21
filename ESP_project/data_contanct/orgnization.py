# -*- coding: utf-8 -*-
# 整理公司通讯录，生成完整的组织机构

from LearnModule import StringSplit

OrgList = []
with open('C:/Users/flyingaura/Desktop/公司通讯录数据（开发用）.dat', mode = 'rb') as outfile:
    for aline in outfile.readlines():
        aline_decode = aline.decode('utf-8')
        OrgList.append(StringSplit.stringsplit(aline_decode.strip(),'\t'))

# print(OrgList)
OrgNameList = []
OrgTemp = []
for unit in OrgList:
    if(unit == None):
        unit = []
    OrgName = ''
    if(len(unit) > 1):
        for alevel in unit:
            OrgName = OrgName + '\\' + alevel
        OrgNameList.append(OrgName)
        OrgTemp = unit[:-1]
    elif(len(unit) == 1):
        if(OrgTemp == []):
            OrgName = OrgName + '\\' + unit[0]
        else:
            for alevel in OrgTemp:
                # print(alevel)
                OrgName = OrgName + '\\' + alevel
            OrgName = OrgName + '\\' + unit[0]
        OrgNameList.append(OrgName)
    else:
        OrgName = OrgNameList[-1]
        OrgNameList.append(OrgName)

# print(OrgList)
# print(OrgNameList)
with open('C:/Users/flyingaura/Desktop/公司通讯录数据(组织机构）.dat', mode = 'w') as infile:
    for Arecord in OrgNameList:
        infile.write('%s\n' %Arecord)




