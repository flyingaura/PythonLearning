# -*- coding: utf-8 -*-

"""
=========== 做作业 ==========
chapter 3.6
exercise 4  破解密码
"""
# print(chr(ord(' ') + 10))

# 定义一个列表移位算法
def move_list(nlist,move_seed,move_direction = 'r'):  #move_direction定义位移的方向，默认为右
    result_list = nlist[::]
    length_list = len(nlist)
    move_seed = move_seed % length_list
    if(move_direction.lower() != 'l'):  #除非指定了'l'或'L'为左移，其他输入都为右移
        for i in range(length_list):
            if(i + move_seed >= length_list):
                result_list[i + move_seed - length_list] = nlist[i]
            else:
                result_list[i + move_seed] = nlist[i]
    else:
        for i in range(length_list):
            if(i - move_seed < 0):
                result_list[i - move_seed + length_list] = nlist[i]
            else:
                result_list[i - move_seed] = nlist[i]

    return result_list


# 定义一个加密密钥
def key_encryption(en_seed,move_direction = 'r'):
    init_letter = []
    for i in range(ord('a'),ord('z') + 1):
        init_letter.append(chr(i))

    return move_list(init_letter,en_seed,move_direction)

# ============= 开始进行加密计算 =============

while(True):
    encry_seed = input('请输入一个任意正整数作为密钥因子：')
    try:
        int_seed = int(encry_seed)
    except ValueError as e:
        print('输入错误，请输入一个正整数！请重试！')
        continue
    break

init_letter = []
for i in range(ord('a'),ord('z') + 1):
    init_letter.append(chr(i))

with open('C:/Users/flyingaura/Desktop/text_en.txt',mode = 'r') as text_file:
    encry_text = ''
    encry_key = key_encryption(int_seed)

    for astr in text_file.read().strip():
        if(astr.lower() in init_letter):
            encry_text = encry_text + key_encryption(int_seed)[init_letter.index(astr.lower())]
        else:
            encry_text = encry_text + astr

with open('C:/Users/flyingaura/Desktop/text_cry.txt', mode = 'w') as cry_file:
    cry_file.write(encry_text)




# def My_sorted(nlist,deserve = False):
#     # if(not isinstance(nlist,list)):
#     #     raise ValueError('')
#     for n_index in range(len(nlist)):
#         for i in range(n_index,len(nlist)):
#             if((nlist[n_index] < nlist[i]) == deserve ):
#                 n_temp = nlist[n_index]
#                 nlist[n_index] = nlist[i]
#                 nlist[i] = n_temp
#     # if(len(nlist) == 2):
#     #     if((nlist[0] < nlist[1]) == deserve):
#     #         n_temp = nlist[0]
#     #         nlist[0] = nlist[1]
#     #         nlist[1] = n_temp
#     #     return nlist
#     # for i in range(len(nlist)):
#     #     if((nlist[0] < nlist[i]) == deserve):
#     #         My_sorted(nlist[:i],deserve)
#     #         My_sorted(nlist[i+1:],deserve)
#
#     return nlist
#
#
# init_str = list('aildkddlnvadliwllkdvnmcnnvf')
#
# print(My_sorted(init_str))


