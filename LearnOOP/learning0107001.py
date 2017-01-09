# 对象的学习用例003
# -*- coding: utf-8 -*-
import math
import types

class ClassDemo(object):
    def DemoShow(self):
        print('this class is just for DemoShow ! ')

class Datatype_print(object):
    def __init__(self,Data1,Data2,Data3):
        self.Data1 = Data1
        self.Data2 = Data2
        self.Data3 = Data3

    def Datatype_show(self):
        print('The data type of ',self.Data1,'is ',type(self.Data1))
        print('The data type of ',self.Data2,'is ',type(self.Data2))
        print('The data type of ',self.Data3,'is ',type(self.Data3))

def fn(x):
    return x*x

# DataA = Datatype_print('\'12345\'',12345,print)
# DataA.Datatype_show()
DemoA = ClassDemo()
DemoA.DemoShow()

print(type(DemoA.DemoShow))
print(type(fn) == types.FunctionType)
print(type(x for x in range(10)) == types.GeneratorType)

# print(type(123))
# print(type('123'))
# print(type(123.456))