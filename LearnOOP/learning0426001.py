# -*- coding: utf-8 -*-

from LearnModule import StringSplit

# 定义一个从文件中读取单词并生成单词列表的函数
def words_list(filepath):
    wordslist = []
    with open(filepath, mode = 'r',encoding = 'utf-8') as init_file:
        for words_rec in init_file.readlines():
            Aword = StringSplit.stringsplit(words_rec.strip(),(' ','|'))
            wordslist.append(Aword[0])

    return wordslist

# 定义一个按单词长度来组织的单词字典表 words_len_dic(wordslist)
def words_len_dic(wordslist):
    words_dic = {}
    for Aword in wordslist:
        if(len(Aword) not in words_dic):
            words_dic[len(Aword)] = [Aword]
        else:
            words_dic[len(Aword)].append(Aword)

    return words_dic

# <---查找大于5个字母的单词，其中只有1个与其余字母不属于同一个电话号码数字--->

# 定义一个电话薄上数字与字母的对应表
phnum_letter = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}


# 定义一个判断一个单词是否满足“只有1个与其余字母不属于同一个电话号码数字”的条件的函数
def if_phnum_word(Aword):
    # 定义一个字母与电话薄数字的对应字典
    letter_phnum = {'v': '8', 'l': '5', 'k': '5', 'c': '2', 's': '7', 'g': '4', 'h': '4',
                    'a': '2', 'e': '3', 'd': '3', 'q': '7', 'o': '6', 'p': '7', 'r': '7',
                    'w': '9', 'z': '9', 'n': '6', 'y': '9', 'x': '9', 'j': '5', 'f': '3',
                    'u': '8', 'b': '2', 't': '8', 'i': '4', 'm': '6'}

    temp_dic = {}
    for Aletter in Aword:
        try:
            dic_value = letter_phnum[Aletter.lower()]
        except KeyError:
            continue
        if(dic_value not in temp_dic):
            temp_dic[dic_value] = 1
        else:
            temp_dic[dic_value] = temp_dic[dic_value] + 1

    if(len(temp_dic) == 2):
        if(1 in temp_dic.values()):
            return True

    return False

length_limit = 5
wordslist = words_list('C:/Users/flyingaura/Desktop/eng_words.dat')
words_dic = words_len_dic(wordslist)

phnum_word = {}
for key in words_dic:
    if(key >= length_limit):
        for Aword in words_dic[key]:
            if(if_phnum_word(Aword)):
                if(key not in phnum_word):
                    phnum_word[key] = [Aword]
                else:
                    phnum_word[key].append(Aword)

for Aresult in sorted(phnum_word.items(),key = lambda d:d[0]):
    print('长度为 %d 的单词结果为：' %Aresult[0], end = '\t')
    for oneword in Aresult[1]:
        print(oneword, end = '\t')
    print('\n')

for Aword in wordslist:
    if(len(Aword) >1 and Aword == Aword[::-1]):
        print(Aword)



