# -*- coding: utf-8 -*-
"""
用于时间计算的模块，包含3个函数：
1、将时间转换为秒数的函数time2seconds(time)（从00:00:00起,time是标准时间类型01:23:45）
2、将秒数转换为时间的函数seconds2time(seconds)（时间显示为01:23:45）
3、计算从初始时间起过若干秒数的时间函数  Cal_time(init_time,seconds)
"""
from LearnModule import StringSplit

def time2seconds(time):
    h,m,s = StringSplit.stringsplit(time,':')  #用分隔符“:”拆分成时、分、秒
    return int(h) * 3600 + int(m) * 60 + int(s)

def seconds2time(seconds):
    h = int(seconds / 3600)
    if(h > 24):
        h = h - 24
    m = int((seconds % 3600) / 60)
    s = (seconds % 3600) % 60
    return ('%02d:%02d:%02d' %(h,m,s))

def cal_time(init_time,seconds):
    return seconds2time(time2seconds(init_time) + seconds)


# init_time = '03:43:12'
# seconds = 24 * 3600 + 56
# print(time2seconds(init_time))
# print(cal_time(init_time,seconds))