# -*- coding: utf-8 -*-
import xlrd
import json

infliepath = r'E:\业务项目\X.内部项目\国务院公文服务（罗斯福计划）项目\项目数据\最终数据\国务院公报 refined V1.0.refined-V1-0.xlsx'
outfilepath = r'E:\业务项目\X.内部项目\国务院公文服务（罗斯福计划）项目\项目数据\最终数据\publicreport1106.json'

xlsfile = xlrd.open_workbook(infliepath)

table = xlsfile.sheets()[0]

# datalist = []
Adata = {}

with open(outfilepath, mode = 'w', encoding= 'utf-8') as outfile:
    for i in range(table.ncols):
        for j in range(table.nrows):
            Adata[table.row(0)[i]] = table.row(j)[i]
        outfile.write(str(Adata.copy()))
        outfile.write('\n')


    # print(table.row(0)[i])
