# -*- coding: utf-8 -*-
"""
用于时间计算的模块，包含3个函数：
1、将时间转换为秒数的函数time2seconds(time)（从00:00:00起,time是标准时间类型01:23:45）
2、将秒数转换为时间的函数seconds2time(seconds)（时间显示为01:23:45）
3、计算从初始时间起过若干秒数的时间函数  Cal_time(init_time,seconds)
4、判断一个字符串是否为标准的时间格式（yyyy-mm-dd HH:MM:SS） isVaildDate(date)
4、计算从给定初始时间到指定结果时间中随机生成一个时间  get_randtime(init_time,end_time) (time is yyyy-mm-dd HH:MM:SS)
"""
import time
from LearnModule import StringSplit
import random

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

def isVaildDate(date):
    try:
        if(":" in date):
            time.strptime(date, "%Y-%m-%d %H:%M:%S")
        else:
            time.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False

def get_randtime(init_time, end_time = None):    #end_time为None表示默认当前时间为终止时间
    if(end_time == None):
        end_timeStamp = int(time.time())
    else:
        if(':' not in end_time):
            end_time = end_time + '00:00:00'
        try:
            end_timeStamp = int(time.mktime(time.strptime(end_time, '%Y-%m-%d %H:%M:%S')))
        except ValueError as e:
            raise ('%s --> 结束时间日期格式不正确，请输入标准日期格式 yyyy-mm-dd HH:MM:SS' % e)
    if(':' not in init_time):
        init_time = init_time + '00:00:00'
    try:
        init_timeStamp = int(time.mktime(time.strptime(init_time, '%Y-%m-%d %H:%M:%S')))
    except ValueError as e:
        raise('%s --> 开始时间日期格式不正确，请输入标准日期格式 yyyy-mm-dd HH:MM:SS' %e)

    GetTime = random.randint(init_timeStamp,end_timeStamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(GetTime))

#
# init_time = '2010-01-01 00:00:00'
#
# print(get_randtime(init_time))




