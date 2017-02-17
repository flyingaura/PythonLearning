# -*- coding: utf-8 -*-

"定义一个全奇数生成器,可以支持全序列和切片序列"

def oddNum(n = None):
    Num = 1
    if(n == None):
        while True:
            yield Num
            Num = Num + 2
    elif(isinstance(n,int)):
        while (Num <= n):
            yield Num
            Num = Num + 2
    # elif(isinstance(n,slice)):
    #     nstart = slice.start
    #     nstop = slice.stop
    #     if(nstart == None and nstop == None):
    #         while True:
    #             yield Num
    #             Num = Num + 2
    #     elif (nstart == None and nstop != None):
    #         while (Num <= nstop):
    #             yield Num
    #             Num = Num + 2
    #     elif(nstart != None and nstop == None):
    #         while True:
    #             if(Num >= nstart):
    #                 yield Num
    #             Num = Num + 2
    #     else:
    #         while(Num <= nstop):
    #             if(Num >= nstart):
    #                 yield Num
    #             Num = Num + 2
    #

    else:
        raise ValueError('The type of parameters is not int !')


# "定义一个偶数生成器"
def evenNum(n = None):
    Num = 2
    if (n == None):
        while True:
            yield Num
            Num = Num + 2
    elif (not isinstance(n, int)):
        raise ValueError('The type of parameters is not int !')
    else:
        while (Num <= n):
            yield Num
            Num = Num + 2

# "定义一个素数生成器"
def primes_filter(n):  #定义一个素数的过滤方法
    return lambda x: x % n > 0

def primesNum(n = None):  #定义一个素数生成器
    yield 2
    it = oddNum()
    if (n == None):
        while True:
            outnum = next(it)
            if(outnum > 2):
                yield outnum
                it = filter(primes_filter(outnum),it)
    elif (not isinstance(n, int)):
        raise ValueError('The type of parameters is not int !')
    else:
        outnum = next(it)
        while (outnum <= n):
            if(outnum > 2):
                yield outnum
                it = filter(primes_filter(outnum),it)
            outnum = next(it)



L = []
# for n in oddNum:
#     if(n < 100):
#         L.append(n)
#     else:
#         break
# print(list(L))

# # print(list(evenNum('1000')))
for n in primesNum():
    if (n < 100):
        L.append(n)
    else:
        break
#
print(list(L))
print(list(primesNum(100)))
