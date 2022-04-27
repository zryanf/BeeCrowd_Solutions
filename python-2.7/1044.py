# -*- coding: utf-8 -*-

N, M = [int(x) for x in raw_input().split()]
if M % N == 0 or N % M == 0:
    print "Sao Multiplos"
else:
    print "Nao sao Multiplos"