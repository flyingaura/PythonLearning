# -*- coding: utf-8 -*-

from LearnModule import cal_date
import random

InterValDays = 30
initDate = 20171114
DateList = []
SearchCounts = []
ViewCounts = []
SpiecialCounts = []
for i in range(abs(InterValDays)):
    # j = 0 - i
    Adate = cal_date.Cal_Data(initDate,i)
    DateList.append(Adate[:4] + '-' + Adate[4:6] + '-' + Adate[6:])
    SearchCounts.append(random.randint(10,150))
    ViewCounts.append(random.randint(10,300))
    SpiecialCounts.append(random.randint(1,100))

print(DateList)
print(SearchCounts)
print(ViewCounts)
print(SpiecialCounts)
