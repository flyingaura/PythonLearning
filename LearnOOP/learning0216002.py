#计算十二生肖的程序
# -*- coding: utf-8 -*-

from enum import Enum,unique
import time
# shenxiao = Enum('生肖',('鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪'))
#
#
# print(shenxiao['猴'].value)
#
# n = 2011
# one_sh = shenxiao((n+8)%12+1)
# print(shenxiao.__members__)
# print(one_sh.name ,'==>',one_sh.value)
# print(shenxiao((n+8)%12+1).name,)

#设计一个可以计算生肖的类:第1种方法
@unique
class shengxiao(Enum):

    shu = 0
    niu = 1
    hu = 2
    tu = 3
    long = 4
    she = 5
    ma = 6
    yang = 7
    hou = 8
    ji = 9
    gou = 10
    zhu = 11
    # '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪'
    #定义一个计算生肖的方法
    def __call__(self,birth_year = -1):

        SH_CN = {'shu': '鼠', 'niu': '牛', 'hu': '虎', 'tu': '兔', 'long': '龙', 'she': '蛇', 'ma': '马', 'yang': '羊',
                      'hou': '猴', 'ji': '鸡', 'gou': '狗', 'zhu': '猪'}
        if(birth_year != -1):
            your_SH = SH_CN[shengxiao((birth_year + 8) % 12).name]
            print('你的年龄是 %d' %(time.localtime()[0] - birth_year),'||  你的生肖是 %s' % your_SH)
            # print(SH_CN[shengxiao((birth_year + 8)%12).name])
        else:
            for name,value in shengxiao:
                print('%s ==> %d' %(name,value))
    # # # def cal_SH(self,birth_year):
    #


# MySH = shengxiao()
# shengxiao.hu(1921)

# 计算生肖的第二种方法
class SH2(object):
    def __init__(self,birth_year = -1):
        self.birth_year = birth_year
        # self.SH_CN = {'shu': '鼠', 'niu': '牛', 'hu': '虎', 'tu': '兔', 'long': '龙', 'she': '蛇', 'ma': '马', 'yang': '羊',
        #               'hou': '猴', 'ji': '鸡', 'gou': '狗', 'zhu': '猪'}
        self.SH_list = Enum('生肖',('鼠','牛','虎','兔','龙','蛇','马','羊','猴','鸡','狗','猪'))

    def __call__(self):
        if(self.birth_year >= 0):
            return '你的年龄是： %d ' %(time.localtime()[0] - self.birth_year) + ' |  你的生肖是： %s' %self.SH_list((self.birth_year + 8)%12 + 1).name
        else:
            return list(self.SH_list.__members__)


print(SH2(-2)())
