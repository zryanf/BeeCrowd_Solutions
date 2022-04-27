# -*- coding: utf-8 -*-

X = int(input())
if X %2 != 0:
    X = X + 1

for x in range(1,X):
    if x % 2 != 0:
        print(x)