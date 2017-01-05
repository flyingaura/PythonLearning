# -*- coding: utf-8 -*-
# 引入自定义的字符串处理模块
from LearnModule import StringAddValue
# 引入自定义的字典类型数据处理模块
from LearnModule import Dict_deal
# 学习类的继承与多态
# 定义一个学生基本信息的类以及一个学习考试成绩的类，考试成绩的类继承学生的基本信息

# 学生基本信息类
class students(object):
    def __init__(self,studentID,name,grade,subject,province):
        self.__studentID = studentID
        self.__name = name
        self.grade = grade
        self.subject = subject
        self.province = province

    def get_SID(self):
        return self.__studentID

    def get_name(self):
        return self.__name

    # 根据学号确定在专业中的位置
    def get_position(self):
        print('Your Poistion in Subjcet %s is %s' %(self.subject,self.__studentID))



# 学生考试成绩类
class scores(students):
    def __init__(self,studentID,name,grade,subject,province,linguistic,math,english,physics,chemistry):
        students.__init__(self,studentID,name,grade,subject,province)
        self.__linguistic = linguistic
        self.__math = math
        self.__english = english
        self.__physics = physics
        self.__chemistry = chemistry



    # 输出一个学生成绩单
    def out_scores(self):
        AddScores = AdditionalScore(get_area(self.province))
        print('Student\'s name : %s | Student\'s ID : %s | Subject : %s ' %(self.name,self.studentID,self.subject))
        print('Origin Score:')
        print('linguistic: %d | math: %d  | english: %d  | physics: %d  | chemistry: %d ' %(self.__linguistic,self.__math,self.__english,self.__physics,self.__chemistry))
        print('Student\'s province %s in %s,it\'s Additional Score: %d' %(self.province,get_area(self.province),AddScores))
        print('linguistic: %d | math: %d  | english: %d  | physics: %d  | chemistry: %d ' % (
        self.__linguistic + AddScores, self.__math + AddScores, self.__english + AddScores, self.__physics + AddScores, self.__chemistry + AddScores))
    # 根据总成绩确定在专业中的位置
    def get_position(self):
        AddScores = AdditionalScore(get_area(self.province))
        Total_Score = self.__linguistic + AddScores + self.__math + AddScores + self.__english + AddScores + self.__physics + AddScores + self.__chemistry + AddScores
        print('Your total Scores in Subjcet %s is %d ' %(self.subject,Total_Score))


# 定义一个判断学生所在区域的函数
def get_area(province):
    Area = {'East': ['zhejiang', 'shanghai', 'jiangsu', 'fujian', 'anhui'],
            'SouthEast': ['guangdong', 'guangxi', 'yunnan', 'guizhou'],
            'NorthEast': ['beijing', 'tianjing', 'hebei', 'henan', 'shangdong']}
    DisArea = Dict_deal.Key2Value(Area)    # 取得省份与区域对应的dict
    YourArea = 'others'
    for key in DisArea:
        # 把省份都转成小写字母并比较
        # print(key, DisArea[key])
        if (StringAddValue.StringLower(province) == key):
            YourArea = DisArea[key]
    return YourArea

# 定义学生根据不同区域有不同的附加分的函数
def AdditionalScore(area):
    AreaAddScore = {'East':10,'SouthEast':15,'NorthEast':5,'others':0}
    # for key in AreaAddScore:
    #     if(key == area):
    #         return AreaAddScore[key]
    #     else:
    #         return 0
    return AreaAddScore[area]


Wanghd = students('110011f','wanghd','grade3','Software','zhejiang')
Wanghd.get_position()

Wanghd_score = scores('110011f','wanghd','grade3','Software','zhejiang',110,135,94,88,121)
Wanghd_score.get_position()

Wanghd_score.out_scores()