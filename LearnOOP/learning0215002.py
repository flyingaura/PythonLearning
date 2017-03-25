# 编写一个杨辉三角的生成器类
# -*- coding: utf-8 -*-

import types
class YHtriangle(object):

    def __init__(self,n = None):  #类初始化
        self.YH_temp = [0,1,0]
        self.n = n
        self.YH_list = []
        # self.YH_a = 1

    def __iter__(self):  #迭代器
        return self

    def __next__(self):  #依次迭代生成数值的算法
        self.YH_list = self.YH_temp
        self.YH_temp = [0,0]
        if(self.n == None):
            if (len(self.YH_list) > 10):
                raise StopIteration()
        else:
            if(len(self.YH_list) > self.n + 2):
                raise StopIteration()
        for i in range(len(self.YH_list) - 1):
            self.YH_value = self.YH_list[i] + self.YH_list[i+1]
            self.YH_temp.insert(i+1,self.YH_value)
        return self.YH_list

    def __getitem__(self,n):  #按指标或切片取值
        self.YH_list = [0, 1, 0]
        if(isinstance(n,int)):
            for x in range(n):
                self.YH_temp = [0, 0]
                for i in range(len(self.YH_list) - 1):
                    self.YH_value = self.YH_list[i] + self.YH_list[i + 1]
                    self.YH_temp.insert(i + 1, self.YH_value)
                self.YH_list = self.YH_temp
            return self.YH_list
        if(isinstance(n,slice)):
            YH_L = []
            for x in range(n.stop):
                self.YH_temp = [0, 0]
                for i in range(len(self.YH_list) - 1):
                    self.YH_value = self.YH_list[i] + self.YH_list[i + 1]
                    self.YH_temp.insert(i + 1, self.YH_value)
                if(x >= n.start):
                    YH_L.append(self.YH_list)
                self.YH_list = self.YH_temp
            return YH_L

def YH_format(n,YH_list):    #定义一个杨辉三角格式化输出的方法

    L_temp = []

    L_index = int(len(YH_list) / 2)
    # print('***:', n, len(YH_list),YH_list, L_index)
    if(n + 2 >= len(YH_list)):
        # if (n == None):
        #     n = 10
        # print('***:',n,YH_list)

        for i in range(2*n + 1):
            L_temp.append(' ')
        for i in range(len(YH_list)):
            if(YH_list[i] == 0):
                YH_list[i] = ' '


        if (len(YH_list)%2 == 0 ):
            step_i = 1
            while((L_index - step_i) >=0 and (n + 1 - step_i*2) >= 0):

                L_temp[n + 1 - step_i*2] = YH_list[L_index - step_i]
                L_temp[n - 1 + step_i*2] = YH_list[L_index - 1 + step_i]
                step_i = step_i + 1
        else:
            step_i = 0
            while ((L_index - step_i) >= 0 and (n - step_i * 2) >= 0):
                # print('++++:', n - 1 + step_i * 2, L_index - 1 + step_i)
                L_temp[n - step_i * 2] = YH_list[L_index - step_i]
                L_temp[n + step_i * 2] = YH_list[L_index + step_i]
                step_i = step_i + 1

        return L_temp
    else:
        raise ValueError('format list length cannot less than YHtriangle list length !')

#打印在屏幕上
class YH_print(object):    #打印杨辉三角的类
    def __init__(self,YH_list):
        # self.n = n
        self.YH_list = YH_list

    def print_method(self):  #打印的方法
        for n in self.YH_list:
            print(n, end='\t')
        print('\n')



n = 10
fn = YHtriangle(n)
YHlist = []
with open('C:/Users/flyingaura/Desktop/YH%d.txt' % n, 'w') as YH_file:
    for YHdate in fn:
        YHlist = YH_format(n+1,YHdate)
        YH_print(YHlist).print_method()
        for nd in YHlist:
            YH_file.write(str(nd))
        YH_file.write('\n')




    # print(YH_format(5,i))
# print(fn[0])
# # print(fn)
# for i in range(7):
#     print(fn[i])
#     # print('No.%d    ' %i,list(fn[i]))

# for i in fn[6]:
#     print(i)
