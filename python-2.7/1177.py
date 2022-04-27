# -*- coding: utf-8 -*-

T = input()
N = []
c = 0
for x in range(0, 1000):
    N.append(c)
    c = c + 1
    if c == T:
        c = 0
for x in range(0, 1000):
    print "N[%d] = %d" %(x, N[x])