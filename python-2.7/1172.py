# -*- coding: utf-8 -*-

x = []
for c in range(0, 10):
    x.append(input())
    if x[c] <= 0:
        x[c] = 1
for c in range(0, 10):
    print "X[%d] = %d" %(c, x[c])