# -*- coding: utf-8 -*-
#
import os
import random
from LearnModule import MY_math
#
#
# # exclude = ['','','”','“','，','：','；','）','（', '《','》','～','【','】','、','。','①','③','②','④','⑤','⑥','⑦','⑧','⑨']
# # def checkfile(filepath):
# #     file_Base = os.path.split(filepath)
# #     if(file_Base[0] == ''):
# #         file_dir = os.getcwd()
# #     else:
# #         file_dir = file_Base[0]
# #     print(file_dir)
# #     print(os.listdir(file_dir))
# #     if(file_Base[1] in os.listdir(file_dir)):
# #         return True
# #     else:
# #         return False
# #
# # print(checkfile('exer0427002.py'))
#
# try:
#     outFile = open('F:/documents/python/测试数据/sys_mk_dir/aaa.txt', mode = 'w')
# except FileNotFoundError:
#     file_Base = os.path.split('F:/documents/python/测试数据/sys_mk_dir/aaa.txt')
#     os.mkdir(file_Base[0])
#     outFile = open(os.path.join(file_Base[0],file_Base[1]), mode = 'w')
#
# outFile.write('好好学习，天天向上')
#
# outFile.close()

#
# class breast_data(object):
#
#     def __init__(self,patient_id,tagA,tagB,tagC,tagD,tagE,tagF,tagG,tagH,tagI,diag_result):
#         self.patient_id = patient_id
#         self.tagA = tagA
#         self.tagB = tagB
#         self.tagC = tagC
#         self.tagD = tagD
#         self.tagE = tagE
#         self.tagF = tagF
#         self.tagG = tagG
#         self.tagH = tagH
#         self.tagI = tagI
#         self.diag_result = diag_result
#
#     # 定义一个输出指标值列表的方法
#     def tag_list(self):
#         return [self.tagA, self.tagB, self.tagC, self.tagD, self.tagE, self.tagF
#             , self.tagG, self.tagH, self.tagI]
#
# classify_data = breast_data('Classifier',0,0,0,0,0,0,0,0,0,0)
#
# GoodDiag_wrong = {'tagA':0,'tagB':0,'tagC':0,'tagD':0,'tagE':0,'tagF':0,'tagG':0
#         , 'tagH': 0,'tagI':0}
#
# i = 0
# for Atag in classify_data.tag_list():
#     tag_name = 'tag' + chr(ord('A') + i)
#     GoodDiag_wrong[tag_name] = 100
#     i = i + 1
#
# # print(GoodDiag_wrong)

# ran_int = set()
# while(len(ran_int) != 20):
#     ran_int.add(random.randint(0,100))
#
# print(sorted(ran_int))
# print(set(range(60,90)).difference(ran_int))

# def fn(x):
#     return x * x
# Nlist = [x for x in range(10)]
# print(list(map(fn,Nlist)))

# print([[0,'-']] * 9)
# print(list(range(9))[1:-1])
# breastAttrList = [[int(x),' '] for x in range(9)[1:-1]]
# print(breastAttrList)
# Myset = set([1,2,3])
# a = Myset.add(4)
# print(a)
# Astr = ''
# print('%s' %Astr)
#
# class aaa(object):
#     def __init__(self,value):
#         self.value = value
#
#     # @classmethod
#     def aaa_out(self):
#         print('NO.%3d ,hello world!' %self.value)
#
# aalist = []
#
# for i in range(10):
#     bbb = aaa(i)
#     bbb.key = str(i)
#     aalist.append(bbb)
#
# for abc in aalist:
#     abc.aaa_out()
#     print('----> %s' %abc.key)

for i in range(1,10):
    print(i)