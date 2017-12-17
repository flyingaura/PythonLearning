# -*- coding: utf-8 -*-

"""
为ESP数据添加ACL（访问权限）
"""

import random
import json

def LoadACL(RoleGroup):

    AllocatedACL = random.sample(RoleGroup,random.randint(1,len(RoleGroup)))
    while(len(AllocatedACL) < 3):
        if(random.randint(1,10) < 5):
            AllocatedACL = random.sample(RoleGroup, random.randint(1, len(RoleGroup)))
        else:
            break

    return AllocatedACL

RoleGroup = ['GeneralManager','ProductCenter','SalesCenter','R&DCenter','PMCenter',
             'QMCenter','CorManager','F&ICenter']

# OriginFilePath = r'F:\documents\python\learning2017\ESP_project\data_knowledge\knowledge_normalized_NoACL.json'
# OutFilePath = r'F:\documents\python\learning2017\ESP_project\data_knowledge\knowledge_normalized.json'

OriginFilePath = r'F:\documents\python\learning2017\ESP_project\data_files\files_normalized.json'
OutFilePath = r'F:\documents\python\learning2017\ESP_project\data_files\files_normalized_ACL.json'

DataList = []
with open(OriginFilePath, mode = 'rb') as infile:
    # i = 0
    for Arec in infile:
        # i += 1
        Arec_json = json.loads(Arec.decode('utf-8'))
        Arec_json['ACL'] = LoadACL(RoleGroup)
        DataList.append(Arec_json)
        # if(i > 10):
        #     break


with open(OutFilePath, mode = 'wb') as outfile:
    for Adata in DataList:
        outfile.write(json.dumps(Adata, ensure_ascii= False).encode('utf-8'))
        outfile.write('\n'.encode('utf-8'))

