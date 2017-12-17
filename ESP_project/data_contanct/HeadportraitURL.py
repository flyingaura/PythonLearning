# -*- coding: utf-8 -*-

import random

imageURL = {'noheadp':'/ESPcontacts/headportrait/noheadp.png','manheadp':'/ESPcontacts/headportrait/manheadp.png',
'womanheadp':'/ESPcontacts/headportrait/womanheadp.png'}

headpmode = ['noheadp','manheadp','womanheadp']

with open('C:/Users/flyingaura/Desktop/公司通讯录数据(个性说明）.dat', mode = 'w') as infile:
    infile.write('\n' + '=' * 20 +'<用户头像>' + '=' * 20 + '\n')
    for i in range(121):
        infile.write('%s\n' %(imageURL[headpmode[random.randint(0,2)]]))


