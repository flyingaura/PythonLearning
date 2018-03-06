#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

infilepath = '/Users/flyingauraMac/Desktop/订阅标签词表_test.txt'
outfilepath = '/Users/flyingauraMac/Desktop/订阅标签词表_test1.txt'

TagWordList = []
with open(infilepath, mode='r', encoding='utf-8') as infile:
    for Aword in infile.readlines():
        TagWordList.append(Aword.strip() + '\tbqcb\t1000')

with open(outfilepath, mode='w', encoding='utf-8') as outfile:
    for Aword in TagWordList:
        outfile.write(Aword + '\n')

