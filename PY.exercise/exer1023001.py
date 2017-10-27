# -*- coding: utf-8 -*-

import csv,random

class goods(object):    #定义一个商品的类，做为帐单的基类

    def __init__(self,goodsID,goodsname,goodsprice,goodsdecr):
        self.goodsID = goodsID  # goodsID做为主键
        self.goodsname = goodsname
        self.goodsprice = goodsprice
        self.goodsdecr = goodsdecr

    def __str__(self):
        return '商品名称：%s | 商品ID： %s | 商品价格：%.2f | 商品描述：%s' %(self.goodsname,self.goodsID,self.goodsprice,self.goodsdecr)

class bill(goods):   #定义一个帐单类，以商品类为基类

    def __init__(self,goodslist):
        self.goodslist = goodslist

    def CalTotalcost(self):
        totalcost = 0
        for key in self.goodslist:
            totalcost =  totalcost + key.goodsprice * self.goodslist[key]
        return totalcost

    def  __mul__(self,otherbill):
        for Akey in otherbill.goodslist:
            if(Akey in self.goodslist.keys()):
                self.goodslist[Akey] = self.goodslist[Akey] + otherbill.goodslist[Akey]
                print('******' + Akey.__str__() + '******')
            else:
                self.goodslist[Akey] = otherbill.goodslist[Akey]
        return self

    def __str__(self):
        printStr = ''
        for key in self.goodslist:
            printStr = printStr + key.__str__() + ' | 商品数量：%d' %(self.goodslist[key]) + '\n'
        printStr = printStr + '商品类数： %d' %(len(self.goodslist)) + '  ||  ' + '帐单总金额：%.2f' %(self.CalTotalcost()) + '\n'
        return printStr

filepath = r'F:\memory\python-learning\learning2017\program data\超市商品信息详细.csv'

GoodsList = []
with open(filepath, mode = 'r', encoding = 'utf-8') as infile:
    i = 0
    NoUseData = infile.readline()
    for Adata in csv.reader(infile):
        if(i < 50):
            goodsA = goods(Adata[1],Adata[2],float(Adata[6]),Adata[3])
            GoodsList.append(goodsA)
            i += 1
        else:
            break

TotalCount = len(GoodsList)
GoodsListA = {}
GoodsListB = {}
ACount = random.randint(1,5)
BCount = random.randint(1,7)

print(TotalCount)

while(len(GoodsListA) < ACount):
    GoodsListA[GoodsList[random.randint(0, TotalCount - 1)]] = random.randint(1,100)

while(len(GoodsListB) < BCount):
    GoodsListB[GoodsList[random.randint(0, TotalCount - 1)]] = random.randint(1,100)

BillA = bill(GoodsListA)
BillB = bill(GoodsListB)
seperaterStr = '=' * 100
print('帐单A' + seperaterStr)
print(BillA)
print('帐单B' + seperaterStr)
print(BillB)
print('帐单A + B' + seperaterStr)
print(BillA * BillB)



