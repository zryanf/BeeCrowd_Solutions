# -*- coding: utf-8 -*-

T = input()
v = []
for x in range(0, T):
    v.append(input())
for x in range(0, T):
    n = 0
    n2 = 1
    p = 0
    while p < v[x]:
        n = n + n2
        n2 = n - n2
        p = p + 1
    print "Fib(%d) = %d" %(v[x], n)