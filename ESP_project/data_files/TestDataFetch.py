# -*- coding: utf-8 -*-

import json
import os

TestFileList = []
totalcount = 0
icount = 0
testkey = '文件名称'
with open('F:/documents/python/learning2017/ESP_project/data_files/origin_files.json', mode = 'rb') as infile:
    # for i in range(10):
    for Afile in infile.readlines():
        # Afile = infile.readline()
        Afile_decode = Afile.decode('utf-8').strip()
        AfileJson = json.loads(Afile_decode)
        # TestFileList.append(AfileJson)
        totalcount += 1

        if(testkey not in AfileJson.keys()):
            icount += 1
            TestFileList.append(AfileJson)


for Afile in TestFileList:
    print(Afile)
print(totalcount)
print(icount)
# with open('F:/documents/python/learning2017/ESP_project/data_files/files_test.json', mode = 'wb') as outfile:
#     for arecord in TestFileList:
#         outfile.write(json.dumps(arecord, ensure_ascii= False).encode('utf-8'))
#         outfile.write('\n'.encode('utf-8'))

print(os.)