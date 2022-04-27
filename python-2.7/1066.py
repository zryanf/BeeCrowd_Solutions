# -*- coding: utf-8 -*-

par = 0
impar = 0
pos = 0
neg = 0
for x in range(0,5):
    a = input()
    if a % 2 == 0:
        par = par + 1
    if a % 2 == 1:
        impar = impar + 1
    if a > 0:
        pos = pos + 1
    if a < 0:
        neg = neg + 1  
for x in range(0,1):
    print "%d valor(es) par(es)" %(par)
    print "%d valor(es) impar(es)" %(impar)
    print "%d valor(es) positivo(s)" %(pos)
    print "%d valor(es) negativo(s)" %(neg)
