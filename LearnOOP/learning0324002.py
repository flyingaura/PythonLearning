'''
 巴 比 伦 平 方 根 算 法 ：
(a) 猜 测 数 字 的 平 方 根 。
(b) 用 猜 测 的 数 字 除 原 数 。
(c) 计 算 步 骤 (b) 的 商 与 猜 测 数 的 平 均 值 。
(d) 对 第 （c） 步 的 平 均 值 再 作 猜 测 。
(e) 如 果 新 的 猜 测 值 与 旧 的 猜 测 值 不 同 ， 则 回 到 第 (b) 步 ； 否 则 ， 停 止 。
'''

"""
巴 比 伦 平 方 根 算 法 ：
(a) 猜 测 数 字 的 平 方 根 。
(b) 用 猜 测 的 数 字 除 原 数 。
(c) 计 算 步 骤 (b) 的 商 与 猜 测 数 的 平 均 值 。
(d) 对 第 （c） 步 的 平 均 值 再 作 猜 测 。
(e) 如 果 新 的 猜 测 值 与 旧 的 猜 测 值 不 同 ， 则 回 到 第 (b) 步 ； 否 则 ， 停 止 。
# """
#
# str1 = '你好啊\'s'
# str2 = "你好啊's"
# if(str1 == str2):
#     print('good')
# else:
#     print('bad')
# print(str1,str2)
#
# for i in range(10,100):
#     if(str(i) == str(i)[::-1]):
#         print(str(i)*2)

# num_str = input('请输入需要平方根的整数(q退出):')
# if(num_str.lower() == 'q'):
#     print('success'.upper())
# else:
#     print('Lose'.lower())

str1 = 'Diablo III & World of Warcraft'
# print(str1.find('ord'))
# print(str1.index('ord'))
# print('%s || %s' %(str1.replace('o','8'),str1))

for i in range(11):
    print(i,end = '\t')