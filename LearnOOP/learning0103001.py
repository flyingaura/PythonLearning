# 练习对象的定义与使用
# -*- coding: utf-8 -*-

import math

# print(math.nan)
# print(math.pi)

# 定义一个对象用来存储名字、性别和年龄

class HumanP(object):
    def __init__(self,name,sex,age,weight):
        self.__name = name
        self.sex = sex
        self.age = age
        self.weight = weight
# 定义对象的打印信息方法
    def print_HumanInfo(self,ave_weight):
        if(self.weight - ave_weight <= 0 ):
            weight_index = 'TOO SHIN'
        elif(self.weight - ave_weight <= 20):
            weight_index = 'JUST FITTING'
        else:
            weight_index = 'TOO FAT'

        print('%s is a %s with %d years old !' % (self.__name, self.sex, self.age,))
        print('Your Weight is %d and Weight index is %s ! ' %(self.weight,weight_index))

# 定义实例中的内部私有(private)变量值获取

    def get_name(self):
        return self.__name

wang = HumanP('wanghd','female',22,35)
wang.print_HumanInfo(40)
# wang.__name = 'wangff'
print(wang.get_name())


#
# class Student(object):
#     def __init__(self,Info,people,*yourfavors,**others):
#         self.Info = Info
#         self.people = people
#         self.yourfavors = yourfavors
#         self.others = others
        # print(kw)
        # self.kw = kw
        # for key,value in kw.items():
        #     print('%s : %s' %(key,value))
# zhang = HumanP('zhangyi','male',19)
# wang = HumanP('wanger','female',13)
# Li = HumanP('Lijietong','female',23)
# zhang.print_HumanInfo()
# wang.print_HumanInfo()
# Li.print_HumanInfo()
#
# Wang = Student('I am from China!','汉族','swiming','basketball','physics','coding','play game',nation='中国',school='Bejing Unversity')
# # cheng = Student()
# # Wang.Info = 'I am from China!'
# # Wang.people = '汉族'
# # cheng.nation = '中国'
# # cheng.Info = 'I am for Beijing'
# # cheng.school = 'Beijing Unversity'
# print(Wang)
# print(Wang.Info,Wang.people)
# print('My favors are : ')
# for n in Wang.yourfavors:
#     print(n)
# for key,value in Wang.others.items():
#     print('%s : %s' %(key,value))
# # print(cheng.Info,cheng.nation,cheng.school)
