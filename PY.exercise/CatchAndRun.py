# -*- coding: utf-8 -*-

# 定义一个独立的动物活动空间（正方形，n * n），所有食物和捕食者都必须在这个空间中活动

import random, numpy
import pylab

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
        if( 0 <= i < self.n and 0 <= j < self.n):
            self.grid[(i,j)] = n
        else:
            self.grid[(i,j)] = -1
        return None

    def GetLivingSpaceSize(self):   #获取生活空间的大小
        return self.n

    def GetNeighbor(self,i,j,lookfortag = ''):
        NeighborGrid = []
        for istep in range(3):
            for jstep in range(3):
                if(self.GetGrid((i + istep - 1),(j + jstep - 1)) == lookfortag):
                    NeighborGrid.append(((i + istep - 1),(j + jstep - 1)))
        return NeighborGrid


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
        NoOccupiedGrid = self.livingspace.GetNeighbor(self.i, self.j)
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

    def moving(self):            #改进羊的移动，移动会朝着远离狼的区域
        NoOccupiedGrid = self.livingspace.GetNeighbor(self.i, self.j)
        if(NoOccupiedGrid):
            for Agrid in NoOccupiedGrid:
                if(not self.livingspace.GetNeighbor(Agrid[0],Agrid[1],'W')):
                    return Agrid
            return random.sample(NoOccupiedGrid, 1)[0]
        else:
            return 0

class Wolf(Animal):  #定义狼的类

    def __init__(self,livingspace,i = 0,j = 0,alive = True,hungry = 0, hasbaby = 0):
        Animal.__init__(self,livingspace,i,j,'W',alive,hungry, hasbaby)

    # 改狼的移动，移动优先会朝着有羊的区域走（2步内）
    #移动策略：1、1步内有羊，去吃羊；2、否则，2步内有羊，朝靠近羊那一格移动 3、否则，随机移动到空格。

    def moving(self):
        HaveSheepGrid = self.livingspace.GetNeighbor(self.i, self.j, 'S')
        if (HaveSheepGrid):  # 优先往有羊的地方移动
            return random.sample(HaveSheepGrid, 1)[0]
        else:
            NoOccupiedGrid = self.livingspace.GetNeighbor(self.i, self.j)
            if(NoOccupiedGrid):
                for Agrid in NoOccupiedGrid:
                    if(self.livingspace.GetNeighbor(Agrid[0],Agrid[1],'S')):
                        return Agrid
                return random.sample(NoOccupiedGrid, 1)[0]
            else:
                return 0


    # def ToEat(self):  #如果临近格子中有羊，则去吃羊，饥饿度归0
    #
    #     else:
    #         MovedGrid = 0
    #         # SheepStatus = 0
    #     return MovedGrid
    #         # self.livingspace.SetGrid(self.i, self.j, 0)
    #         # self.i = MovedGrid[0]
    #         # self.j = MovedGrid[1]
    #         # self.livingspace.SetGrid(self.i, self.j, self.name)

#定义一个模拟统计图表展示函数

def StatsGraphic(TermStats):

    xVals = numpy.array(sorted(TermStats.keys()))
    yVals1 = [TermStats[x][0] for x in xVals]
    yVals2 = [TermStats[x][1] for x in xVals]
    # print(xVals)
    # pylab.xticks(xVals, keylist, rotation = 45)
    # pylab.bar(xVals,valuelist,width = barwidth,color = 'g')
    pylab.plot(xVals, yVals1,'g',xVals,yVals2,'y')
    pylab.xlabel('TermClock')
    pylab.ylabel('AnimalsCount')
    pylab.title('green X for sheep and yellow + for wolves')
    pylab.show()

# 定义一个动物生活空间，初始化羊群和狼群的坐标位置。（狼群数量小于羊群数量）
IslandSize = 20   #定义动物生活空间的边长
Island = LivingSpace(IslandSize)
WolvesGroupCount = random.randint(1,IslandSize * IslandSize // 4)
SheepGroupCount = random.randint(WolvesGroupCount * 2, IslandSize * IslandSize - WolvesGroupCount)
# WolvesGroupCount = 10
# SheepGroupCount = 50
SheepGroup = []
WolVesGroup = []
# 设置羊和狼的繁殖率
Hungry2Death = 2   #设置狼的饥饿死亡度，每个周期饥饿度+1
#设置羊和狼的繁殖周期，每个周期+1，一旦达到或超过这个度，则可以新生羊和狼
AnimalBreed = {'S':2, 'W':5}
TermClock = 200  #设置整个模拟的周期
TermStats = {}   #设置统计数据存储

print('%s' %('=' * 20 + '捕猎开始' + '=' * 20))
print('初始羊群数量为：%d' %(SheepGroupCount))
print('初始狼群数量为：%d' %(WolvesGroupCount))

print('初始化')

while(len(SheepGroup) < SheepGroupCount):
    pointx = random.randint(0,IslandSize - 1)
    pointy = random.randint(0,IslandSize - 1)
    if(not Island.GetGrid(pointx,pointy)):
        SheepGroup.append(Sheep(Island, pointx, pointy))

while(len(WolVesGroup) < WolvesGroupCount):
    pointx = random.randint(0,IslandSize - 1)
    pointy = random.randint(0,IslandSize - 1)
    if(not Island.GetGrid(pointx,pointy)):
        WolVesGroup.append(Wolf(Island, pointx, pointy))

print(Island)
# ========================初始化完成========================

# ========================开始捕猎========================
# 假定一个节拍周期内:
# 1、所有动物都移动了一遍且只能移动一遍
# 2、没有捕食到的动物饥饿度 + 1。当饥饿度 > 3时，动物死亡。（羊不考虑饥饿度）
# 3、羊和狼按设定繁殖率，第个周期都会繁殖一遍。当怀孕的羊被吃掉后，羊群扩张率会变小。

# 演化结果输出到文件中
with open(r'F:\memory\python-learning\learning2017\program data\CatchAndRun_Result.dat', mode = 'w', encoding= 'utf-8') as outfile:
    outfile.write('%s\n' % ('=' * 20 + '捕猎开始' + '=' * 20))
    outfile.write('初始羊群数量为：%d\n' % (SheepGroupCount))
    outfile.write('初始狼群数量为：%d\n' % (WolvesGroupCount))
    outfile.write('%s' %Island)

    for AclockTime in range(TermClock):

        SheepGroupCount = len(SheepGroup)      #两个种群在每个周期开始的数量
        WolvesGroupCount = len(WolVesGroup)

        NoMovedAnimals = SheepGroup.copy() + WolVesGroup.copy()    #所有未移动的动物集合
        # # 每一周期开始，初始化羊群和狼群中怀孕的动物
        # for Anum in range(int(len(SheepGroup) * SheepIncreasing)):
        #     SheepGroup[Anum].hasbaby = 1
        # for Anum in range(int(len(WolVesGroup) * WolfIncreasing)):
        #     WolVesGroup[Anum].hasbaby = 1

        while(NoMovedAnimals):
            AnAnimal = random.sample(NoMovedAnimals,1)[0]         #随机选出未移动集合中的一只动物
            AnAnimal.hungry += 1           #每个周期，每个动物的饥饿度+1，饥饿度对羊无影响
            AnAnimal.hasbaby += 1          #每个周期，每个动物的怀孕度+1
            MovedPoint = AnAnimal.moving()
            if(MovedPoint):
                if(isinstance(AnAnimal,Sheep)):  #如果是羊，直接移动
                    Island.SetGrid(AnAnimal.i, AnAnimal.j, '')
                    AnAnimal.i = MovedPoint[0]
                    AnAnimal.j = MovedPoint[1]
                    Island.SetGrid(AnAnimal.i, AnAnimal.j, AnAnimal.name)
                else:
                    Island.SetGrid(AnAnimal.i, AnAnimal.j, '')
                    AnAnimal.i = MovedPoint[0]
                    AnAnimal.j = MovedPoint[1]
                    if(Island.GetGrid(AnAnimal.i, AnAnimal.j) == 'S'):    #如果是狼，优先判断是否有羊可吃
                        AnAnimal.hungry = 0
                        for Asheep in SheepGroup:  # 从羊群里去掉被吃掉的羊
                            # print('(%d,%d) | (%d,%d)' %(Asheep.i,Asheep.j,MovedPoint[0],MovedPoint[1]))
                            if (Asheep.i == AnAnimal.i and Asheep.j == AnAnimal.j):
                                # if(Asheep.hasbaby):
                                #     print('kill ******')
                                SheepGroup.remove(Asheep)
                                try:
                                    NoMovedAnimals.remove(Asheep)
                                except ValueError:
                                    pass
                                break
                    else:         #没有羊可吃，则往周边无动物区域移动
                        if(AnAnimal.hungry >= Hungry2Death):
                            WolVesGroup.remove(AnAnimal)
                            AnAnimal.name = ''
                    Island.SetGrid(AnAnimal.i, AnAnimal.j, AnAnimal.name)

            NoMovedAnimals.remove(AnAnimal)

        # NoOccupiedSpace = []
        # for pointx in range(IslandSize):  # 统计无动物占据的空间格子
        #     for pointy in range(IslandSize):
        #         if (not Island.GetGrid(pointx, pointy)):
        #             NoOccupiedSpace.append((pointx, pointy))

        # 每个种群在本周期内的死亡数量
        SheepDeathCount = SheepGroupCount - len(SheepGroup)
        WolvesDeathCount = WolvesGroupCount - len(WolVesGroup)

        outfile.write('%s 第 %d 次节拍周期 %s\n' % ('=' * 20, (AclockTime + 1), '=' * 20))
        outfile.write('<----种群新生前----> \n')
        outfile.write('原有羊群数量为：%d，其中死亡：%d, 剩余羊群数量为：%d\n' % (SheepGroupCount, SheepDeathCount,len(SheepGroup)))
        outfile.write('原有狼群数量为：%d，其中死亡：%d, 剩余狼群数量为：%d\n' % (WolvesGroupCount, WolvesDeathCount,len(WolVesGroup)))
        # outfile.write('本轮移动后，无动物占据的空间格子数量为：%d\n' % (len(NoOccupiedSpace)))
        outfile.write('%s' % Island)

        # 一个周期结束后，判断剩余羊群和狼群中能出生多少新动物，再次初始化两个种群。
        # 判断依据：1、羊和狼的怀孕周期达到出生度；2、达到出生度的动物周边有空白区域，如果没有，则延续出生度到下一周期。

        NewSheepCount = 0   # 统计每个种群在本周期内的新生数量
        NewWolvesCount = 0
        BreedAnimalGroup = SheepGroup.copy() + WolVesGroup.copy()
        while(BreedAnimalGroup):
            AnAnimal = random.sample(BreedAnimalGroup,1)[0]
            NewAnimalGrid = AnAnimal.moving()
            # 以下判断能否出生新动物
            if(NewAnimalGrid):
                if (AnAnimal.hasbaby >= AnimalBreed[AnAnimal.name]):
                    AnNewAnimal = AnAnimal.__class__(Island, NewAnimalGrid[0], NewAnimalGrid[1])
                    AnAnimal.hasbaby = 0
                    if(isinstance(AnAnimal,Sheep)):
                        SheepGroup.append(AnNewAnimal)
                        NewSheepCount += 1
                    else:
                        WolVesGroup.append(AnNewAnimal)
                        NewWolvesCount +=1
            BreedAnimalGroup.remove(AnAnimal)

        # print('========================第 %d 次节拍周期========================' %(AclockTime + 1))
        # print('羊群数量为：%d，其中死亡：%d，新生：%d' %(len(SheepGroup),SheepDeathCount,NewSheepCount))
        # print('狼群数量为：%d，其中死亡：%d，新生：%d' %(len(WolVesGroup),WolvesDeathCount,NewWolvesCount))
        # print(Island)

        outfile.write('<----种群新生后----> \n')
        outfile.write('羊群数量为：%d，其中死亡：%d，新生：%d\n' % (len(SheepGroup), SheepDeathCount, NewSheepCount))
        outfile.write('狼群数量为：%d，其中死亡：%d，新生：%d\n' % (len(WolVesGroup), WolvesDeathCount, NewWolvesCount))
        outfile.write('%s' %Island)

        TermStats[AclockTime] = (len(SheepGroup), len(WolVesGroup))

StatsGraphic(TermStats)

# print(LivingSpace(20))
