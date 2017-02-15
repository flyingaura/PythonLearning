# 学习通过类生成一个斐波那契数列生成器
# -*- coding: utf-8 -*-

class iter_fib(object):
    def __init__(self,value = None):
        self.value = value
        self.a = 0
        self.b = 1
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if(self.value == None):
            raise StopIteration()
        self.a,self.b = self.b,self.a + self.b
        # t = [a,b] a = t[0], b = t[1]
        # a = t[0] = 1, b = t[1] = a+b = 2
        # / t[0] = b = 2, t[1] = a+b = 1+2
        # /a = t[0] = 2, b = t[1] = 3
        if(self.i > self.value):
            raise StopIteration('%d 项斐波那契数列计算完成!' %self.value)
        self.i = self.i + 1
        return self.a

class fib(iter_fib):

    def __getitem__(self,n):
        if(isinstance(n,int)):
            a,b = 0,1
            for x in range(n):
                a,b = b,a+b
            return a
        if(isinstance(n,slice)):
            nstart = n.start
            fiblist = []
            if (nstart == None):
                nstart = 0
            a, b = 0, 1
            for x in range(n.stop):
                a,b = b, a+b
                if (x >= nstart):
                    fiblist.append(a)
            return fiblist



fn = fib()
# print(list(fn))
print(fn[4:8])
#
# for n in fn:
#     print(n)
