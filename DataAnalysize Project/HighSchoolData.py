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
                + '学校中文名称：%-30s' %(self.fullname) + '||' + '学校英文名称：%-60s' %(self.EnName) + '\n' \
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

datafilepath1 = r'F:\documents\python\learning2017\program data\高校相关数据\2016年全国高等学校名单.csv'
datafilepath2 = r'F:\documents\python\learning2017\program data\高校相关数据\985 and 211名单.csv'
datafilepath3 = r'F:\documents\python\learning2017\program data\高校相关数据\中西部高校基础能力建设工程.csv'
datafilepath4 = r'F:\documents\python\learning2017\program data\高校相关数据\高等学校学科创新引智计划.dat'
datafilepath5 = r'F:\documents\python\learning2017\program data\高校相关数据\教育部与地方共建高校.dat'
datafilepath6 = r'F:\documents\python\learning2017\program data\高校相关数据\教育部直属高等学校名单.dat'

# ========== 读取中西部高校基础能力建设工程高校信息 ==========
# NBACcount = 0
NBACSchoolList = []
# i = 1
for Aschool in readCSV(datafilepath3,'GBK'):
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

# ========== 读取高等学校学科创新引智计划高校信息 ==========
P111schoolList = []
for Aschool in readCSV(datafilepath4,'utf-8'):
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

# ========== 读取985和211高校信息 ==========
HighSchoolCPinfo = {}
for Aschool in readCSV(datafilepath2,'GBK')[2:]:
    try:
        orderNum = int(Aschool[0])
    except ValueError:
        continue
    if(orderNum < 100):
        HighSchoolCPinfo[Aschool[1]] = [Aschool[2],Aschool[5],Aschool[6]]
    else:
        HighSchoolCPinfo[Aschool[1]] = [Aschool[3], Aschool[7], Aschool[8]]

SchoolCPkeys = HighSchoolCPinfo.keys()

# ========== 读取高校办学模式数据 ============
HighSchoolModel = {}
for Aline in readCSV(datafilepath5):
    HighSchoolModel[Aline[2]] = '教育部与地方共建高校'
for Aline in readCSV(datafilepath6):
    HighSchoolModel[Aline[0]] = '教育部直属高等学校'

SchoolModelkeys = HighSchoolModel.keys()

# ========== 读取并设置全部高校基本信息 ==========
HighSchoolList = []
for aline in readCSV(datafilepath1):  #读取全部高校的基本信息
    # print(aline)
    # ========== 判断办学模式 ===========
    if(aline[0].isdigit()):
        if (aline[1] in SchoolModelkeys):
            SchoolModel = HighSchoolModel[aline[1]]
        else:
            SchoolModel = ''

        # ========== 设置高校所属的建设项目 ===========
        ConsProject = {'985Project': False, '211Project': False, 'NBACWC': False, '111Plan': False}
        if (aline[1] in SchoolCPkeys):    #判断是否为985或211大学
            SchoolCategory = HighSchoolCPinfo[aline[1]][0]
            if (HighSchoolCPinfo[aline[1]][1]):
                ConsProject['211Project'] = True
                try:
                    JoinYear = StringSplit.stringsplit(HighSchoolCPinfo[aline[1]][1], ('（', '）'))[1]
                except IndexError:
                    print('出错学校为：%s' % aline[1], end='')
                    print(HighSchoolCPinfo[aline[1]])
                    JoinYear = ''
                ConsProject['211ProjectTime'] = JoinYear

            if (HighSchoolCPinfo[aline[1]][2]):
                ConsProject['985Project'] = True
                try:
                    JoinYear = StringSplit.stringsplit(HighSchoolCPinfo[aline[1]][2], ('（', '）'))[1]
                except IndexError:
                    print('出错学校为：%s' % aline[1], end='')
                    print(HighSchoolCPinfo[aline[1]])
                    JoinYear = ''
                ConsProject['211ProjectTime'] = JoinYear
                ConsProject['985Project'] = JoinYear
        else:
            SchoolCategory = ''

        if (aline[1] in NBACSchoolList):  # 判断是否为中西部高校基础能力建设工程高校
            ConsProject['NBACWC'] = True

        if (aline[1] in P111schoolList):  # 判断是否为高等学校学科创新引智计划高校
            ConsProject['111Plan'] = True

        # ========== 设置高校的运营模式 ===========
        if (aline[5]):
            SchoolRunner = aline[5]
        else:
            SchoolRunner = '公立'

        # 定义一个高校的基本属性信息
        Aschool = HighSchool(OrderID = aline[0], fullname = aline[1], SchoolCategory = SchoolCategory, CompetentDepartment = aline[2], Location = aline[3], SchoolLevel = aline[4],
                             SchoolModel = SchoolModel, SchoolRunner = SchoolRunner, ConsProject = ConsProject)

        HighSchoolList.append(Aschool)

OutFilePath = r'F:\documents\python\learning2017\program data\高校相关数据\全国高校基本信息.dat'

with open(OutFilePath, mode = 'w', encoding = 'utf-8') as outfile:
    outfile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t'
                  %('序号','学校中文名称','学校英文名称','学校中文简称','学校英文简称','学校类别','主管部门',
                    '学校所在地','办学层次','学校运营模式','办学模式','属于985工程','属于211工程','属于中西部高校基础能力建设工程',
                    '属于高等学校学科创新引智计划'))
    outfile.write('\n')
    for Aschool in HighSchoolList:
        if (Aschool.ConsProject['985Project']):
            is985 = 'Y'
        else:
            is985 = 'N'
        if (Aschool.ConsProject['211Project']):
            is211 = 'Y'
        else:
            is211 = 'N'
        if (Aschool.ConsProject['NBACWC']):
            isNBAC = 'Y'
        else:
            isNBAC = 'N'
        if (Aschool.ConsProject['111Plan']):
            is111 = 'Y'
        else:
            is111 = 'N'

        outfile.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t'
                  %(Aschool.OrderID,Aschool.fullname,Aschool.EnName,Aschool.Abbreviation_cn,Aschool.Abbreviation_en,
                    Aschool.SchoolCategory, Aschool.CompetentDepartment, Aschool.Location,
                   Aschool.SchoolLevel,Aschool.SchoolRunner,Aschool.SchoolModel,is985,is211,isNBAC,is111))
        outfile.write('\n')



