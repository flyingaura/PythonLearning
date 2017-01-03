# 练习对象的定义与使用
# -*- coding: utf-8 -*-

import math

# print(math.nan)
# print(math.pi)

# 定义一个对象用来存储名字、性别和年龄

class HumanP(object):
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
# 定义对象的打印信息方法
    def print_HumanInfo(self):
        print('%s is a %s with %d years old !' % (self.name, self.sex, self.age))


class Student(object):
    def __init__(self,Info,people,**others):
        self.Info = Info
        self.people = people
        self.others = others
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

Wang = Student('I am from China!','汉族',nation='中国',school='Bejing Unversity')
# cheng = Student()
# Wang.Info = 'I am from China!'
# Wang.people = '汉族'
# cheng.nation = '中国'
# cheng.Info = 'I am for Beijing'
# cheng.school = 'Beijing Unversity'
print(Wang)
print(Wang.Info,Wang.people,Wang.others)
for key,value in Wang.others.items():
    print('%s : %s' %(key,value))
# print(cheng.Info,cheng.nation,cheng.school)
