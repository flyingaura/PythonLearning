# -*- coding: utf-8 -*-

#Chapter 1
#Question 31

import math

def check_triangle(a,b,c):  #检测三条边是否满足三角形要求
    if((a + b > c ) and (a + c > b) and (b + c > a)):
        return True
    else:
        return False

def tri_angle(a,b,c): #计算c所对应的顶点角度
    if(not check_triangle(a,b,c)):
        print('输入的三个边长不符合三角形要求')
        return None
    angle_cos = float((a*a + b*b - c*c)/(2*a*b))  #算出顶角的cos值
    de_angle = math.acos(angle_cos)   #通过arccose函数反算出顶角的角度值,返回弧度值
    return de_angle

a = 3.5
b = 4.9
c = 6.32
angle_pi = 180/math.pi
if (not check_triangle(a, b, c)):
    print('输入的三个边长不符合三角形要求')
else:
    A_angle = tri_angle(b,c,a) * angle_pi
    B_angle = tri_angle(a,c,b) * angle_pi
    C_angle = tri_angle(a,b,c) * angle_pi
    print('三角形三个顶角的角度为：顶角A --> %f ，顶角B --> %f ，顶角C --> %f ' %(A_angle,B_angle,C_angle))
    print('三个顶角角度之和为： %f' %(A_angle + B_angle + C_angle))




