# -*- coding: utf-8 -*-

def fib(n):
    a = 1
    b = 1
    L = []
    L.append(1)
    for x in range(n-1):
        L.append(a)
        # L.append(b)
        temp = a
        a = a + b
        b = temp
    return L

print(list(fib(10)))
