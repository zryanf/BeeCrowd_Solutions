# -*- coding: utf-8 -*-

import os
os.system('clear')

def imp_par(pares):
    for p in range(0,5):
        print("par[%d] = %d" %(p,pares[p]))

def imp_impar(impares):
    for p in range(0,5):
        print("impar[%d] = %d" %(p,impares[p]))

par = []
impar = []

for z in range(0,15):
    wert = int(input())
    if wert % 2 == 0:
        par.append(wert)
        if len(par) >= 5:
            imp_par(par)
            par = []
    elif wert % 2 != 0:
        impar.append(wert)
        if len(impar) >= 5:
            imp_impar(impar)
            impar = []
for i in range(0,len(impar)):
    print("impar[%d] = %d" %(i,impar[i]))
for p in range(0,len(par)):
    print("par[%d] = %d" %(p,par[p]))