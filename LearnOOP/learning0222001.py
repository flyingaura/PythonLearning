# -*- coding:utf-8 -*-
# 学习程序调试 assert / logging
import logging
import time
logging.basicConfig(level = logging.DEBUG)

def fn(n = None):
    if (not isinstance(n,(int,str))):
        raise ValueError('The type of parameter is WRONG! ')
    try:
        ret = float(100/(int(n)-10))
    except ValueError as e:
        raise ValueError('TYPE WRONG ---> %s' % e)
    except ZeroDivisionError as e:
        raise ZeroDivisionError('Division ERROR ---> %s' % e)
    return ret


# print(int('a'))
# while(True):
#     n = input('input a number(q to quit): ')
#     if(n == 'q'):
#         break
#     else:
#         try:
#             print(fn(n))
#         except ValueError as e:
#             logging.exception('TYPE Wrong: %s' %e)
#         except ZeroDivisionError as e:
#             logging.exception('Division Wrong: %s' %e)
#         finally:
#             print('Process Again!')
#     logging.info('n = %d,==Process END!==' %int(n))

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler('C:/Users/flyingaura/Desktop/test.log')
fh.setLevel(logging.INFO)

ch = logging.StreamHandler()
ch.setLevel(logging.INFO)


# formatter = logging.Formatter('%(proLevel)s @ %(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s' )
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

# logger.info('foobar')
# print(dir(logging.Formatter))

logger.info('Now Start ---> %s' %time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
for n in range(20):
    logger.info('===Function Start=== || the Parameters of fn is : %d ' % n)
    try:
        zt = fn(n)
        logger.info('===== %f =====' % zt)
    except ValueError as e:
        logger.error('The ValueError of fn is : %s' % e)
    except ZeroDivisionError as e:
        logger.error('The DivisionError of fn is : %s' % e)
    finally:
        logger.info('===Function END  === || the Result of fn is : %f ' % zt)



