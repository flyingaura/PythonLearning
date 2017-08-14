# -*-coding: utf-8 -*-

"""
编写一个对乳腺癌数据的指标分析与分类诊断工具
数据来源：http://archive.ics.uci.edu/ml/breast-cancer-wisconsin.data
本程序是对exer0512001.py的重构

"""
from LearnModule import StringSplit
import random
from LearnModule import MY_math
# 定义乳腺癌病人数据类
class breast_patients(object):

    def __init__(self,patientID,breastAttrList,diagResult):  #breastAttrList存储乳腺癌指标数据列表，列中每个数据为一个数组（breastAttrValue,breastAttrTags）
        self.patientID = patientID
        self.breastAttrList = breastAttrList
        # self.tagB = [VtagB,TtagB]
        # self.tagC = [VtagC,TtagC]
        # self.tagD = [VtagD,TtagD]
        # self.tagE = [VtagE,TtagE]
        # self.tagF = [VtagF,TtagF]
        # self.tagG = [VtagG,TtagG]
        # self.tagH = [VtagH,TtagH]
        # self.tagI = [VtagI,TtagI]
        self.diagResult = diagResult

    # 定义一个输出指标值列表的方法
    # @classmethod
    def BattrList(self):
        return [x[0] for x in self.breastAttrList]

    # 定义一个打印所有数据的方法
    # @classmethod
    def dataOutput(self):
        print('Patient ID : %10s' %self.patientID)
        # print('%10s | %10s | %10s | %10s | %10s | %10s | %10s | %10s | %10s '
        #       %('tagA','tagB','tagC','tagD','tagE','tagF','tagG','tagH','tagI'))
        for Attr in self.breastAttrList:
            print('%.3f (%s)[%.3f] ||' %(Attr[0],Attr[1],Attr[2]) , end = '\t')
        print('\nDiagnosis Result: %s' %(self.diagResult))
        print('\n')


#定义一个分类器，通过对分类语料数据的学习，找出某种诊断结论的分类特征值,输出分类特征值列表
def Classifier(TrainingDataList):
    AttrData_length = len(TrainingDataList[0].breastAttrList)
    TrainingList_length = len(TrainingDataList)
    Classifier_data = [0] * AttrData_length
    # 计算每个训练数据的肿瘤指标数值之和
    for AtrainingData in TrainingDataList:
        for i in range(AttrData_length):
            Classifier_data[i] = Classifier_data[i] + AtrainingData.breastAttrList[i][0]

    #返回肿瘤指标数值的平均值
    return [(x / TrainingList_length) for x in Classifier_data]

# 定义一个分类分离值计算器，通过分类分离值来判断某种情况应该属性于哪个分类
def SeperateClassify(GoodData,BadData):
    SepDataList = []
    if (len(GoodData) != len(BadData)):
        raise IndexError ('IndexError --> 两个列表长度不一致！')
        return None
    for i in range(len(GoodData)):
        SepDataList.append((GoodData[i] + BadData[i]) / 2)

    return SepDataList

# 定义一个分类诊断函数，判断一个病人有多少项指标是正常，多少项指标异常，并根据正常、异常指标数量多少来判断是否得病
def Diagnosis(Patient_data,Sep_Data):
    GoodAttrCount = 0
    BadAttrCount = 0
    if(len(Patient_data.breastAttrList) != len(Sep_Data)):
        raise IndexError('IndexError --> 两个列表长度不一致！')
        return None

    for i in range(len(Sep_data)):
        if(Patient_data.breastAttrList[i][0] <= Sep_Data[i]):
            Patient_data.breastAttrList[i][1] = '-'           #'-'表示指标正常
            Patient_data.breastAttrList[i][2] = Patient_data.breastAttrList[i][0] - Sep_Data[i]
            GoodAttrCount += 1
        else:
            Patient_data.breastAttrList[i][1] = '+'  # '+'表示指标不正常
            Patient_data.breastAttrList[i][2] = Patient_data.breastAttrList[i][0] - Sep_Data[i]
            BadAttrCount += 1

    if (GoodAttrCount > BadAttrCount):
        diag_result = 'Good'
    else:
        diag_result = 'Bad'

    return diag_result

# 定义一个分类器测试函数，输出分类测试错误结果，分类测试精准度
def ClassifyTest(test_data,Sep_Data):
    Diag_wrong = []
    for APatientData in test_data:
        Diag_result = Diagnosis(APatientData,Sep_Data)
        if (Diag_result != APatientData.diagResult):
            Diag_wrong.append(APatientData)

    testAccuracy = 1 - len(Diag_wrong) / len(test_data)

    return (Diag_wrong,testAccuracy)

# 定义一个对错误诊断数据的分析函数，看在现有模型下，哪个指标最容易出错
def AnalysisWD(WrongdataList,Sep_Data):
    AttrData_length = len(Sep_Data)
    GoodDiag_wrong = [0] *  AttrData_length #把良性诊断为恶性的出错情况
    BadDiag_wrong = [0] *  AttrData_length   #把恶性诊断为良性的出错情况
    for APatientdata in WrongdataList:
        if (APatientdata.diagResult == 'Good'):
            for i in range(AttrData_length):
                if(APatientdata.breastAttrList[i][1] == '+'):
                    GoodDiag_wrong[i] += 1
        elif(APatientdata.diagResult == 'Bad'):
            for i in range(AttrData_length):
                if(APatientdata.breastAttrList[i][1] == '-'):
                    BadDiag_wrong[i] += 1

    return (GoodDiag_wrong,BadDiag_wrong)




# ================ 主程序 =====================

# AllData = []
breastPatientList = []
# 从文件中读取所有学习数据
with open('G:/memory/python-learning/learning2017/program data/breast-cancer-wisconsin.data', mode = 'rb') as Datafile:

    for Aline in Datafile.readlines():
        # breastAttrList = []
        # save_tag = 1
        Aline_decode = Aline.decode('utf-8').strip()
        APatientData = StringSplit.stringsplit(Aline_decode,',')
        try:
            breastAttrList = [[int(x),'',0] for x in APatientData[1:-1]]
        except ValueError as e:
            print('ValueError --> 参数错误，该参数无法转换为数值')
            continue

        ABpatient = breast_patients(0,[],'')
        ABpatient.patientID = APatientData[0]
        ABpatient.breastAttrList = breastAttrList
        if(APatientData[-1] == '2'):
            ABpatient.diagResult = 'Good'
        elif(APatientData[-1] == '4'):
            ABpatient.diagResult = 'Bad'
        else:
            ABpatient.diagResult = 'UnKnown'

        # breast_patients.dataOutput()
        breastPatientList.append(ABpatient)

for ABBpatient in breastPatientList:
    ABBpatient.dataOutput()

# 随机选取400组做为训练语料，剩下的做为测试语料
TrainingNum = 400
AllCount = len(breastPatientList)
#保证总数据集比训练数据集要大
while(AllCount - 1 <= TrainingNum):
    TrainingNum = TrainingNum / 2

TrainingIndexSet = MY_math.RandomFetch(AllCount - 1 ,TrainingNum)
TestIndexSet = set(range(AllCount)).difference(TrainingIndexSet)

# print(TrainingIndexSet)
# print(TestIndexSet)

Good_DiagData = []  #学习数据中的良性数据集
Bad_DiagData = []  #学习数据中的恶性数据集
for i in TrainingIndexSet:
    if(breastPatientList[i].diagResult == 'Good'):
        Good_DiagData.append(breastPatientList[i])
    elif(breastPatientList[i].diagResult == 'Bad'):
        Bad_DiagData.append(breastPatientList[i])
    # breastPatientList[i].dataOutput()



# 计算良性的分类特征值
Good_Classify = Classifier(Good_DiagData)
# 计算恶性的分类特征值
Bad_Classify = Classifier(Bad_DiagData)
# 计算两者的分类分离值
Sep_data = SeperateClassify(Good_Classify,Bad_Classify)

print('%s%s%s' %('-'*10,'良性分类特征值为','-'*10))
print(Good_Classify)
print('%s%s%s' %('-'*10,'恶性分类特征值为','-'*10))
print(Bad_Classify)
print('%s%s%s' %('-'*10,'分类分离特征值为','-'*10))
print(Sep_data)
# print(Good_Classify,Bad_Classify,Sep_data)

# 使用测试数据对学习分类特征值进行测试，并输出测试准确性

Test_datalist = []
for j in TestIndexSet:
    Test_datalist.append(breastPatientList[j])

test_result = ClassifyTest(Test_datalist,Sep_data)
print('测试数据数量为： %d ' %(len(TestIndexSet)))
print('测试精度为：%f' %test_result[1])
print('测试错误数据共 %d 个，具体如下表：' %(len(test_result[0])))
# count_GW = 0   #良性判断为恶性的出错数
# count_BW = 0   #恶性判断为良性的出错数

for WrongData in test_result[0]:
    WrongData.dataOutput()

print('分类错误结果分析如下：')
Analysis_result = AnalysisWD(test_result[0],Sep_data)
print('把良性诊断为恶性的出错情况:',Analysis_result[0])
print('把恶性诊断为良性的出错情况:',Analysis_result[1])






