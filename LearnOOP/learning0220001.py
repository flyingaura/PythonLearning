# -*- coding: utf-8 -*-
"学习python的错误处理"

import logging

class ZDError(ArithmeticError):
    pass


def foo(s):
    try:
        n = int(s)
    except ValueError as e:
        raise ValueError('__foo__.ValueError is : %s' %e)
    # finally:
    #     print('Caculating Start !')
    print('__foo__.function is starting !')
    if(n == 0):
        raise ZDError('invalid division number :%d' %n)
    return 100/n

def get_err():
    n = input('input a number for division:')
    try:
        ret = foo(n)
        print(ret)
        x = 100/(ret-10)
    # except Exception as e:
        # logging.exception()
    #     logging.exception('__main__.Exception is: %s' %e)
    except ValueError as e:
        print('__main__.ValueError !',e)
    except ZDError as e:
        print('__main__.ZDError: %s' % e)
    except ZeroDivisionError as e:
        print('__main__.ZeroDivisionError: %s' %e)
        # raise
    finally:
        print('Caculating End !')

get_err()
