# -*- coding: utf-8 -*-

N = [0]
N[0] = input()
for x in range(0, 10):
    N.append(N[x] * 2)
for x in range(0, 10):
    print "N[%d] = %d" %(x, N[x])