# -*- coding: utf-8 -*-

X = input()
N = [0]
N[0] = X
for c in range(0, 100):
    print "N[%d] = %.4f" %(c, N[c])
    N.append(N[c] / 2)