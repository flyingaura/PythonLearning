# -*- coding: utf-8 -*-

import os

appendixfiles = os.listdir('E:/业务项目/Y.学习资料/EKP共享文档/2014年7月15日')
appendixfilesPath = []
appendixRelativePath = '/ESPnews/appendixfiles'
for afile in appendixfiles:
    appendixfilesPath.append(os.path.join('%s/%s' %(appendixRelativePath,afile)))
print(appendixfilesPath)

# print(os.path.basename(''))