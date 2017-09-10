# -*- coding: utf-8 -*-

"""
有一段楼梯台阶有 15 级台阶，以小明的脚力一步最多只能跨 3 级，请问小明登上这段楼梯，有多少种不同的走法?
"""

import random



# StepModList = []
# i = 0
# while(i < 500000):
#     StepNum = 0
#     StepMod = []
#     while(True):
#         StepChoice = random.randint(1,3)
#         StepMod.append(StepChoice)
#         StepNum = StepNum + StepChoice
#         if(StepNum == 15 and StepMod not in StepModList):
#             StepModList.append(StepMod)
#             break
#         if(StepNum > 15):
#             break
#     i = i + 1
#
# print(len(StepModList))

def StepChoiseCount(StepNum):
    if(StepNum == 1):
        return 1
    if(StepNum == 2):
        return 2
    if(StepNum == 3):
        return 4

    StepMode = StepChoiseCount(StepNum - 1) + StepChoiseCount(StepNum - 2) + StepChoiseCount(StepNum - 3)

    return StepMode

print(StepChoiseCount(15))
