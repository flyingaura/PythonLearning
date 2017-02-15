# -*- codingf-8 -*-
import math
import types

class students(object):
    def __init__(self,name):
        self.name = name
    def Pstudents(self):
        print('%s ,good good study,day day up!' %self.name)
        return None

class LittleStudents(students):
    def __init__(self,name,schoolname):
        self.name = name
        self.schoolname = schoolname

    def Lstudents(self):
        print('Your school is : %s' %self.schoolname)
        return [self.name,self.schoolname]

def Pstudents():
    print('good good study,day day up!')
    return None

# students().Pstudents()
zhangone = LittleStudents('zhangxiaolong','PekingUniversity')
# zhangone.Pstudents()
# Arribute = zhangone.Lstudents()
# print(Arribute)
chengone = students('chengxiaolong')
# print(type(zhangone))
# print(type(Pstudents))
# print(type(zhangone) == '__main__.students')
# print(type(Pstudents) == types.FunctionType)
# print(list(types))

# print('string'[:1] == 'string'[0])
#
# print(isinstance(zhangone,LittleStudents),isinstance(chengone,LittleStudents))
# print(type(zhangone))
# print(dir(zhangone))
lilong = LittleStudents('Lixiaolong','sss123')
setattr(lilong,'age','xxx')
students.score = 99
LittleStudents.score = 60
# print(hasattr(zhangone,'Pstudents'))
# print(getattr(zhangone,'Sstudents',404))
# fn = getattr(lilong,'Pstudents')
fn = lilong.Pstudents()
print(lilong.score,lilong.age)
# print(fn)
# fn()
# print(dir(zhangone))
# # print(dir(lilong.age))
# print(getattr(zhangone,'age',404))
# print(getattr(lilong,'age',404))