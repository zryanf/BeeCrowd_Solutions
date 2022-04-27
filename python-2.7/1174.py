# -*- coding: utf-8 -*-

A = []
for x in range(0, 100):
    A.append(input())
for x in range(0, 100):
    if A[x] <= 10:
        print "A[%d] = %.1f" %(x, A[x])