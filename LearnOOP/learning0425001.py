# -*- coding: utf-8 -*-

# otherHash = {}
# otherHash[2] = 10
#
# selfHash = {}
# selfHash[2] = otherHash
# selfHash['2'] = selfHash
#
# # print(selfHash['2']['2']['2'][2][2])
#
# Astr = 'qwerty'
# wanted = 'z'
# print(Astr.find(wanted))
# print(Astr.index(wanted))

from LearnModule import StringSplit

# 定义一个描述英文单词的类
class EnglishWord(object):

    def __init__(self,name,symbol,nominal_meaning):
        self.name = name   #单词拼写
        self.symbol = symbol #单词音标
        self.nominal_meaning = nominal_meaning  #单词词性与词义对应字典{nominal:meaning}

# 定义一个读取英文单词的函数
def readWords(filepath):
    with open(filepath,mode = 'rb') as read_file:
        Words_list = []
        BOM = read_file.read(3)
        for word_rec in read_file.readlines():
            Aword = StringSplit.stringsplit(word_rec.decode('utf-8').strip(',').strip(),',')
            # print(Aword)
            Aword_NM = {}
            for word_NM in Aword[2:]:
                word_no_me = StringSplit.stringsplit(word_NM,'.')
                # print(word_no_me)
                try:
                    Aword_NM[word_no_me[0] + '.'] = word_no_me[1]
                except IndexError:
                    Aword_NM['other nominal'] = word_no_me[0]
            Words_list.append(EnglishWord(Aword[0],Aword[1],Aword_NM))

    return Words_list


with open('C:/Users/flyingaura/Desktop/eng_words.dat', mode = 'w',encoding = 'utf-8') as out_file:
    out_file.write('%-20s|%-20s|%-20s\n' %('单词','音标','词性&词义'))
    out_file.write('-' * 80)
    out_file.write('\n')
    for word_rec in readWords('C:/Users/flyingaura/Desktop/english words.csv'):
        # print('<-- %s -->' %word_rec.symbol)

        try:
            out_file.write('%-22s|' %word_rec.name)
        except UnicodeEncodeError:
            print(word_rec.name)
            out_file.write('%-22s|' % (word_rec.name))
        try:
            out_file.write('%-22s|' %word_rec.symbol)
        except UnicodeEncodeError as e:
            out_file.write('%-22s|' % word_rec.symbol)
        for key,value in word_rec.nominal_meaning.items():
            try:
                out_file.write('< %s > - %s ;' %(key,value))
            except UnicodeEncodeError:
                print('< %s > - %s ;' %(key,value))
                out_file.write('< %8s > - %s ;' % (key, '******'))
        out_file.write('\n')


