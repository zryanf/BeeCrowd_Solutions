# -*- coding: utf-8 -*-

N = []
for x in range(0, 20):
    N.append(input())
N.reverse()
for x in range(0, 20):
    print "N[%d] = %d" %(x, N[x])