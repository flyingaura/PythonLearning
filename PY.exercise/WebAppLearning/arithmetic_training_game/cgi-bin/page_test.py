# -*- coding: utf-8 -*-

import yate,json,os
#
# page_header = yate.include_header('aaaa')
# print('*' * 40)
# print(page_header)

RecordFilePath = '../data/WrongRecord.json'

# with open(RecordFilePath,mode = 'w+', encoding= 'utf-8') as outfile:
#     # json.dump({'aa':123},outfile)
#     # outfile.seek(0)
#     # print(outfile.read())
#     # jsonstring = json.loads(outfile.read())

print(os.path.isfile(RecordFilePath))