# -*- coding: utf-8 -*-

import string

# print(string.digits)

from LearnModule import StringSplit

# words_list = []
# with open('C:/Users/flyingaura/Desktop/sg_wordlist.dat', mode = 'rb') as in_file:
#     for words in in_file.readlines():
#         words_decode = words.decode('utf-8').strip()
#         # print(words.decode('utf-8'))
#         for aword in StringSplit.stringsplit(words_decode, ('\t',' ')):
#             words_list.append(aword)
#
# words_dic = []
# with open('C:/Users/flyingaura/Desktop/SGwordlist.dic', mode = 'w') as out_file:
#     for aword in words_list:
#         if(aword not in words_dic):
#             words_dic.append(aword)
#     for aword in words_dic:
#         aword_encode = aword.encode('utf-8').decode('utf-8')
#         # print(aword_encode.decode('utf-8'))
#         out_file.write('%s\t%s\t%s\t%s\n' %(aword_encode,'tag','1000',aword_encode))
#
# print(len(words_dic))

# -*- coding: utf-8 -*-

import string

# print(string.digits)

from LearnModule import StringSplit

words_list = []
with open('C:/Users/flyingaura/Desktop/国网95598智能知识库项目/POC测试方案/测试数据/知识库3.csv', mode = 'rb') as in_file:
    icount = 0
    error_count = 0
    for words in in_file.readlines():
        words_decode = words.decode('utf-8').strip()
        # print(words_decode)
        try:
            first_letter = words_decode[0]
            # second_letter = words_decode[1]
        except IndexError as e:
            print('错误：%s --->列表不存在！' %e)
            error_count = error_count + 1
        #     # icount = icount + 1
        if(len(words_decode) > 1):
            if(words_decode[0] == '\"' and words_decode[1] != '\"'):
                icount = icount + 1
    #     # print(words.decode('utf-8'))
    #     for aword in StringSplit.stringsplit(words_decode, ('\t',' ')):
    #         words_list.append(aword)
    # print(len(in_file.readlines()))
    print(icount)
    print(error_count)

# with open('C:/Users/flyingaura/Desktop/SGwordlist.dat', mode = 'w') as out_file:
#     for aword in words_list:
#         out_file.write('%s\n' % aword)

# print(len(words_list))