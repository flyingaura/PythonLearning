'一个专门用来处理dict类型数据的模块，包含：1、Key2Value（）函数，Key和Value互换'
# -*- coding: utf-8 -*-

__author__ = 'Flyingaura_wl'

def Key2Value(DictObject):
    DisDict = {}
    for key in DictObject:
        # print(key,value)
        DictValue = DictObject[key]
        if(isinstance(DictValue,list)):
            for n in DictValue:
                DisDict[str(n)] = key
        else:
            DisDict[str(DictValue)] = key
    return DisDict

# Area = {'East':['zhejiang','shanghai','jiangsu','fujian','anhui'],'SouthEast':['guangdong','guangxi','yunnan','guizhou'],'NorthEast':['beijing','tianjing','hebei','henan','shangdong']}
# # for key,value in Area.items():
# #     print(key,value)
#     # print(Area[key])
# DisArea = Key2Value(Area)
# print(DisArea)
# # for key,value in DisArea.items():
#     print(key,value)

