# -*- coding: utf-8 -*-
# 练习doctest(单元测试)

def fn(string = ''):
    '''
    >>> fn()
     是一个回文串
    >>> fn('abcba')
    abcba 是一个回文串
    >>> fn('123')
    123 不是一个回文串
    >>> fn(12321)
    12321 是一个回文串
    '''

    try:
        string = str(string)
        if (string == string[::-1]):
            print('%s 是一个回文串' % string)
        else:
            print('%s 不是一个回文串' % string)
    except ValueError as e:
        print('%s --> 参数类型不正确，请输入字符串' %e)
        # return False

    # while(True):
    #     TheString = input('请输入任意字符串(q退出)：')
    #     if(TheString.lower() == 'q'):
    #         print('程序结束！')
    #         break
    #     if(fn(TheString)):
    #         print('%s 是一个回文串' % TheString)
    #     else:
    #         print('%s 不是一个回文串' % TheString)

if (__name__ == '__fn__'):
    import doctest
    doctest.testmod()