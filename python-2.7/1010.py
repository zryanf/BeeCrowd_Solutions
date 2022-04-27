# -*- coding: utf-8 -*-

c, n, v = raw_input().split()
c2, n2, v2 = raw_input().split()
t = int(n) * float(v) + int(n2) * float(v2)
print "VALOR A PAGAR: R$ %.2f" %(t)