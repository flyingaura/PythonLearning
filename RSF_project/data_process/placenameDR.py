# -*- coding: utf-8 -*-

infilepath = r'F:\documents\python\learning2017\RSF_project\data\地区名称.txt'
PlaceNameList = set()
with open(infilepath, mode = 'r', encoding= 'utf-8') as infile:
    for Aline in infile.readlines():
        PlaceNameList.add(Aline.strip())

print(len(PlaceNameList))