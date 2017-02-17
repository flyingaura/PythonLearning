'把一个数字转换为中文单位数字'

__author__ = 'weil'
# -*-coding: utf-8 -*-
from LearnModule import String_func
from LearnModule import str2int

# 定义单个数字与汉字对应字典
Num_List = {'.': '点', '1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '七', '8': '八', '9': '九',
            '0': '零'}
# 定义数字单位列表
Unit_List = ['','十', '百', '千', '万', '亿']

# 定义一个千位内的整数到汉字转换函数
def Numin4(Num,zerotag = 0):
    NumStrList = ['']
    errorinfo = 'The Bit of Number is longer than 5, cannot transform !'
    if(isinstance(Num,int)):
        NumString = str(Num)
    elif(isinstance(Num,str)):
        NumString = Num
    else:
        return errorinfo
    deltag = 0
    while(1):
        if(NumString[0] == '0'):
            NumString = String_func.Str_del_letter(0, NumString)
            deltag = 1
        else:
            break
    Numlen = len(NumString)
    if(Numlen > 4):
        return errorinfo
    elif(str2int.str2int(NumString) == 0):
        Num2String = Num_List['0']
    else:
        i = -1
        j = 0
        while(i >= -Numlen):
            if(NumString[i] == '0' and NumStrList[0] == ''):
                NumStrTemp = ''
            elif (NumString[i] == '0' and NumStrList[0] == Num_List['0']):
                NumStrTemp = ''
            elif(NumString[i] == '0'):
                NumStrTemp = Num_List['0']
            else:
                NumStrTemp = Num_List[NumString[i]] + Unit_List[j]
            NumStrList.insert(0,NumStrTemp)
            i = i - 1
            j = j + 1
        if(zerotag != 0 and deltag == 1):
            Num2String = Num_List['0']
        else:
            Num2String = ''
        for Strkey in NumStrList:
            Num2String = Num2String + Strkey
    return Num2String

# 定义一个任意位整数到汉字的转换函数
def Int2Chinese(Num):
    NumStr = str(Num)
    LNum = len(NumStr)
    if (LNum <= 4):
        int_string = Numin4(NumStr)
    elif (LNum <= 8):
        int_string = Numin4(NumStr[-LNum:-4],1) + Unit_List[4] + Numin4(NumStr[-4:],1)
    else:
        YLNum = LNum - 8
        int_string = Int2Chinese(str2int.str2int(NumStr[0:YLNum])) + Unit_List[5] + Numin4(NumStr[-8:-4],1) + Unit_List[4] + Numin4(NumStr[-4:],1)
    return int_string

# 把一个数字转换为中文单位数字的函数
def Num2Chinese(Num):
    # 判断输入的值是否为数字，如果不是数字，直接报错！
    if (not isinstance(Num,(int,float,str))):
        return 'The type is not a Number, cannot to transform !'
    else:
        NumString = str(Num)
        # 如果是小数，则将整数部分与小数部分分开
        for i in range(len(NumString)):
            if(NumString[i] == '.'):
                Num_int = NumString[0:i]
                Num_dec = NumString[i+1:]
                break
            Num_int = NumString
            Num_dec = ''
        # 输出小数部分
        if(Num_dec != ''):
            dec_string = Num_List['.']
            while (1):
                if (Num_dec[-1] == '0'):
                    Num_dec = String_func.Str_del_letter(-1, Num_dec)
                else:
                    break
            for strN in Num_dec:
                dec_string = dec_string + Num_List[strN]
        else:
            dec_string = Num_dec

#         输出整数部分
        IntNum = str2int.str2int(Num_int)
        int_string = Int2Chinese(IntNum)

    # 合并整数和小数部分，并输出
    return int_string + dec_string

Anum = 193900000300410
# print(str(Anum))
print(Num2Chinese(Anum))
# print(Num2Chinese('6380002812300230000943.214534546'))
# print(str(123422))








