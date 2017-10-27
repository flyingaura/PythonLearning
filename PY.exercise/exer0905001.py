"""
定义一个有理数的类，并实现有理数据的加减乘除运算 Rational(N1,N2)
"""
from LearnModule import MY_math

class Rational(object):

    def __init__(self,N1,N2 = 1):
        if(not isinstance(N1,int) or not isinstance(N2,int)):
            raise ValueError('有理数的分子和分母都必须为整数！')
        if(N2 == 0):
            raise ZeroDivisionError('分母不能为零！')
        RN_GCD = MY_math.CalGCD(N1,N2)

        self.numer = N1 // RN_GCD
        self.denom = N2 // RN_GCD

    def __add__(self,RN):   #定义加法
        if (isinstance(RN, int)):
            RN = Rational(RN)
        # RN_gcd = MY_math.CalGCD(self.numer,self.denom)
        RN_lcm = MY_math.CalLCM(self.denom, RN.denom)
        return Rational((self.numer * RN_lcm // self.denom + RN.numer * RN_lcm // RN.denom),RN_lcm)

    def __sub__(self,RN):   #定义减法
        if (isinstance(RN, int)):
            RN = Rational(RN)
        RN_lcm = MY_math.CalLCM(self.denom, RN.denom)
        return Rational((self.numer * int(RN_lcm / self.denom) - RN.numer * int(RN_lcm / RN.denom)), RN_lcm)

    def __mul__(self,RN):   #定义乘法
        if(isinstance(RN,int)):
            RN = Rational(RN)
        return Rational(self.numer * RN.numer, self.denom * RN.denom)

    def __truediv__(self, RN):   #定义除法
        if(isinstance(RN,int)):
            RN = Rational(RN)
        return Rational(self.numer * RN.denom, self.denom * RN.numer)

    def __str__(self):   #定义输出，分数化简输出
        if(self.denom == 1):
            return '%d' % (self.numer)
        return '%d / %d' %(self.numer,self.denom)

    # def __repr__(self):
    #     return self.__str__()


RN1 = Rational(19,27)
RN2 = 5.5

print(RN1,RN2)
print(RN1 + RN2)
print(RN1 - RN2)
print(RN1 * RN2)
print(RN1 / RN2)
# print(2//-4.10)

# print(isinstance(RN1,Rational))