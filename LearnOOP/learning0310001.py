# -*- coding: utf-8 -*-
from io import StringIO
import os
#
# XS = input('input a string:')
MS = StringIO()
# MS.write(XS + '\n' + 'good luck')
# # print(MS.getvalue())
# MS.seek(0)
# # while True:
# #     LS = MS.readline()
# #     if(LS == ''):
# #         break
# #     print(LS.strip())
# LS = MS.readlines()
# for sstr in LS:
#     print(sstr.strip())
# print('Your OS is %s ' % os.name)
# print('Detail of OS : %s' % os.environ)
# print(type(os.environ))
ens = os.environ
print(ens)
# print(ens.items())
# for key in ens:
#     print(key,ens[key])
print(sorted(ens.items(),key = lambda d:d[0]))

# dict_test = {'aaa':123,'bbb':'aaa','ccc':333,'ddd':'uuy'}
# for key,value in dict_test.items():
#     print(key,value)
# MS.write('Your OS is : %s ' % os.name)
# MS.write('\n<====== Detail of OS ======>')
# for sstr in sorted(ens.items(),key = lambda d:d[0]):
#     MS.write('\n%s : %s' %(sstr[0],sstr[1]))
# # # MS.write(os.environ)
# print(MS.getvalue())
# print(ens.get('PATH'))

print(os.path.abspath('.'))
# New_dir_path = os.path.join(os.path.split('F:\documents\python\learning2017\learning2017\LearnOOP')[0],'LearnIO')
New_dir_path1 = os.path.join(os.path.abspath('.'),'LearnIO')
New_dir_path2 = os.path.join(os.path.abspath('.'),'LearnTest')

# #  print(New_dir_path)
# os.mkdir(New_dir_path1)
# os.mkdir(New_dir_path2)

# os.rmdir(New_dir_path)

# os.rename('just_testaaa.jsp','just_test123.txt')
# dirlist = [x for x in os.listdir('C:/Users/flyingaura/Desktop') if os.path.isdir(x)]
# filelist = [x for x in os.listdir('C:/Users/flyingaura/Desktop') if os.path.isfile(x)
#             and (os.path.splitext(x)[1] == '.doc' or os.path.splitext(x)[1] == '.docx')]
# print(list(dirlist))
# filelist = [x for x in os.listdir('C:/Users/flyingaura/Desktop') if os.path.splitext(x)[1] == '.doc' or os.path.splitext(x)[1] == '.docx']
# clear_filelist = []
# for xf in filelist:
#     if (xf[0] != '~'):
#         clear_filelist.append(xf)
# print(list(clear_filelist))
#
# for x in os.listdir('.'):
#     if (os.path.isdir(x)):
#             print(x)
#     # print(x)