# -*- coding: utf-8 -*-

import os
import json

filepath = r'F:\documents\python\learning2017\ESP_project\data_images\images_normalized.json'

# filestat = os.stat(filepath)
#
# print(filestat)

icount = 0
filesuflist = []
Badfiles = {}
with open(filepath, mode = 'rb') as infile:
    for aline in infile.readlines():
        alineJson = json.loads(aline.decode('utf-8'))
        if(alineJson['imagePixel'] == []):
            filesuffix = alineJson['file_suffix']
            if(filesuffix not in filesuflist):
                Savefiles = []
                filesuflist.append(filesuffix)
                Savefiles.append(alineJson['filename'] + ' | ' + alineJson['fileURL'])
                Badfiles[filesuffix] = Savefiles
                # print(filesuffix)
                # print(Badfiles[filesuffix])
                # print('good')
            else:
                # print(filesuffix)
                # print(Badfiles[filesuffix])
                Badfiles[filesuffix].append(alineJson['filename'] + ' | ' + alineJson['fileURL'])

            # print('%s:%s | %s:%s | %s:' %('filename',alineJson['filename'],'file_suffix',alineJson['file_suffix'],'imagePixel') ,end = '')
            # print(alineJson['imagePixel'])
            icount += 1
print(icount)
for key in Badfiles:
    print('--- %s --- ' % key)
    for afile in Badfiles[key]:
        print(afile)

