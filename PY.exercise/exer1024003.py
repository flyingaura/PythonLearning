# -*- coding: utf-8 -*-

class Clock(object):

    def __init__(self,hours = 0,mins = 0,seconds = 0):
        if(isinstance(hours,int) and isinstance(mins,int) and isinstance(seconds,int)):
            self.seconds = seconds
            self.mins = mins
            self.hours = hours
            while(self.seconds >= 60):
                self.seconds = self.seconds - 60
                self.mins = self.mins + 1
            while(self.mins >= 60):
                self.mins = self.mins - 60
                self.hours = self.hours + 1
            while(self.hours >= 24):
                self.hours = self.hours - 24
        else:
            self.seconds = 0
            self.mins = 0
            self.hours = 0

    def __add__(self,ClockB):
        if(not isinstance(ClockB,Clock)):
            ClockB = Clock(ClockB)
        return Clock(self.hours + ClockB.hours, self.mins + ClockB.mins, self.seconds + ClockB.seconds)

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return ('Time is %02d:%02d:%02d' %(self.hours,self.mins,self.seconds))

# ClockA = Clock(32,60,149)
ClockB = 6.6
ClockA = Clock(29,93,3)
print(ClockA)
print(ClockB)
print(ClockA + ClockB)
print(ClockB + ClockA)