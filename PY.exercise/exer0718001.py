# -*- coding: utf-8 -*-
#
# i = 1
# while(True):
#     x = 15 * i - 1
#     if(x % 11 == 0 and x % 7 == 6 and x % 8 == 7 and x % 9 == 8):
#         print(x)
#         break
#     i += 1


# 实现一个优先级排列的队列，每次pop返回优先级最高的那元素

class PriorityQueue(object):
    def __init__(self):
        self.Queue = []

    def push(self,item,priority):
        self.Queue.append({'item':item,'priority':priority})
        self.Queue.sort(key = lambda s:s['priority'],reverse= True)
        return None

    def pop(self):
        return self.Queue.pop(0)


q = PriorityQueue()
q.push('foo',1)
q.push('cool',4)
q.push('bar',5)
q.push('spam',4)
q.push('grok',1)
q.push('fock',5)

print(q.Queue)
# print(q.Queue.pop(-1))
while(len(q.Queue) != 0):
    print(q.pop())