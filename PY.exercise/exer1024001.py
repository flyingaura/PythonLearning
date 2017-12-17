# -*- coding: utf-8 -*-

class color(object):

    def __SetColorValue__(self,n):
        if(n < 0):
            self.n = 0
        elif(n > 1):
            self.n = 1
        else:
            self.n = n
        return self.n

    def __init__(self,red = 0.0,green = 0.0,blue = 0.0):
        self.red = self.__SetColorValue__(red)
        self.green = self.__SetColorValue__(green)
        self.blue = self.__SetColorValue__(blue)

    def __add__(self,colorA):
        return color((self.red + colorA.red), (self.green + colorA.green), (self.blue + colorA.blue))

    def __sub__(self, colorA):
        return color((self.red - colorA.red), (self.green - colorA.green), (self.blue - colorA.blue))

    def __str__(self):
        return '(red,green,blue) = (%.5f,%.5f,%.5f)' %(self.red,self.green,self.blue)

colorA = color(0.321,0.949,0.112)
colorB = color(0.344,0.315)
print(colorA)
print(colorB)
print(colorA + colorB)
print(colorB - colorA)