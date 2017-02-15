# # 对类和实例的学习
# # -*- coding: utf-8 -*-
#
# import types
#
# class person(object):  #定义一个类
#     def __init__(self,address,phonenumber,postcode):
#         self.address = address
#         self.phonenumber = phonenumber
#         self.postcode = postcode
#     # __slots__ = ('address','phonenumber','postcode','name','age','country')
#
# class students(object):
#     name = 'No one call'
#     # __slots__ = ('age','score')
#
# def set_name(self,name):
#     self.name = name
#
# person.set_name = set_name
# students.set_name = set_name
# s1 = person('北京市海淀区中关村东路66号','123456788','8874392')
# # person.set_name('None')
# person.name = 'None'
# # students.name = 'everybody'
# s2 = students()
# s2.name = 'No One Call'
# s2.score = 99
# # s2.set_name('zhongtong')
#
#
# print(s1.name)
# print(s2.name,s2.score)
# # s1.set_name = types.MethodType(set_name,s1)
# s1.set_name('lilong')
# # s1.name = 'zhangxiaolong'
# s1.age = 16
# # s1.score = 99
# print(s1.address,s1.phonenumber)
# print(s1.name,s1.age)

class DemoA(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def get_score(self):
        if(not isinstance(self.score, int)):
            # print('the type of name is wrong !')
            return 'the type of name is wrong !'
        if(self.score < 0 or self.score > 100):
            # print('the cope of score is not in [0,100] !')
            return 'the cope of score is not in [0,100] !'
        return self.score

class DemoB(object):

    @property
    def score(self):
        return self.score
    # score = 0

    @score.setter
    def score(self,value):
        if(not isinstance(value,int)):
            raise ValueError('the type of score is not integer !')
        if(value < 0 or value > 100):
            raise ValueError('the cope of score is not in [0,100] OVERSITE!')
        self._score = value

    @property
    def scorelvl(self):
        if(self._score < 60):
            print('Your score is %d ,Not Pass !' %(self._score - 60))
        elif(self._score < 90):
            print('Your score is %d ,Good Work!' %(self._score - 60))
        else:
            print('Your score is %d, Perfect!' %(self._score - 60))




s1 = DemoA('zhanglong','99')
s1.name = 'lilong'
s1.score = 33
print(s1.name,s1.score,s1.get_score())

s2 = DemoB()
s2.score = 12
s2.scorelvl