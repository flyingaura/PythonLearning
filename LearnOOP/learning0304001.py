# -*- coding: utf-8 -*-

class Multiper(object):

    # def MultiperA(self,valueA):
    #     self.valueA = valueA
    #
    # def MultiperB(self,valueB):
    #     self.valueB = valueB
    #
    # def _Multi_result(self):
    #     return self.valueA * self.valueB

    @property
    def MultiperA(self):
        return self.valueA

    @MultiperA.setter
    def MultiperA(self,value):
        self.valueA = value

    @property
    def MultiperB(self):
        return self.valueB

    @MultiperB.setter
    def MultiperB(self,value):
        self.valueB = value

    @property
    def _Multiper_result(self):
        return self.valueA * self.valueB


xxx = Multiper()
xxx.MultiperA = 10
xxx.MultiperB = 20
print(xxx._Multiper_result)