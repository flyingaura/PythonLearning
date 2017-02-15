# 学习类和实例的用法（5）
# -*- coding: utf-8 -*-

class screen(object):

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self,value):
        if (not isinstance(value,int)):
            raise ValueError('the type of width is Wrong !')
        if(value <= 0):
            raise ValueError('the scope of width is Overside !')
        self._width = value

    @height.setter
    def height(self,value):
        if(not isinstance(value,int)):
            raise ValueError('the type of height is Wrong !')
        if (value <= 0):
            raise ValueError('the scope of height is Overside !')
        self._height = value

    @property
    def resolution(self):
        return self._resolution
        # return self._width * self._height * 1024

    # #
    @resolution.setter
    def resolution(self,value):
        # return self._width * self._height * 1024
        # self._resolution = self._width * self._height * 1024
        self._resolution = 9999

MyOne = screen()
MyOne.width = 50
MyOne.height = 30
MyOne.resolution = 10
print(MyOne.width,MyOne.height,MyOne.resolution)