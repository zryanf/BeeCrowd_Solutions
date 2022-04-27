# -*- coding: utf-8 -*-

A, B, C = raw_input().split()
A = float(A)
B = float(B)
C = float(C)
t = A * C / 2
c = 3.14159 * C ** 2
tr = (A + B) / 2 * C
q = B ** 2
r = A * B
print "TRIANGULO: %.3f" %(t)
print "CIRCULO: %.3f" %(c)
print "TRAPEZIO: %.3f" %(tr)
print "QUADRADO: %.3f" %(q)
print "RETANGULO: %.3f" %(r)