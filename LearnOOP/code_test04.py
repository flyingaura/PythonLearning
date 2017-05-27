# -*- coding: utf-8 -*-

# <<<<<<< Updated upstream
import time
from LearnModule import MY_math
from LearnModule import cal_data
import random
import os
#
# print(MY_math.combination(52,5))

# nlist = (1,2,3)
# print(type(nlist))
# print(isinstance(nlist,(list,tuple)))
#
# # print(nlist[1:])
#
# nlist = [1,2,3,4,5]
#
# result_list = MY_math.fetch_in_list(nlist,3)
# for nl in result_list:
#     print(nl)
from LearnModule import MY_math
# def fetch_in_list(nlist,m):
#     # ============参数校验=============
#     if(not isinstance(nlist,(list,tuple))):
#         raise ValueError('参数错误 --> 第一个输入参数必须为序列类型（list或者tuple）')
#
#     try:
#         # int_n = int(n)
#         int_m = int(m)
#     except ValueError as e:
#         raise ValueError('参数错误 ：%s --> 两个输入参数都必须为正整数' % e)
#
#     if(len(nlist) < int_m):
#         raise ValueError('参数错误 --> 输入的序列长度不能小于第二个值')
#
#     if(int_m < 1):
#         raise ValueError('参数错误 --> 输入参数必须为正整数')
#
#     # ============开始计算=============
#     # ============定义两个退出条件=============
#     num_list = []
#     if(m == 1):
#         for n in nlist:
#             num_list.append([n])
#         return num_list
#     if(len(nlist) == m):
#         num_list.append(nlist)
#         return num_list
#
#     # while(m > 1):
#         # for n in nlist[:-(m-1)]:
#     # ============递归计算=============
#     for temp_list in fetch_in_list(nlist[1:],m-1):
#         temp_list.insert(0,nlist[0])
#         num_list.append(temp_list)
#     for temp_list in fetch_in_list(nlist[1:],m):
#         num_list.append(temp_list)
#
#     return num_list
#
#
# nlist = list(range(1,21))
#
# result = fetch_in_list(nlist,5)
# countf = MY_math.combination(len(nlist),5)
# for templist in result:
#     print(templist)
# # print(len(result),countf)
#
# astr = 'abc'
# for achar in astr:
#     print(achar in ('a','b'))
#
# # print('当前时间为 %s' %time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
# a1 = time.time()
# print(a1)
# time.sleep(3)
# a2 = time.time()
# print(a2)
# print(a2 - a1)

# alist = [1,2,3,4,5]
# print(alist[-5] == alist[0])

# index_num = sorted(list(range(10)),reverse = True)
# print(list(index_num))
# print(len([[]]))
#
# str1 = 'Diablo III and World of Warcraft and STAR WAR'
# print(str1.swapcase())
# print(str1.capitalize())
# print(str1.title())
# print(str1.lower().count('z'))
#
# str2 = 'Diablo III PPP'
#
# print(str2.ljust(20,'-'),str2.rjust(20,'*'),len(str2.rjust(20,'*')))
#
# def array_in_list(nlist,m):
#     # ============参数校验=============
#     if(not isinstance(nlist,(list,tuple))):
#         raise ValueError('参数错误 --> 第一个输入参数必须为序列类型（list或者tuple）')
#
#     try:
#         # int_n = int(n)
#         int_m = int(m)
#     except ValueError as e:
#         raise ValueError('参数错误 ：%s --> 两个输入参数都必须为正整数' % e)
#
#     if(len(nlist) < int_m):
#         raise ValueError('参数错误 --> 输入的序列长度不能小于第二个值')
#
#     if(int_m < 1):
#         raise ValueError('参数错误 --> 输入参数必须为正整数')
#
#     # ============开始计算=============
#     # ============定义退出条件=============
#     num_list = []
#     if(m == 1):
#         for n in nlist:
#             num_list.append([n])
#         return num_list
#
#     # ============递归计算=============
#     for i in range(len(nlist)):
#         temp_num = nlist[i]
#         temp_numlist = nlist.copy()
#         temp_numlist.pop(i)
#         for temp_list in array_in_list(temp_numlist,m-1):  #从序列中取一个，从剩下序列中取剩下几个
#             temp_list.insert(0,temp_num)
#             num_list.append(temp_list)
#
#
#     return num_list

# num_list = ['1','3','5','7','9']
# # print(num_list[::-1][0])
# print(' + '.join(num_list))
# i = 0
# for strlist in MY_math.through_in_list('+-*/',8):
#     print(strlist)
#     i = i + 1
# print(i)

# print(list(range(1,9)))
#
# strings = '1234567890'
# print(strings.replace('45','00',1))
#
# N = None
# if(not N):
#     print('===None')
#
# string1 = '"北许场村、张辛庄村、上马头村、梁各庄村、土桥村、皇木场村'
#
# print(string1.strip('\"'))

# filter_wordlist = ('省', '市', '自治区', '区', '县', '街道', '社区', '镇', '乡', '村', '回民乡')
#
# def alias_province(string1):
#     alias_province_list = []
#     for astr in filter_wordlist:
#         if (len(string1) > len(astr)):
#             filter_index = len(string1) - len(astr)
#             if (string1.find(astr) == filter_index):
#                 print(string1.find(astr))
#                 alias_province_list.append(string1[:filter_index])
#     if (alias_province_list):
#         return alias_province_list
#     else:
#         return None
#
#
# string1 = '北京市'
# print(alias_province(string1))
#
#
# phnum_letter = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
# # 将上面的对应表转换成字母与数字的对应函数
# letter_phnum = {}
# for key,values in phnum_letter.items():
#     for letter in values:
#         letter_phnum[letter] = key
#
# print(letter_phnum)
#
# file_path = 'F:/documents/python/测试数据/root/python数据类型判断及类型转换.txt'
# print(os.path.splitext(os.path.split(file_path)[1]))
#
# Astr = '我爱北京天安门'
# print(Astr.find('北京'))

def search_text(keywords,fileobject):
    with open(fileobject, mode = 'rb') as init_file:
        try:
            fulltext = init_file.read().decode('utf-8')
        except UnicodeDecodeError:
            fulltext = init_file.read().decode('gbk')
    print(fulltext)
    # try:
    #     search_tag = fulltext.find(keywords)
    # except UnicodeEncodeError:
    #     print(fileobject)
    #     search_tag = 0
    if(fulltext.find(keywords) >= 0):
        print(fulltext.find(keywords))
        return True
    else:
        return False


# rec = search_text('数据','F:\documents\python\测试数据\使用Notepad++编辑运行Python程序.txt')
# print(rec)
#
with open('F:\documents\python\测试数据\使用Notepad++编辑运行Python程序.txt', mode = 'rb') as init_file:
    try:
        fulltext = init_file.read().decode('utf-8')
    except UnicodeDecodeError:
        init_file.seek(0)
        fulltext = init_file.read().decode('gbk')
print(fulltext)
# print(type(text))