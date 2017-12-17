# -*- coding: utf-8 -*-

# quelist = []

#

class dequeue(list):

    def __init__(self,maxlen = None):
        self.maxlen = maxlen

    def append(self,value):
        if(self.maxlen == None):
            super(dequeue,self).append(value)
            return None
        else:
            if(len(self) < self.maxlen):
                super(dequeue, self).append(value)
                # print(self.qlist)
                return None
            else:
                super(dequeue, self).pop(0)
                super(dequeue, self).append(value)
                return None

    def appendleft(self,value):
        if (self.maxlen == None):
            super(dequeue, self).insert(0,value)
            return None
        else:
            if (len(self) < self.maxlen):
                super(dequeue, self).insert(0,value)
                # print(self.qlist)
                return None
            else:
                super(dequeue, self).insert(0,value)
                super(dequeue, self).pop(-1)
                return None

    #
    # def __str__(self):
    #     printstr = '['
    #     for i in self.qlist[:-1]:
    #         printstr = printstr + str(i) + ', '
    #     printstr = printstr + str(self.qlist[-1]) + ']'
    #     return printstr


qlist = dequeue(4)
print(type(qlist))
# print(qlist)

# print(qlist.append(1))
# qlist.append(2)
for i in range(10,3,-1):
    print(i)
    qlist.append(i)

print(qlist)
qlist.appendleft(100)
print(qlist)

print(qlist.pop(0),qlist)
# qlist = list()
# print(type(qlist))
# for i in qlist:
#     print(i)