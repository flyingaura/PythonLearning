# -*-coding: utf-8 -*-

"""
编写一个对乳腺癌数据的指标分析与分类诊断工具
数据来源：http://archive.ics.uci.edu/ml/breast-cancer-wisconsin.data

"""
from LearnModule import StringSplit
import random
# 定义乳腺癌指标数据类
class breast_data(object):

    def __init__(self,patient_id,tagA,tagB,tagC,tagD,tagE,tagF,tagG,tagH,tagI,diag_result):
        self.patient_id = patient_id
        self.tagA = tagA
        self.tagB = tagB
        self.tagC = tagC
        self.tagD = tagD
        self.tagE = tagE
        self.tagF = tagF
        self.tagG = tagG
        self.tagH = tagH
        self.tagI = tagI
        self.diag_result = diag_result

    # 定义一个输出指标值列表的方法
    def tag_list(self):
        return [self.tagA,self.tagB,self.tagC,self.tagD,self.tagE,self.tagF
            , self.tagG,self.tagH,self.tagI]

    #定义一个打印所有数据的方法
    def data_output(self):
        print('Patient ID : %10d' %self.patient_id)
        print('%10s | %10s | %10s | %10s | %10s | %10s | %10s | %10s | %10s '
              %('tagA','tagB','tagC','tagD','tagE','tagF','tagG','tagH','tagI'))
        print('%10.1f | %10.1f | %10.1f | %10.1f | %10.1f | %10.1f | %10.1f | %10.1f | %10.1f'
              %(self.tagA,self.tagB,self.tagC,self.tagD,self.tagE,self.tagF
            , self.tagG,self.tagH,self.tagI))
        print('Diagnosis Result: %10d' %(self.diag_result))

#定义一个分类器，通过对分类语料数据的学习，找出某种诊断结论的分类特征值,输出分类特征值列表
def Classifier(Learning_data):
    classify_data = breast_data(9999998,0,0,0,0,0,0,0,0,0,99)
    dataList_length = len(Learning_data)
    for AData in Learning_data:
        classify_data.tagA = classify_data.tagA + AData.tagA
        classify_data.tagB = classify_data.tagB + AData.tagB
        classify_data.tagC = classify_data.tagC + AData.tagC
        classify_data.tagD = classify_data.tagD + AData.tagD
        classify_data.tagE = classify_data.tagE + AData.tagE
        classify_data.tagF = classify_data.tagF + AData.tagF
        classify_data.tagG = classify_data.tagG + AData.tagG
        classify_data.tagH = classify_data.tagH + AData.tagH
        classify_data.tagI = classify_data.tagI + AData.tagI

    classify_data.tagA = classify_data.tagA / dataList_length
    classify_data.tagB = classify_data.tagB / dataList_length
    classify_data.tagC = classify_data.tagC / dataList_length
    classify_data.tagD = classify_data.tagD / dataList_length
    classify_data.tagE = classify_data.tagE / dataList_length
    classify_data.tagF = classify_data.tagF / dataList_length
    classify_data.tagG = classify_data.tagG / dataList_length
    classify_data.tagH = classify_data.tagH / dataList_length
    classify_data.tagI = classify_data.tagI / dataList_length

    return classify_data

# 定义一个分类分离值计算器，通过分类分离值来判断某种情况应该属性于哪个分类
def Seperate_Data(GoodData,BadData):
    Sep_Data = breast_data(9999999,0,0,0,0,0,0,0,0,0,99)
    Sep_Data.tagA = (GoodData.tagA + BadData.tagA) / 2
    Sep_Data.tagB = (GoodData.tagB + BadData.tagB) / 2
    Sep_Data.tagC = (GoodData.tagC + BadData.tagC) / 2
    Sep_Data.tagD = (GoodData.tagD + BadData.tagD) / 2
    Sep_Data.tagE = (GoodData.tagE + BadData.tagE) / 2
    Sep_Data.tagF = (GoodData.tagF + BadData.tagF) / 2
    Sep_Data.tagG = (GoodData.tagG + BadData.tagG) / 2
    Sep_Data.tagH = (GoodData.tagH + BadData.tagH) / 2
    Sep_Data.tagI = (GoodData.tagI + BadData.tagI) / 2

    return Sep_Data

# 定义一个分类诊断函数，判断一个病人有多少项指标是正常，多少项指标异常，并根据正常、异常指标数量多少来判断是否得病
def Diagnosis(Patient_data,Sep_Data):
    Good_tag = []
    Bad_tag = []
    tagList = Patient_data.tag_list()
    Sep_tagList = Sep_Data.tag_list()
    for i in range(len(tagList)):
        if(tagList[i] < Sep_tagList[i]):
            Good_tag.append(tagList[i])
        else:
            Bad_tag.append(tagList[i])

    if (len(Good_tag) > len(Bad_tag)):
        diag_result = 2
    else:
        diag_result = 4

    return (Patient_data.patient_id,Good_tag,Bad_tag,diag_result)

# 定义一个分类器测试函数，输出分类测试错误结果，分类测试精准度
def ClassifyTest(test_data,Sep_Data):
    Diag_wrong = []
    for Adata in test_data:
        Diag_result = Diagnosis(Adata,Sep_Data)
        if (Diag_result[3] != Adata.diag_result):
            Diag_wrong.append(Adata)

    test_accuracy = 1 - len(Diag_wrong) / len(test_data)

    return (Diag_wrong,test_accuracy)

# 定义一个对错误诊断数据的分析函数，看在现有模型下，哪个指标最容易出错
def AnalysisWD(Wrong_data,Sep_Data):
    GoodDiag_wrong = {'tagA':0,'tagB':0,'tagC':0,'tagD':0,'tagE':0,'tagF':0,'tagG':0
        , 'tagH': 0,'tagI':0}  #把良性诊断为恶性的出错情况
    BadDiag_wrong = {'tagA':0,'tagB':0,'tagC':0,'tagD':0,'tagE':0,'tagF':0,'tagG':0
        , 'tagH': 0,'tagI':0}   #把恶性诊断为良性的出错情况
    for Adata in Wrong_data:
        tagList = Adata.tag_list()
        Sep_tagList = Sep_Data.tag_list()
        if(Adata.diag_result == 2):
            for i in range(len(tagList)):
                if(tagList[i] >= Sep_tagList[i]):
                    tag_name = 'tag' + chr(ord('A') + i)
                    GoodDiag_wrong[tag_name] = GoodDiag_wrong[tag_name] + 1
        else:
            for i in range(len(tagList)):
                if(tagList[i] < Sep_tagList[i]):
                    tag_name = 'tag' + chr(ord('A') + i)
                    BadDiag_wrong[tag_name] = BadDiag_wrong[tag_name] + 1

    return (GoodDiag_wrong,BadDiag_wrong)

# ================ 主程序 =====================

AllData = []
# 从文件中读取所有学习数据
with open('C:/Users/flyingaura/Desktop/breast-cancer-wisconsin.data', mode = 'rb') as Datafile:
    for Aline in Datafile.readlines():
        Adata = []
        save_tag = 1
        Aline_decode = Aline.decode('utf-8').strip()
        for x in StringSplit.stringsplit(Aline_decode,','):
            try:
                Adata.append(int(x))
            except ValueError:
                save_tag = 0
                break
        if(save_tag):
            AllData.append(breast_data(Adata[0],Adata[1],Adata[2],Adata[3],Adata[4], Adata[5],
                                   Adata[6],Adata[7],Adata[8],Adata[9],Adata[10]))

# 随机选取400组做为训练语料，剩下的做为测试语料
ML_indexList = set()
ML_count = 400
DataCount = len(AllData)
print(DataCount)
if(DataCount < 400):
    ML_count = DataCount / 2

while(len(ML_indexList) < ML_count):
    ML_indexList.add(random.randint(0,DataCount - 1))

Test_indexList = set(range(DataCount)).difference(ML_indexList)

Good_DiagData = []  #学习数据中的良性数据集
Bad_DiagData = [] #学习数据中的恶性数据集
for i in ML_indexList:
    if(AllData[i].diag_result == 2):
        Good_DiagData.append(AllData[i])
    else:
        Bad_DiagData.append(AllData[i])

# 计算良性的分类特征值
Good_Classify = Classifier(Good_DiagData)
# 计算恶性的分类特征值
Bad_Classify = Classifier(Bad_DiagData)
# 计算两者的分类分离值
Sep_data = Seperate_Data(Good_Classify,Bad_Classify)

print('%s%s%s' %('-'*10,'良性分类特征值为','-'*10))
Good_Classify.data_output()
print('%s%s%s' %('-'*10,'恶性分类特征值为','-'*10))
Bad_Classify.data_output()
print('%s%s%s' %('-'*10,'分类分离特征值为','-'*10))
Sep_data.data_output()
# print(Good_Classify,Bad_Classify,Sep_data)

# 使用测试数据对学习分类特征值进行测试，并输出测试准确性

Test_datalist = []
for j in Test_indexList:
    Test_datalist.append(AllData[j])

test_result = ClassifyTest(Test_datalist,Sep_data)
print('测试数据数量为： %d ' %(len(Test_indexList)))
print('测试精度为：%f' %test_result[1])
print('测试错误数据共 %d 个，具体如下表：' %(len(test_result[0])))
count_GW = 0   #良性判断为恶性的出错数
count_BW = 0   #恶性判断为良性的出错数

for WrongData in test_result[0]:
    WrongData.data_output()

print('分类错误结果分析如下：')
Analysis_result = AnalysisWD(test_result[0],Sep_data)
print('把良性诊断为恶性的出错情况:',sorted(Analysis_result[0].items(),key = lambda d:d[1],reverse = True))
print('把恶性诊断为良性的出错情况:',sorted(Analysis_result[1].items(),key = lambda d:d[1],reverse = True))






