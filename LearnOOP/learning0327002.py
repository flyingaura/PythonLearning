# -*- coding: utf-8 -*-

# 做作业
# chapter 3.5.5 豆堆游戏

from LearnModule import MY_math
import random
# viowls = 'aeiou'
# add_str = ['yay','ay']
# while(True):
#     init_str = input('<儿童黑话游戏（Pig Latin）>请输入任意一个英文单词(q退出): ')
#     if(init_str.lower() == 'q'):
#         print('游戏结束！')
#         break
#     trans_str = init_str
#     if(init_str[0] in viowls):
#         trans_str = init_str + add_str[0]
#     else:
#         for i in range(len(init_str)):
#             if(init_str[i] in viowls):
#                 trans_str = init_str[i:] + init_str[:i] + add_str[1]
#                 break
#
#     print('原始单词为 %s ---> 黑话单词为 %s' %(init_str,trans_str))

#chapter 3.5.5 豆堆游戏

def beans_game(init_num,get_num):    #init_num：最开始的豆堆数量  #get_num:这次取走的豆子数量
    try:
        init_num = int(init_num)
        get_num = int(get_num)
    except ValueError as e:
        raise ValueError('参数错误：%s -->输入参数必须为整数类型' %e)

    if(init_num <= 0 or get_num <= 0):
        raise ValueError('参数错误! -->输入参数必须为正整数')

    if(init_num > get_num):
        return init_num - get_num
    else:
        print('豆子取完了！')
        return 0

beans_num = 16
# 两个人先猜谁先取。通过取随机数判断
player_list = []
while(True):
    Aplayer = random.randint(1,100)
    Bplayer = random.randint(1,100)
    if(Aplayer > Bplayer):
        print('玩家A先开始')
        player_list = ['A','B']
        break
    elif(Aplayer < Bplayer):
        print('玩家B先开始')
        player_list = ['B','A']
        break

count_num = 0
while(beans_num):
    count_num = count_num + 1
    # first_getbeans = beans_num
    first_getbeans = random.randint(1,3)
    print('第%d次：现有豆子%d颗----> 玩家%s取了%d颗' %(count_num,beans_num,player_list[0],first_getbeans))
    beans_num = beans_game(beans_num,first_getbeans)
    if(beans_num == 0):
        print('---->玩家%s输了！' % player_list[0])
        break
    second_getbeans = random.randint(1,3)
    print('第%d次：现有豆子%d颗----> 玩家%s取了%d颗' % (count_num, beans_num, player_list[1], second_getbeans))
    beans_num = beans_game(beans_num,second_getbeans)
    if (beans_num == 0):
        print('---->玩家%s输了！' % player_list[1])

print('游戏结束！')
# if(count_num % 2 == 1):
#     print('%splayer lose!' %player_list[0])
# else:
#     print('%splayer lose!' %player_list[1])

