# -*- coding: utf-8 -*-
A = input()

x = [int(x)for x in raw_input().split()]
for y in range(0,1):
    print "Menor valor:", min(x)
    print "Posicao:", x.index(min(x))