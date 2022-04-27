# -*- coding: utf-8 -*-

A, B, C = raw_input().split()
A = float(A)
B = float(B)
C = float(C)
d = B ** 2 - 4 * A * C
if d < 0 or A == 0:
    print "Impossivel calcular"
else:
    import math
    r = math.sqrt(d)
    r1 = (-1 * B + r) / (2 * A)
    r2 = (-1 * B - r) / (2 * A)
    print "R1 = %.5f" %(r1)
    print "R2 = %.5f" %(r2)