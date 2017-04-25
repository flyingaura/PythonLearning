# -*- coding: utf-8 -*-

# list1 = [x for x in range(1,8)]
# list2 = [100,200]
# list2.extend(list1[6:3:-1])
# lista = list2
# print(list2,lista)

#方法一，直接计算位移量进行数值位移,生成新的序列
def list_move_a(nlist,k,direction = 'r'):
    moved_list = nlist[:]
    list_length = len(nlist)
    if(direction.lower() == 'l'):
        for i in range(list_length):
            if(i - k >= 0):
                moved_list[i- k] = nlist[i]
            else:
                moved_list[list_length + i - k] = nlist[i]
    else:
        for i in range(list_length):
            if(i + k <= list_length - 1):
                moved_list[i + k] = nlist[i]
            else:
                moved_list[i + k - list_length] = nlist[i]

    return moved_list

#方法二：通过对1步位移函数进行循环位移实现，改变原序列
def list_move_b(nlist,k,direction = 'r'):
    if(direction.lower() == 'l'):
        for i in range(k):
            temp = nlist[0]
            for i in range(1,len(nlist)):
                nlist[i - 1] = nlist[i]
            nlist[len(nlist) - 1] = temp
    else:
        for i in range(k):
            temp = nlist[-1]
            for i in range(len(nlist),1,-1):
                nlist[i-1] = nlist[i-2]
            nlist[0] = temp

    return None

nlist = [x for x in range(1,11)]
k = 4

# print(list_move_a(nlist,k,'l'))
# print(nlist)
print(nlist)
list_move_b(nlist,k,'l')
print(nlist)
list_move_b(nlist,k,'aa')
print(nlist)

