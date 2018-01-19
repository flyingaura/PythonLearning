#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

'''
设计一个用来做算术训练的游戏 Arithmetic_training_game
'''
import math,random,time
import sys

class ArithmeticMode(object):
    # 定义一个有关算术表达式的类
    def __init__(self,NumList=[0,1,2,3,4,5,6,7,8,9], OperatorList = ['+','-','*','/'],level = 2):
        #Numlist-->参与算术运算的数字列表；OperatorList-->参与算术运算的运算符列表;level表示算术表达式的最大运算级数
        self.NumList = NumList
        self.OperatorList = OperatorList
        self.level = level

    def get_ArtExpress(self):   #生成算术表达式的方法！
        if(self.level < 2):
            print('算术表达式的参与数字不能少于2个！')
            self.ExpressStr = None
        else:
            self.ExpressStr = ''
            Numbers = []
            ZeroTag = 0
            SetLevel = random.randint(2,self.level)
            while(len(Numbers) < SetLevel):
                if(not ZeroTag):
                    ANumGroup = random.sample(self.NumList, 1)
                else:
                    ANumGroup = random.sample(self.NumList[1:], 1)
                    ZeroTag = 0
                ANOperator = random.sample(self.OperatorList, 1)[0]
                if(ANOperator == '/'):
                    ZeroTag = 1
                ANumGroup.append(ANOperator)  #每组算术表达式由一个数字和一个运算符组成
                Numbers.append(ANumGroup)
            # ==========往表达式中随机添加括号==========
            if(SetLevel > 2):
                add_count = 0
                for i in range(SetLevel):
                    if(random.randint(0,1) == 1 and i < SetLevel - 1):
                        Numbers[i].insert(0,'(')
                        add_count += 1
                    elif(add_count and random.randint(0,1) == 0):
                        Numbers[i].insert(1, ')')
                        add_count -= 1
                while(add_count):     #必须保证括号是成对出现的
                    Numbers[-1].insert(1, ')')
                    add_count -= 1
            # ==========表达式最后一位不能是运算符==========
            Numbers[-1].pop()

            # ==========生成算术表达式==========
            for ANumGroup in Numbers:
                self.ExpressStr += ' '.join([str(x) for x in ANumGroup]) + ' '
            self.ExpressStr = self.ExpressStr.strip()
        return self.ExpressStr

    # def get_CalResult(self):  #获取算术表达式计算结果的方法
    #     return eval(self.ExpressStr)




