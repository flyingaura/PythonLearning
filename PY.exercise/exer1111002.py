# -*- coding: utf-8 -*-

import sys,time
sys.path.append(r'.\WebAppLearning\arithmetic_training_game\cgi-bin')
import arithmetic_training_games


Numlist = [x for x in range(20)]

Ainstance = arithmetic_training_games.ArithmeticMode(Numlist,level= 3, OperatorList=['+','-'])
ExpressCount = 0
TotalTimeCost = 0
quit_tag = 1
print('现在开始算术训练!---->输入q退出')
while(ExpressCount < 20 and quit_tag):
    AnExpress = Ainstance.get_ArtExpress()
    starttime = time.time()
    while (True):
        YourAnswer = input('第 %d 题 ：%s = ' %(ExpressCount + 1, AnExpress))
        if(YourAnswer.lower() != 'q'):
            try:
                Answer_int = int(YourAnswer)
            except ValueError:
                print('请输入正确答案！')
                continue
            else:
                if(Answer_int == eval(AnExpress)):
                    endtime = time.time()
                    TotalTimeCost += endtime - starttime
                    ExpressCount += 1
                    break
                else:
                    print('请输入正确答案！')
                    continue
        else:
            quit_tag = 0
            break

print('<===============训练结束===============>')
print('本轮训练你一共答对了 %d 道题，用时 %d 秒！' %(ExpressCount,TotalTimeCost))