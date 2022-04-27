# -*- coding: utf-8 -*-

N = input()
m = N - int(N)
N = int(N - m)
c = N / 100
cq = (N - (c * 100)) / 50
v = (N - (c * 100 + cq * 50)) / 20
d = (N - (c * 100 + cq * 50 + v * 20)) / 10
cc = (N - (c * 100 + cq * 50 + v * 20 + d * 10)) / 5
ds = (N - (c * 100 + cq * 50 + v * 20 + d * 10 + cc * 5)) / 2
u = N - (c * 100 + cq * 50 + v * 20 + d * 10 + cc * 5 + ds * 2)
m = int(m * 100)
mcq = m / 50
mv = (m - mcq * 50) / 25
md = (m - (mcq * 50 + mv * 25)) / 10
mc = (m - (mcq * 50 + mv * 25 + md * 10)) / 5
mu = m - (mcq * 50 + mv * 25 + md * 10 + mc * 5)
print "NOTAS:"
print "%d nota(s) de R$ 100.00" %(c)
print "%d nota(s) de R$ 50.00" %(cq)
print "%d nota(s) de R$ 20.00" %(v)
print "%d nota(s) de R$ 10.00" %(d)
print "%d nota(s) de R$ 5.00" %(cc)
print "%d nota(s) de R$ 2.00" %(ds)
print "MOEDAS:"
print "%d moeda(s) de R$ 1.00" %(u)
print "%d moeda(s) de R$ 0.50" %(mcq)
print "%d moeda(s) de R$ 0.25" %(mv)
print "%d moeda(s) de R$ 0.10" %(md)
print "%d moeda(s) de R$ 0.05" %(mc)
print "%d moeda(s) de R$ 0.01" %(mu)