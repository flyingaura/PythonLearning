# -*- coding: utf-8 -*-

"""
设计一个程序用来处理和生成中国全部高校基本数据资源
定义高校数据类：HighSchool(object)

"""

import csv
from LearnModule import StringSplit,String_func

class HighSchool(object):

    def __init__(self, OrderID, fullname, EnName = '', Abbreviation_cn = '', Abbreviation_en = '', SchoolCategory = '', CompetentDepartment = '',
                 Location = '', SchoolLevel = '', SchoolRunner = '', SchoolModel = '', ConsProject = {'985Project': False, '211Project': False, 'NBACWC': False, '111Plan': False}):

        self.OrderID = OrderID
        self.fullname = fullname    #学校中文全称
        self.EnName = EnName  # 学校英文全称
        self.Abbreviation_cn = Abbreviation_cn  # 学校中文简称
        self.Abbreviation_en = Abbreviation_en  # 学校英文简称
        self.SchoolCategory = SchoolCategory  # 学校类别
        self.CompetentDepartment = CompetentDepartment  # 主管部门
        self.Location = Location  # 学校所在地
        self.SchoolLevel = SchoolLevel  # 办学层次
        self.SchoolRunner = SchoolRunner  # 学校运营模式（公立、民办）
        self.SchoolModel = SchoolModel  # 办学模式（教育部，教育部与地方共建高校，其他部委所属，地方建设，其他）
        self.ConsProject = ConsProject  # 建设项目（985 Project , 211 Project, NBACWC（中西部高校基础能力建设工程）, 111 plan（高等学校学科创新引智计划））

    def __str__(self):
        ConsProject_str = ''
        hasCP = 0
        if(self.ConsProject['985Project']):
            hasCP = 1
            ConsProject_str = ConsProject_str + ' ' * 11 + '->' + '985工程' + '\n'
        if (self.ConsProject['211Project']):
            hasCP = 1
            ConsProject_str =  ConsProject_str + ' ' * 11 + '->' + '211工程' + '\n'
        if (self.ConsProject['NBACWC']):
            hasCP = 1
            ConsProject_str = ConsProject_str + ' ' * 11 + '->' + '中西部高校基础能力建设工程' + '\n'
        if (self.ConsProject['111Plan']):
            hasCP = 1
            ConsProject_str = ConsProject_str + ' ' * 11 + '->' + '高等学校学科创新引智计划' + '\n'
        if(hasCP == 0):
            ConsProject_str = ' ' * 18 + '->' + '暂无' + '\n'


        return  '-' * 46  + ' 序号：%5s' %(self.OrderID) + '-' * 46 + '\n' \
                + '学校名称：%-30s' %(self.fullname) + '||' + '学校英文名称：%-60s' %(self.EnName) + '\n' \
                + '学校中文简称: %-30s' %(self.Abbreviation_cn) + '||' + '学校英文简称: %-60s' %(self.Abbreviation_en) + '\n' \
                + '学校类别: %-30s' %(self.SchoolCategory) + '||' + '主管部门: %-60s' %(self.CompetentDepartment) + '\n' \
                + '学校所在地: %-30s' %(self.Location) + '||' + '办学层次: %-60s' %(self.SchoolLevel) + '\n' \
                + '学校运营模式: %-30s' %(self.SchoolRunner) + '||' + '办学模式: %-60s' %(self.SchoolModel) + '\n' \
                + '国家扶持高校建设项目: ' + '\n' \
                + ConsProject_str

def readCSV(filepath,reqcode = 'utf-8'):
    with open(filepath, mode = 'r', encoding= reqcode) as infile:
        datalist = []
        for aline in csv.reader(infile):
            datalist.append(aline)

    return datalist

datafilepath1 = r'F:\memory\python-learning\learning2017\program data\高校相关数据\2016年全国高等学校名单.csv'
datafilepath2 = r'F:\memory\python-learning\learning2017\program data\高校相关数据\985 and 211名单.csv'
datafilepath3 = r'F:\memory\python-learning\learning2017\program data\高校相关数据\中西部高校基础能力建设工程.csv'
datafilepath4 = r'F:\memory\python-learning\learning2017\program data\高校相关数据\高等学校学科创新引智计划.dat'
datafilepath5 = r'F:\memory\python-learning\learning2017\program data\高校相关数据\教育部与地方共建高校.dat'
datafilepath6 = r'F:\memory\python-learning\learning2017\program data\高校相关数据\教育部直属高等学校名单.dat'

HighSchoolList = []

HighSchoolBI = readCSV(datafilepath1)  #读取全部高校的基本信息
HighSchoolKey = readCSV(datafilepath2,'GBK') #读取985和211高校信息
HighSchoolNBAC = readCSV(datafilepath3,'GBK')  #中西部高校基础能力建设工程高校信息
HighSchool111P = readCSV(datafilepath4,'utf-8')  #高等学校学科创新引智计划高校信息

# NBACcount = 0
NBACSchoolList = []
# i = 1
for Aschool in HighSchoolNBAC:
    NBACschools = Aschool[0].split('\t')
    # Acount = String_func.StrExtractNum(NBACschools[1],1)[0]
    # print('%d: %d' %(i,Acount))
    # i += 1
    # NBACcount = NBACcount + Acount
    for Arec in NBACschools[2:]:
        if(Arec != '-' and Arec != ''):
            # print(Arec.strip())
            NBACSchoolList.append(Arec.strip())

# print('NBACCount = %d' %NBACcount)
# print('Count of NBACShool is %d' %(len(NBACSchoolList)))

P111schoolList = []
for Aschool in HighSchool111P:
    P111schools = StringSplit.stringsplit(Aschool[0],(':','、'))
    # Acount = String_func.StrExtractNum(P111schools[0], 1)[0]
    # print('%d: %d' %(i,Acount))
    # i += 1
    # NBACcount = NBACcount + Acount
    for Arec in P111schools[1:]:
        if (Arec != '-' and Arec != ''):
            # print(Arec.strip())
            P111schoolList.append(Arec.strip())

# print('NBACCount = %d' %NBACcount)
# print('Count of NBACShool is %d' %(len(P111schoolList)))


HighSchoolCPinfo = {}
for Aschool in HighSchoolKey[2:]:
    try:
        orderNum = int(Aschool[0])
    except ValueError:
        continue
    if(orderNum < 100):
        HighSchoolCPinfo[Aschool[1]] = [Aschool[2],Aschool[5],Aschool[6]]
    else:
        HighSchoolCPinfo[Aschool[1]] = [Aschool[3], Aschool[7], Aschool[8]]


for aline in HighSchoolBI:
    # print(aline)
    if(aline[1]):
        Aschool = HighSchool(OrderID = aline[0], fullname = aline[1], CompetentDepartment = aline[2], Location = aline[3], SchoolLevel = aline[4])
        if(aline[5]):
            Aschool.SchoolRunner = aline[5]
        else:
            Aschool.SchoolRunner = '公立'

        ConsProject = {'985Project': False, '211Project': False, 'NBACWC': False, '111Plan': False}   #设置学校所拥有的国家扶持建设项目

        if(aline[1] in HighSchoolCPinfo.keys()):    #判断是否为985或211大学
            Aschool.SchoolCategory = HighSchoolCPinfo[aline[1]][0]
            if(HighSchoolCPinfo[aline[1]][1]):
                ConsProject['211Project'] = True
                try:
                    JoinYear = StringSplit.stringsplit(HighSchoolCPinfo[aline[1]][1],('（', '）'))[1]
                except IndexError:
                    print('出错学校为：%s' %aline[1], end = '')
                    print(HighSchoolCPinfo[aline[1]])
                    JoinYear = ''
                ConsProject['211ProjectTime'] = JoinYear

            if(HighSchoolCPinfo[aline[1]][2]):
                ConsProject['985Project'] = True
                try:
                    JoinYear = StringSplit.stringsplit(HighSchoolCPinfo[aline[1]][2], ('（', '）'))[1]
                except IndexError:
                    print('出错学校为：%s' %aline[1], end='')
                    print(HighSchoolCPinfo[aline[1]])
                    JoinYear = ''
                ConsProject['211ProjectTime'] = JoinYear
                ConsProject['985Project'] = JoinYear

        if(aline[1] in NBACSchoolList):   #判断是否为中西部高校基础能力建设工程高校
            ConsProject['NBACWC'] = True

        if(aline[1] in P111schoolList):    #判断是否为高等学校学科创新引智计划高校
            ConsProject['111Plan'] = True

        Aschool.ConsProject = ConsProject.copy()
        HighSchoolList.append(Aschool)

for Aschool in HighSchoolList:
    print(Aschool)









