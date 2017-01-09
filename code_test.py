# 用来验证代码是否好用的模块，不要被外部模块引用
# -*- coding: utf-8 -*-

from LearnModule import Func_StringSpilt
from LearnModule import Dict_deal
from LearnModule import StringAddValue

# print(list(range(ord('A'),ord('z')+1)))
# print(range(ord('A'),ord('z')))

#
# def get_area(province):
#     Area = {'East': ['zhejiang', 'shanghai', 'jiangsu', 'fujian', 'anhui'],
#             'SouthEast': ['guangdong', 'guangxi', 'yunnan', 'guizhou'],
#             'NorthEast': ['beijing', 'tianjing', 'hebei', 'henan', 'shangdong']}
#     DisArea = Dict_deal.Key2Value(Area)    # 取得省份与区域对应的dict
#     YourArea = 'others'
#     for key in DisArea:
#         # 把省份都转成小写字母并比较
#         print(key,DisArea[key])
#         if (StringAddValue.StringLower(province) == key):
#             YourArea = DisArea[key]
#     return YourArea
#
# print(get_area('zhejiang'))

#
# class students(object):
#     def __init__(self, studentID, name, grade, subject, province):
#         self.__studentID = studentID
#         self.__name = name
#         self.grade = grade
#         self.subject = subject
#         self.province = province
#
#     def get_SID(self):
#         return self.__studentID
#
#     def get_name(self):
#         return self.__name
#
#     # 根据学号确定在专业中的位置
#     def get_position(self):
#         print('Your Poistion in Subjcet %s is %s' % (self.subject, self.__studentID))
#
#
# # 学生考试成绩类
# class scores(students):
#     def __init__(self, studentID, name, grade, subject, province, linguistic, math, english, physics, chemistry):
#         students.__init__(self, studentID, name, grade, subject, province)
#         self.__linguistic = linguistic
#         self.__math = math
#         self.__english = english
#         self.__physics = physics
#         self.__chemistry = chemistry
#
#     def get_name_score(self):
#         print('Your Score is : ',self.__math)
#         print('your name is : ',self.name)
#
#
# Wanghd = students('110011f','wanghd','grade3','Software','zhejiang')
# print(Wanghd.get_name())
# # Wanghd.get_position()
#
# Wanghd_score = scores('110011f','wanghd','grade3','Software','zhejiang',110,135,94,88,121)
# print(Wanghd_score.get_name())
# Wanghd_score.get_name_score()

# class AAA(object):
#     def __init__(self,aaa,bbb):
#         self.aaa = aaa
#         self.bbb = bbb
#
# class BBB(AAA):
#     def __init__(self,aaa,bbb,ccc):
#         super(BBB,self).__init__(aaa,bbb)
#         self.ccc = ccc
#
#     def get_ABC(self):
#         print('aaa = ',self.aaa)
#
#
#
# NBB = BBB(1,2,3)
# print(NBB.aaa,NBB.ccc)
# NBB.get_ABC()

# print('Origin Score:')
StrList = []
dicttest = {"compound_key_words": "实践过程:5326,教学内容:4471,学生思维:3449,民族音乐:3162,音乐教师:2871,教育观念:2227,音乐信息:2106,音乐教学:2026,教学过程:2004,改变:1992","machine_standard_key_words": "毛线:5968,壁饰:4422,色彩搭配:3385,作品:2716,白乳胶:2662,表现形式:2187,制作教学:2094,制作方法:1849,植绒:1800,材料经济:1748"}
# print(dicttest.keys())
# print(dicttest.values())
for key,value in dicttest.items():
    StrList = Func_StringSpilt.stringsplit(value,',')
    print(key,':')
    for NL in StrList:
        NLL = Func_StringSpilt.stringsplit(NL,':')[0]
        print(NLL)
# dicttest.keys()