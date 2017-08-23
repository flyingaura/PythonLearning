# -*- coding: utf-8 -*-

import os
from LearnModule import StringSplit

AllPathList = os.walk(r'F:\documents\ESP产品开发用数据\ESP_files')
FilePathList = []

for Apath in AllPathList:
    if(Apath[2] != []):
        for Afile in Apath[2]:
            # AfilePath = os.path.join(Apath[0],Afile)
            FilePathList.append([Apath[0],Afile])
            # FilePath = os.path.join(Apath[0],Afile)
            # print(FilePath)


            FilePathlist = StringSplit.stringsplit(Apath[0],'\\')
            # print(FilePathlist[3:][::-1])

            FilePath = ''
            for xpath in FilePathlist[3:][::-1]:
                # print(xpath)
                FilePath = os.path.join(xpath,FilePath)
                # print(xpath,FilePath)
            print(FilePath)
            # FilePath = lambda os.path.join(x,FilePath)