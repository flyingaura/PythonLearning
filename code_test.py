# 用来验证代码是否好用的模块，不要被外部模块引用
# -*- coding: utf-8 -*-

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


class students(object):
    def __init__(self, studentID, name, grade, subject, province):
        self.__studentID = studentID
        self.__name = name
        self.grade = grade
        self.subject = subject
        self.province = province

    def get_SID(self):
        return self.__studentID

    def get_name(self):
        return self.__name

    # 根据学号确定在专业中的位置
    def get_position(self):
        print('Your Poistion in Subjcet %s is %s' % (self.subject, self.__studentID))


# 学生考试成绩类
class scores(students):
    def __init__(self, studentID, name, grade, subject, province, linguistic, math, english, physics, chemistry):
        students.__init__(self, studentID, name, grade, subject, province)
        self.__linguistic = linguistic
        self.__math = math
        self.__english = english
        self.__physics = physics
        self.__chemistry = chemistry

    def get_name_score(self):
        print('Your Score is : ',self.__math)
        print('your name is : ',self.name)


Wanghd = students('110011f','wanghd','grade3','Software','zhejiang')
print(Wanghd.get_name())
# Wanghd.get_position()

Wanghd_score = scores('110011f','wanghd','grade3','Software','zhejiang',110,135,94,88,121)
print(Wanghd_score.get_name())
Wanghd_score.get_name_score()