# -*- coding: utf-8 -*-

# 定义一个独立的动物活动空间（正方形，n * n），所有食物和捕食者都必须在这个空间中活动

import random

class LivingSpace(object):
    def __init__(self,n):   #n表示生活空间的边长，每个动物所占用空间为其中1*1的一个格子
        self.n = n
        self.grid = {}
        for i in range(self.n):
            for j in range(self.n):
                self.grid[(i,j)] = ''

    def __str__(self):
        printstr = '-' * (self.n * 4) + '-' + '\n'
        for j in range(self.n):
            for i in range(self.n):
                printstr = printstr + '|' + '%2s ' %(self.grid[(i,j)])
            printstr = printstr + '|' + '\n' + '-' * (self.n * 4) + '-' + '\n'

        return printstr

    def GetGrid(self,i,j):    #获取坐标点（i,j）上的动物实例信息
        try:
            Ainstance = self.grid[(i,j)]
        except KeyError:
            Ainstance = -1
        return Ainstance

    def SetGrid(self,i,j,n):   #为坐标点（i,j）设置动物实例信息
        self.grid[(i,j)] = n
        return None

    def GetLivingSpaceSize(self):   #获取生活空间的大小
        return self.n

class Animal(object):   #定义一个动物的基类

    def __init__(self,livingspace,i = 0,j = 0,name = 'S',alive = True, hungry = 0, hasbaby = 0):    #hababy = 0 表示该动物未怀孕
        self.livingspace = livingspace
        self.i = i
        self.j = j
        self.name = name
        self.alive = alive
        # self.movedtag = movedtag
        self.hungry = hungry
        self.hasbaby = hasbaby
        if(hungry > 3):
            self.alive = False
        if(self.alive):
            self.livingspace.SetGrid(self.i,self.j,self.name)
        else:
            self.livingspace.SetGrid(self.i,self.j,'')


    def moving(self):  #只能是邻近移动，移动到周围的8个格子中
        NoOccupiedGrid = []
        for istep in range(3):
            if(self.i + istep >= 1 and self.i + istep <= self.livingspace.GetLivingSpaceSize()):
                for jstep in range(3):
                    if(self.j + jstep >= 1 and self.j + jstep <= self.livingspace.GetLivingSpaceSize()):
                        if(not self.livingspace.GetGrid((self.i + istep - 1),(self.j + jstep - 1))):
                            NoOccupiedGrid.append(((self.i + istep - 1),(self.j + jstep - 1)))
        if(NoOccupiedGrid):
            MovedGrid = random.sample(NoOccupiedGrid,1)[0]
        else:
            MovedGrid = 0

        return MovedGrid
            # self.livingspace.SetGrid(self.i,self.j,0)
            # self.i = MovedGrid[0]
            # self.j = MovedGrid[1]
            # self.livingspace.SetGrid(self.i, self.j, self.name)

    def __str__(self):
        if(self.alive):
            alivestatus = 'alive'
        else:
            alivestatus = 'death'
        return '%s:(%d,%d):%s' %(self.name,self.i,self.j,alivestatus)

class Sheep(Animal):   #定义羊的类

    def __init__(self,livingspace,i = 0,j = 0,alive = True, hungry = 0, hasbaby = 0):
        Animal.__init__(self, livingspace, i, j, 'S', alive, hungry, hasbaby)

    def SetAlive(self,alive):
        self.alive = alive


class Wolf(Animal):  #定义狼的类

    def __init__(self,livingspace,i = 0,j = 0,alive = True,hungry = 0, hasbaby = 0):
        Animal.__init__(self,livingspace,i,j,'W',alive,hungry, hasbaby)

    def moving(self):  #只能是邻近移动，移动到周围的8个格子中
        NoOccupiedGrid = []
        HaveSheepGrid = []

        for istep in range(3):
            if(self.i + istep >= 1 and self.i + istep <= self.livingspace.GetLivingSpaceSize()):
                for jstep in range(3):
                    if(self.j + jstep >= 1 and self.j + jstep <= self.livingspace.GetLivingSpaceSize()):
                        if(self.livingspace.GetGrid((self.i + istep - 1),(self.j + jstep - 1)) == 'S'):     #找有羊的地方
                            HaveSheepGrid.append(((self.i + istep - 1),(self.j + jstep - 1)))
                        elif(not self.livingspace.GetGrid((self.i + istep - 1),(self.j + jstep - 1))):    #再找空的地方
                            NoOccupiedGrid.append(((self.i + istep - 1),(self.j + jstep - 1)))

        if(HaveSheepGrid):    #优先往有羊的地方移动
            MovedGrid = random.sample(HaveSheepGrid, 1)[0]
            # SheepStatus = 1
        elif(NoOccupiedGrid):
            MovedGrid = random.sample(NoOccupiedGrid, 1)[0]
            # SheepStatus = 0
        else:
            MovedGrid = 0
            # SheepStatus = 0

        return MovedGrid
            # self.livingspace.SetGrid(self.i, self.j, 0)
            # self.i = MovedGrid[0]
            # self.j = MovedGrid[1]
            # self.livingspace.SetGrid(self.i, self.j, self.name)



# 定义一个动物生活空间，初始化羊群和狼群的坐标位置。（狼群数量小于羊群数量）
IslandSize = 20   #定义动物生活空间的边长
Island = LivingSpace(IslandSize)
SheepGroupCount = random.randint(2, IslandSize * IslandSize // 2)
WolvesGroupCount = random.randint(1,SheepGroupCount // 2)
SheepGroup = []
WolVesGroup = []
# 设置羊和狼的繁殖率
SheepIncreasing = 0.8
WolfIncreasing = 0.3

print('%s' %('=' * 20 + '捕猎开始' + '=' * 20))
print('初始羊群数量为：%d' %(SheepGroupCount))
print('初始狼群数量为：%d' %(WolvesGroupCount))

print('初始化')
for i in range(SheepGroupCount):
    pointx = random.randint(0,IslandSize - 1)
    pointy = random.randint(0,IslandSize - 1)
    while(Island.GetGrid(pointx,pointy)):
        pointx = random.randint(0, IslandSize - 1)
        pointy = random.randint(0, IslandSize - 1)
    Asheep = Sheep(Island, pointx, pointy)
    SheepGroup.append(Asheep)

for j in range(WolvesGroupCount):
    pointx = random.randint(0, IslandSize - 1)
    pointy = random.randint(0, IslandSize - 1)
    while (Island.GetGrid(pointx, pointy)):
        pointx = random.randint(0, IslandSize - 1)
        pointy = random.randint(0, IslandSize - 1)
    Awolf = Wolf(Island, pointx, pointy)
    WolVesGroup.append(Awolf)

print(Island)
# ========================初始化完成========================

# ========================开始捕猎========================
# 假定一个节拍周期内:
# 1、所有动物都移动了一遍且只能移动一遍
# 2、没有捕食到的动物饥饿度 + 1。当饥饿度 > 3时，动物死亡。（羊不考虑饥饿度）
# 3、羊和狼按设定繁殖率，第个周期都会繁殖一遍。当怀孕的羊被吃掉后，羊群扩张率会变小。

# 演化结果输出到文件中
with open(r'F:\documents\python\learning2017\program data\CatchAndRun_Result.dat', mode = 'w', encoding= 'utf-8') as outfile:
    outfile.write('%s\n' % ('=' * 20 + '捕猎开始' + '=' * 20))
    outfile.write('初始羊群数量为：%d\n' % (SheepGroupCount))
    outfile.write('初始狼群数量为：%d\n' % (WolvesGroupCount))
    outfile.write('%s' %Island)

    for AclockTime in range(100):

        SheepGroupCount = len(SheepGroup)      #两个种群在每个周期开始的数量
        WolvesGroupCount = len(WolVesGroup)

        NoMovedAnimals = SheepGroup.copy() + WolVesGroup.copy()    #所有未移动的动物集合
        # 每一周期开始，初始化羊群和狼群中怀孕的动物
        for Anum in range(int(len(SheepGroup) * SheepIncreasing)):
            SheepGroup[Anum].hasbaby = 1
        for Anum in range(int(len(WolVesGroup) * WolfIncreasing)):
            WolVesGroup[Anum].hasbaby = 1

        while(NoMovedAnimals):
            AnAnimal = random.sample(NoMovedAnimals,1)[0]         #随机选出未移动集合中的一只动物
            MovedPoint = AnAnimal.moving()
            NoMovedAnimals.remove(AnAnimal)
            if(MovedPoint):     #没有移动空间，但本轮也不能再移动了
                Island.SetGrid(AnAnimal.i, AnAnimal.j, '')

                # print('-------> %s <--------' %(Island.GetGrid(MovedPoint[0],MovedPoint[1])))
                if(AnAnimal.name == 'S'):        #如果是羊，直接移动
                    AnAnimal.i = MovedPoint[0]
                    AnAnimal.j = MovedPoint[1]
                else:              #如果是狼，要先判断是否遇到羊，如果遇到羊，吃掉羊
                    if(Island.GetGrid(MovedPoint[0],MovedPoint[1]) == 'S'):
                        AnAnimal.i = MovedPoint[0]
                        AnAnimal.j = MovedPoint[1]
                        AnAnimal.hungry = 0
                        for Asheep in SheepGroup:            #从羊群里去掉被吃掉的羊
                            # print('(%d,%d) | (%d,%d)' %(Asheep.i,Asheep.j,MovedPoint[0],MovedPoint[1]))
                            if(Asheep.i == MovedPoint[0] and Asheep.j == MovedPoint[1]):
                                # if(Asheep.hasbaby):
                                #     print('kill ******')
                                SheepGroup.remove(Asheep)
                                if(Asheep in NoMovedAnimals):
                                    NoMovedAnimals.remove(Asheep)
                                break
                    else:
                        AnAnimal.i = MovedPoint[0]
                        AnAnimal.j = MovedPoint[1]
                        AnAnimal.hungry = AnAnimal.hungry + 1
                        if (AnAnimal.hungry > 2):  # 从狼群里去掉被饿死的狼
                            WolVesGroup.remove(AnAnimal)
                            AnAnimal.name = ''
                Island.SetGrid(MovedPoint[0], MovedPoint[1], AnAnimal.name)
            else:
                if(AnAnimal.name == 'W'):
                    AnAnimal.hungry = AnAnimal.hungry + 1
                if (AnAnimal.hungry > 2):  # 从狼群里去掉被饿死的狼
                    WolVesGroup.remove(AnAnimal)
                    Island.SetGrid(AnAnimal.i, AnAnimal.j, '')

        NoOccupiedSpace = []
        for pointx in range(IslandSize):  # 统计无动物占据的空间格子
            for pointy in range(IslandSize):
                if (not Island.GetGrid(pointx, pointy)):
                    NoOccupiedSpace.append((pointx, pointy))

        # 每个种群在本周期内的死亡数量
        SheepDeathCount = SheepGroupCount - len(SheepGroup)
        WolvesDeathCount = WolvesGroupCount - len(WolVesGroup)

        outfile.write('%s 第 %d 次节拍周期 %s\n' % ('=' * 20, (AclockTime + 1), '=' * 20))
        outfile.write('<----种群新生前----> \n')
        outfile.write('原有羊群数量为：%d，其中死亡：%d, 剩余羊群数量为：%d\n' % (SheepGroupCount, SheepDeathCount,len(SheepGroup)))
        outfile.write('原有狼群数量为：%d，其中死亡：%d, 剩余狼群数量为：%d\n' % (WolvesGroupCount, WolvesDeathCount,len(WolVesGroup)))
        outfile.write('本轮移动后，无动物占据的空间格子数量为：%d\n' % (len(NoOccupiedSpace)))
        outfile.write('%s' % Island)

        # 一个周期结束后，根据剩余羊群和狼群中怀孕动物的数量，再次初始化两个种群

        NewSheepCount = 0   # 统计每个种群在本周期内的新生数量
        NewWolvesCount = 0
        HasBabiesGroup = []

        for AnAnimal in (SheepGroup + WolVesGroup):
            if(AnAnimal.hasbaby):
                HasBabiesGroup.append(AnAnimal)
        HasBabiesGroupCount = len(HasBabiesGroup)
        NoOccupiedSpaceCount = len(NoOccupiedSpace)
        if(HasBabiesGroupCount <= NoOccupiedSpaceCount):
            for NewAnimal in HasBabiesGroup:
                NewGrid = random.sample(NoOccupiedSpace, 1)[0]
                if (NewAnimal.name == 'S'):
                    SheepGroup.append(Sheep(Island, NewGrid[0], NewGrid[1]))
                    NewSheepCount += 1
                else:
                    WolVesGroup.append(Wolf(Island, NewGrid[0], NewGrid[1]))
                    NewWolvesCount += 1
                NoOccupiedSpace.remove(NewGrid)
        else:
            for NewGrid in NoOccupiedSpace:
                NewAnimal = random.sample(HasBabiesGroup, 1)[0]
                if (NewAnimal.name == 'S'):
                    SheepGroup.append(Sheep(Island, NewGrid[0], NewGrid[1]))
                    NewSheepCount += 1
                else:
                    WolVesGroup.append(Wolf(Island, NewGrid[0], NewGrid[1]))
                    NewWolvesCount += 1
                HasBabiesGroup.remove(NewAnimal)

        for AnAnimal in (SheepGroup + WolVesGroup):
            if(AnAnimal.hasbaby):
                AnAnimal.hasbaby = 0


        print('========================第 %d 次节拍周期========================' %(AclockTime + 1))
        print('羊群数量为：%d，其中死亡：%d，新生：%d' %(len(SheepGroup),SheepDeathCount,NewSheepCount))
        print('狼群数量为：%d，其中死亡：%d，新生：%d' %(len(WolVesGroup),WolvesDeathCount,NewWolvesCount))
        print(Island)

        outfile.write('<----种群新生后----> \n')
        outfile.write('羊群数量为：%d，其中死亡：%d，新生：%d\n' % (len(SheepGroup), SheepDeathCount, NewSheepCount))
        outfile.write('狼群数量为：%d，其中死亡：%d，新生：%d\n' % (len(WolVesGroup), WolvesDeathCount, NewWolvesCount))
        outfile.write('%s' %Island)



# print(LivingSpace(20))
