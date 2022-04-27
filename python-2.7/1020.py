# -*- coding: utf-8 -*-

nd = input()
a = nd / 365
m = (nd - a * 365) / 30
d = nd - (a * 365 + m * 30)
print "%d ano(s)" %(a)
print "%d mes(es)" %(m)
print "%d dia(s)" %(d)