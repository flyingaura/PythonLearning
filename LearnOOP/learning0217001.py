# -*-coding: utf-8 -*-

from LearnModule import String_func
"定义一个显示回数的发生器"

# 定义一个判断回数的函数
def if_huishu(n):
    return str(n) == String_func.str_reverse(str(n))

# 定义一个自然数生成序列
def NatureNum(n = None):
    num = 0
    if(n == None):
        while True:
            yield num
            num = num + 1
    elif(not isinstance(n,int)):
        raise ValueError('The type of parameters is not int !')
    else:
        while(num <= n):
            yield num
            num = num + 1

# 定义一个回数生成函数
def huishu(n = None):
    it = NatureNum(n)
    return filter(if_huishu,it)

Nlist = []
for n in huishu():
    if(n <= 20000):
        if(n >= 10000):
            Nlist.append(n)
    else:break
print(list(Nlist))






