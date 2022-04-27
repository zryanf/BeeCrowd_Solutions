# -*- coding: utf-8 -*-

X = int(input())
 
if X % 2 == 0:
    X += 1
    for Y in range(0,11,2):
        Z = X + Y
        print (Z)
else:
    for Y in range(0,11,2):
        Z = X + Y
        print (Z)