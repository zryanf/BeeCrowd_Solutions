# -*- coding: utf-8 -*-

a, b, c = raw_input().split()
a = int(a)
b = int(b)
c = int(c)
MaiorAB = (a + b + abs(a - b)) / 2
MaiorAB = (MaiorAB + c + abs(MaiorAB - c)) / 2
print "%d eh o maior" %(MaiorAB)