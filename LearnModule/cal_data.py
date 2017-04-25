# -*- coding: utf-8 -*-
"""
用于日期计算的模块，包含几个函数：
1、用于判断是否为闰年的函数 if_leapyear(year)
2、判断当前输入年份格式是否正确的函数（标准格式为：19000101） if_yearformat(data)
3、定义一个当前日期在当前年（从1月1日算起）已过天数的函数 pass_days(data)
4、计算从初始年份起到这个整数天数的年份日期的函数  Cal_Data(init_year,days)
"""

__author__ = 'Flyingaura_wl'
__edittime__ = '20170322'

# 定义一个判断是否闰年的函数
def if_leapyear(year_data):
    if(int(year_data) % 4 == 0 ):
        if(int(year_data) % 100 != 0):
            return True
        elif(int(year_data) % 400 == 0):
            return True
        else:
            return False
    else:
        return False

#定义一个判断当前年份格式是否正确的函数

def if_yearformat(init_year):
    mon2days = {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
    try:
        int_year = int(init_year)
    except ValueError as e:
        print('格式错误：%s  ---> 年份必须为8位正整数' %e)
        return False
    if(int_year < 0):
        print('年份大小不正确 ---> 年份必须为8位正整数')
        return False
    if(len(str(init_year)) != 8):
        print('年份位数不正确 ---> 年份必须为8位正整数')
        return False
    if(str(init_year)[4:6] not in mon2days.keys()):
        print('月份格式不正确 ---> 月份必须为01-12')
        return False
    if(if_leapyear(int(int_year/10000))):  #判断当前年是否为闰年
        mon2days['02'] = 29
    if(((int_year) % 100) <= 0 or ((int_year) % 100) > mon2days[str(init_year)[4:6]]):
        print('日期大小不正确 ---> 日期必须在该月实际天数范围内')
        return False
    return True

#定义一个当前日期在当前年（从1月1日算起）已过天数的函数
def pass_days(init_data):
    mon2days = {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
    # data0 = [int(init_year/10000),int((init_year % 10000)/100),(init_year % 10000) % 100]
    str_data = str(init_data)
    data0 = [int(str_data[:4]),int(str_data[4:6]),int(str_data[6:])]
    sum_passdays = 0
    # leap_year = 0
    if(if_leapyear(data0[0])):
        # leap_year = 1
        mon2days['02'] = 29
    for mons in range(1,data0[1]):
        if(mons <= 0):
            break
        elif(mons < 10):
            str_mons = '0' + str(mons)
        else:
            str_mons = str(mons)
        sum_passdays = sum_passdays + mon2days[str_mons]
    sum_passdays = sum_passdays + data0[2]
    return sum_passdays



#定义计算从初始年份起到这个整数天数的年份日期的函数
def Cal_Data(init_year,days):
    """the format of init_year：19000101"""

    #对输入参数做校验
    if(not if_yearformat(init_year)):
        return None
    try:
        int_days = int(days)
    except ValueError as e:
        print('格式错误：%s ---> 所输入的天数必须为零或正整数' %e)
        return None

    if(int_days < 0):
        print('数值错误 ---> 所输入的天数必须为零或正整数')
        return None

    # 开始计算
    mon2days = {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
    Ayear = str(init_year)[:4]
    Amon = str(init_year)[4:6]
    Aday = str(init_year)[6:]

    if(if_leapyear(Ayear)):  #定义一年有多少天，闰年多一天
        yeardays = 366
        mon2days['02'] = 29
    else:
        yeardays = 365

    if(pass_days(init_year) + int_days <= yeardays):  #当前日期+输入天数仍在当年内的情况
        if(int_days <= (mon2days[Amon]-int(Aday))):
            forday = int(Aday) + int_days
            if(forday < 10):
                Aday = '0' + str(forday)
            else:
                Aday = str(forday)
        else:
            init_mon = int(Amon)
            for mons in range(init_mon+1,13):
                int_days = int_days -(mon2days[Amon]-int(Aday))
                if(mons < 10):
                    Amon = '0' + str(mons)
                else:
                    Amon = str(mons)
                if(int_days < 10):
                    Aday = '0' + str(int_days)
                    break
                elif(int_days <= mon2days[Amon]):
                    Aday = str(int_days)
                    break
                else:
                    Aday = 0
        return Ayear + Amon + Aday
    else:
        next_year = str(int(Ayear) + 1)
        while(len(next_year) < 4):   #保证日期格式正确
            next_year = '0' + next_year
        next_data = next_year + '01' + '01'
        rest_days = pass_days(init_year) + int_days - yeardays - 1  #扣除1月1日这一天
        furday = Cal_Data(next_data,rest_days)   #递归调用计算日期函数
    return furday