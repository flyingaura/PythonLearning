# -*- coding: utf-8 -*-

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

# ========== 开始进行解密操作 ==========
# 读取密文
init_letter = []
# for i in range(ord('a'),ord('z') + 1):
#     init_letter.append(chr(i))

letter_stat = {}
total_count = 0
with open('C:/Users/flyingaura/Desktop/text_cry.txt',mode = 'r') as cry_file:
    fulltext = cry_file.read().strip()

for astr in fulltext.lower():
    if(astr not in init_letter):
        init_letter.append(astr)

for astr in init_letter:
    letter_stat[astr] = fulltext.count(astr)
    total_count = total_count + fulltext.count(astr)


for letter_item in sorted(letter_stat.items(),key = lambda d:d[1],reverse = True):
    print('字母：%s ---> 出现次数：%d , 出现机率 %.3f%%'
          %(letter_item[0],letter_item[1],float(letter_item[1] / total_count * 100)))
    maxcount_letter = ''
    if(ord(letter_item) in range(ord('a'),ord('z') + 1) and maxcount_letter == ''):
        maxcount_letter = letter_item[0]



