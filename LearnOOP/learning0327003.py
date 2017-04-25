# -*- coding: utf-8 -*-

from LearnModule import StringSplit
with open('C:/Users/flyingaura/Desktop/test.txt',mode = 'rb') as wordsfile:
    wordsfile.readline()
    # print(wordsfile.readline().decode('utf-8'))
    all_words = []
    for line in wordsfile.readlines():
        for word in StringSplit.stringsplit(line.decode('utf-8').strip(),(',',' ','.','-')):
            all_words.append(word.lower())

print('The count of Speech Words is: %d' %len(all_words))
print(list(all_words))

unique_words = {}
for aword in all_words:
    if(aword not in unique_words.keys()):
        unique_words[aword] = all_words.count(aword)

print('the count of unique words in this speech is : %d ' % len(unique_words))
for keys in sorted(unique_words,key = lambda x: unique_words[x],reverse = True):
    print('%s : %d ' %(keys,unique_words[keys]))