"""
1、给每个字符串加上一个默认串的函数
2、把大写字母统一转换成小写字母的函数
3、删除字符串中指定位置的字符
4、字符串反转
5、字符串拆分（支持多个分隔符）
6、在字符串指定位置插入一个字符串
7、替换字符串指定位置中的字符或字符串
8、删除字符串中的指定字符
"""
# -*- coding: utf-8 -*-
import functools

__author__ = 'Flyingaura_wl'

def StringAddVal(StrN,ValueN):
    StrValue = ValueN
    if(not isinstance(StrValue,str)):
        StrValue = str(ValueN)
    StrN = StrValue + StrN + StrValue
    return StrN


def StringLower(StrN):
    StrGap = ord('a') - ord('A')
    StrTemp = ''
    for n in StrN:
        StrNum = ord(n)
        if(StrNum in range(ord('A'),ord('Z')+1)):
            StrNum = StrNum + StrGap
        StrTemp = StrTemp + chr(StrNum)
        # print(chr(StrNum),StrN[n])

    return StrTemp

def Str_del_letter(Sindex,StrList):
    StrTemp = []
    Astring = ''
    if(Sindex > len(StrList)):
        print('The Position index is more longer than the length of String, cannot process!')
        return None
    else:
        for skey in StrList:
            StrTemp.append(skey)
    StrTemp.pop(Sindex)
    for skey in StrTemp:
        Astring = Astring + skey
    return Astring

# 定义一个字符串反转的函数。 str_reverse('123456') = '654321'
# str_reverse(s) = s[::-1]
# def str_reverse(s):
#     # if (not isinstance(s,str)):
#     #     istr = str(s)
#     # else:
#     #     istr = s
#     # rev_strL = []
#     rev_str = ''
#     for astr in istr:
#         rev_str = astr + rev_str
#     return rev_str

# ======================================================================================
# 增加日志输出功能
def log(func):
    def wrapper(*args,**kw):
        with open('C:/Users/flyingaura/Desktop/stringsplit_log.txt', 'w') as logfile:
            logfile.write('functions %s start at ' %func.__name__)
            logfile.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            logfile.write('\n')
            ret = func(*args,**kw)
            if(not isinstance(args[0],str)):
                logfile.write('ERROR!! The first parameter of %s type is wrong! \n' %func.__name__)
            elif(args[0] == ''):
                logfile.write('ERROR! The first parameter of %s should not be Null \n' %func.__name__)
            else:
                logfile.write('Success! \n')
            logfile.write('functions end at ')
            logfile.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
            logfile.write('\n')
        return ret
    return wrapper


# 5、字符串拆分（支持多个分隔符）

@log
def stringsplit(strN,splitN):
    # strN:待拆分字符串
    # splitN:分隔符,可以多个
    if(not isinstance(strN,str) or strN == ''):
        return None
    i = 0
    strL = []
    for n in range(len(strN)):
        if((strN[n] in splitN)):
            if(i != n):       # 抛掉空串
                strL.append(strN[i:n])
            i = n+1
    if(i <= n):
        strL.append(strN[i:])
    return strL


# 6、在字符串指定位置插入一个字符串
# def addstring(sindex,strN,addstr):
#     str_temp = []
#     result_str = ''
#     for astr in strN:
#         str_temp.append(astr)
#     str_temp.insert(sindex,addstr)
#     for astr in str_temp:
#         result_str = result_str + astr
#     return result_str

# print(addstring(-1,'123456','a'))

# strlist = ['1','2','3']
# strlist.insert(-1,'a')
# print(list(strlist))

# 7、替换字符串指定位置中的字符或字符串
def MY_replace(strN,exp_str,rep_str,rep_count = None):
    '''
    ************* 重构str.replace函数 *************
    :param strN: 原字符串
    :param rep_str:希望被替换的字符串
    :param rep_str: 替换用字符串
    :param rep_count: 替换次数，默认为全部替换
    :return: replaced_str 替换后字符串
    '''

    if(not isinstance(strN,str)):
        raise ValueError('参数错误--->第一个参数必须为字符串')
    if(not isinstance(exp_str,str)):
        raise ValueError('参数错误--->第二个参数必须为字符串')
    if (not isinstance(rep_str, str)):
        raise ValueError('参数错误--->第三个参数必须为字符串')
    if(rep_count):
        if(not isinstance(rep_count,int)):
            raise ValueError('参数错误---> 第三个参数必须为整数')

    length_exp = len(exp_str)
    i_count = 1
    replaced_str = ''
    if(rep_count):
        while(len(strN) - length_exp >= 0 and i_count <= rep_count):
            stop_tag = 1
            for i in range(len(strN) - length_exp + 1):
                if(strN[i:i + length_exp] == exp_str):
                    replaced_str = replaced_str + strN[:i] + rep_str
                    strN = strN[i + length_exp:]
                    i_count = i_count + 1
                    stop_tag = 0
                    break

            if(stop_tag):
                break

    else:
        while (len(strN) - length_exp >= 0):
            stop_tag = 1
            for i in range(len(strN) - length_exp + 1):
                if (strN[i:i + length_exp] == exp_str):
                    replaced_str = replaced_str + strN[:i] + rep_str
                    strN = strN[i + length_exp:]
                    stop_tag = 0
                    break
            if (stop_tag):
                break

    replaced_str = replaced_str + strN
    return replaced_str

# 8、删除字符串中的指定字符
def str_delstr(str1,delstr,ignor_cap = False):
    #str1为原字符串，delstr为希望删除的字符串，ignor_cap：是否忽略要删除字符串大小写。默认False区分大小写
    if(not isinstance(str1,str)):
        raise ValueError('参数错误：%s --> 第1个参数必须为字符串类型')
    if (not isinstance(delstr, str)):
        raise ValueError('参数错误：%s --> 第2个参数必须为字符串类型')
    if (not isinstance(ignor_cap, bool)):
        raise ValueError('参数错误：%s --> 第3个参数必须为布尔值类型')

    start_index = 0
    str_temp = []
    if(ignor_cap):
        str2 = str1.lower()
    else:
        str2 = str1
    while(True):
        del_index = str2.find(delstr,start_index)
        if(del_index == -1):
            str_temp.append(str1[start_index:])
            break
        str_temp.append(str1[start_index:del_index])
        start_index = del_index + len(delstr)

    out_str = ''
    for astr in str_temp:
        out_str = out_str + astr

    return out_str



