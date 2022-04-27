# -*- coding: utf-8 -*-

hi, hf = [int(x) for x in raw_input().split()]

if hi > hf:
    v = (24 + hf) - hi
    print "O JOGO DUROU %d HORA(S)" %(v)
elif hi < hf:
    v = hf - hi
    print "O JOGO DUROU %d HORA(S)" %(v)
else:
    print "O JOGO DUROU 24 HORA(S)"