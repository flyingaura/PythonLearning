# 测试模块的搜索与加载

import sys

sys.path.append('G:\memory\c-program\c++')
print('模块路径如下：')
for n in sys.path:
    print(n)
#
# print(sys.path[0])