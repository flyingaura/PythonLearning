# -*- coding: utf-8 -*-

from LearnModule import String_func
from LearnModule import MY_math
import random

# =================生成所有规则可能性================
code_list = ['A','B','C','D','E','F']
chess_list = MY_math.array_in_list(code_list,4)

# =================随机取出其中一种可能性================
index_num = random.randint(0,len(chess_list))
# print(chess_list[index_num])

# =================游戏规则运算================
# =================#颜色不匹配，判为XX；颜色对，位置不对，判为BK；颜色和位置都对，判为WH
step_num = 0
result_list = ['XX','XX','XX','XX']
win_step = 12
while(True):
    input_chess = []
    step_num = step_num + 1
    print('请在(A,B,C,D,E,F)任输入一个做为你的棋子 !')
    for i in range(1,5):
        onechess = input('<--第 %d 步，请输入第 %d 棋子 >>> ' %(step_num,i)).upper()
        input_chess.append(onechess)
        # if(onechess == chess_list[index_num][i-1]):
        #     result_list[i-1] = 'WH'

    # 判断游戏规则
    for i in range(4):
        if(input_chess[i] in chess_list[index_num]):
            if(input_chess[i] == chess_list[index_num][i]):
                result_list[i] = 'WH'
            else:
                result_list[i] = 'BK'
        else:
            result_list[i] = 'XX'

    win_tag = 1  #胜利标记
    print('========第 %d 步 结果判定========' %step_num)
    for astr in input_chess:
        print('%10s' %astr,end = '')
    print('\n')
    for astr in result_list:
        print('%10s' %astr,end = '')
        if(astr != 'WH'):
            win_tag = 0
    print('\n')
    # 游戏取胜判定
    if(win_tag):
        if(step_num <= win_step):
            print('\n你赢了，一其用了%d步' %step_num)
            break
        else:
            print('\n你猜对了，但你还是输了。你一其用了%d步，超过了%d的要求' %(step_num,win_step))
            break

    # 超过12步后，询问是否继续
    if(step_num == win_step):
        continue_str = ('你已经用了%d步，但仍未猜对。你已经输了！是否继续？ Y/N')
        if(continue_str.lower() in ['y','yes']):
            continue
        else:
            break

# 跳出循环后，游戏结束！
print('游戏结束!')






# for Acode in array_list:
#     print(Acode)
#
# print(len(array_list))
