# -*-coding: utf-8 -*-
# 学习海龟绘图

import turtle

# 定义一个画N角星的函数
def DrawStar(n,step = 100):  #n为星形图的顶点数，step为星形边长
    if(not isinstance(n,int)):
        raise ValueError('The type of star_top_number is Wrong! ')
    # if(not isinstance(degree,(int,float))):
    #     raise ValueError('The type of star_top_degree is Wrong!')
    # step = 100
    if(n < 5):
        raise ValueError('星形边长不能少于5!')
    L_degree = ((n-2) * 180)/n  #星形内部n边形的内角
    # D_degree = 2*(180 - L_degree)
    D_degree = 180 - L_degree
    for i in range(n):
        turtle.forward(step)
        turtle.right(D_degree)
    return None


# 画一个五角星
# DrawStar(6)
step = 80
degree = 120
n = 6
for i in range(n):
    turtle.forward(step)
    turtle.right(degree)
    turtle.forward(step)
    turtle.left(180 - degree)

