# -*- coding: utf-8 -*-

class linearEquation(object):

    def __init__(self,a = 1.0,b = 0.0):
        self.a = a
        self.b = b

    def valueX(self,LEA):
        if(isinstance(LEA,(int,float))):
            LEA = linearEquation(0,LEA)
        if(isinstance(LEA,linearEquation)):
            if(self.a == LEA.a and self.b == LEA.b):
                return 'AnyValue'
            elif(self.a == LEA.a and self.b != LEA.b):
                return 'NoneValue'
            else:
                return (LEA.b - self.b)/(self.a - LEA.a)
        else:
            raise ValueError('-->方程式的参数必须为数值型')

    def compose(self,LEA):
        if(isinstance(LEA,linearEquation)):
            LEB = linearEquation(self.a * LEA.a, (self.a * LEA.b + self.b))
        elif(isinstance(LEA,(int,float))):
            LEB = self.a * LEA + self.b
        else:
            raise ValueError('-->方程式的参数必须为数值型')
        return LEB

    def __add__(self,LEA):
        if (isinstance(LEA, linearEquation)):
            LEB = linearEquation(self.a + LEA.a, self.b + LEA.b)
        elif (isinstance(LEA, (int, float))):
            LEB = linearEquation(self.a, self.b + LEA)
        else:
            raise ValueError('-->方程式的参数必须为数值型')
        return LEB

    def __radd__(self, LEA):
        return self.__add__(LEA)

    def __str__(self):
        if(self.a):
            if(self.b < 0):
                printstr = 'y = %fx - %f' %(self.a,abs(self.b))
            elif(self.b > 0):
                printstr = 'y = %fx + %f' %(self.a,self.b)
            else:
                printstr = 'y = %fx' %(self.a)
        else:
            printstr = 'y = %f' %(self.b)
        return printstr

# fa = linearEquation(9,17)
fa = -4.3
fb = linearEquation(-3,3)
# fb = 8
# print(fa)
# print(fb)
# print(fa.valueX(fb),fa.valueX(fa))
# print(fa.compose(fb))
# print(fb.compose(fa))
print(fa + fb)