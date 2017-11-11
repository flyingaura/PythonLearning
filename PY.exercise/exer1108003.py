# -*- coding: utf-8 -*-

import math
import numpy
from matplotlib import pylab,font_manager,pyplot

font = font_manager.FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=12)

fig = pyplot.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x_values = numpy.arange(-math.pi * 2, math.pi * 2, 0.1)
y_values = [math.sin(x) for x in x_values]

ax.plot(x_values,y_values)
# ax.xlabel('横坐标：角度',fontproperties=font)
# ax.ylabel('纵坐标：sin值',fontproperties=font)
# ax.title('sin(x)图形',fontproperties=font)

pyplot.show()

pylab.plot(x_values,y_values)
pylab.xlabel('横坐标：角度',fontproperties=font)
pylab.ylabel('纵坐标：sin值',fontproperties=font)
pylab.title('sin(x)图形',fontproperties=font)

pylab.show()