# -*- coding: utf-8 -*-

N = input()
c = N / 100
cq = (N - (c * 100)) / 50
v = (N - (c * 100 + cq * 50)) / 20
d = (N - (c * 100 + cq * 50 + v * 20)) / 10
cc = (N - (c * 100 + cq * 50 + v * 20 + d * 10)) / 5
ds = (N - (c * 100 + cq * 50 + v * 20 + d * 10 + cc * 5)) / 2
u = N - (c * 100 + cq * 50 + v * 20 + d * 10 + cc * 5 + ds * 2)
print N
print "%d nota(s) de R$ 100,00" %(c)
print "%d nota(s) de R$ 50,00" %(cq)
print "%d nota(s) de R$ 20,00" %(v)
print "%d nota(s) de R$ 10,00" %(d)
print "%d nota(s) de R$ 5,00" %(cc)
print "%d nota(s) de R$ 2,00" %(ds)
print "%d nota(s) de R$ 1,00" %(u)