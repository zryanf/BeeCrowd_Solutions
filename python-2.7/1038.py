# -*- coding: utf-8 -*-

c, q = raw_input().split()
c = int(c)
q = int(q)
if c == 1:
    t = 4.0 * q
elif c == 2:
    t = 4.5 * q
elif c == 3:
    t = 5.0 * q
elif c == 4:
    t = 2.0 * q
else:
    t = 1.5 * q
print "Total: R$ %.2f" %(t)