'模块使用测试'
# -*- coding: utf-8 -*-

__author__ = 'from LearningBooks'

import sys

def test():
    args = sys.argv
    if (len(args) == 1):
        print('Hello World !')
    elif(len(args) == 2):
        print('Hello %s !' %args[1])
    else:
        print('too many argments !')

if (__name__ == '__main__' ):
    test()
    print('sys module\'s argments are: ', sys.argv)
