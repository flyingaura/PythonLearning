# -*- coding: utf-8 -*-
# 生成游戏页面
import sys
import yate,arithmetic_training_games

# =================生成一个HTML页面=================
print(yate.start_response())
print(yate.include_header('欢迎来到韦浩宇的算术运算训练营！'))
# print(yate.start_form('arithmetic_training_games.py'))
print(yate.para('即将开始算术训练！',fontsize = 15,fontcolor = '#a52a2a'))
print(yate.start_form(''))
Numlist = [x for x in range(20)]
ArtInstance = arithmetic_training_games.ArithmeticMode(Numlist,level= 2, OperatorList=['-'])

while(True):
    AnExpress = ArtInstance.get_ArtExpress()
    if(0 <= eval(AnExpress) <= 100):
        break
print(yate.header('%s = %s' %(AnExpress,yate.text_inputs('ArithmeticValue') + yate.submit_button('确定')), header_level = 1))
# print()
print(yate.end_form())

print(yate.header('更多算题，敬请期待！'))

# print('%s = ' %(AnExpress))

print(yate.include_footer({'Home':'/index.html'}))