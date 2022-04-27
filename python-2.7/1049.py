# -*- coding: utf-8 -*-

genero = raw_input()
especie = raw_input()
individuo = raw_input()

if genero == "vertebrado":
    if especie == "ave":
        if individuo == "carnivoro":
            print "aguia"
        elif individuo == "onivoro":
            print "pomba"

    if especie == "mamifero":
        if individuo == "onivoro":
            print "homem"
        elif individuo == "herbivoro":
            print "vaca"
elif genero == "invertebrado":
    if especie == "inseto":
        if individuo == "hematofago":
            print "pulga"
        elif individuo == "herbivoro":
            print "lagarta"

    if especie == "anelideo":
        if individuo == "hematofago":
            print "sanguessuga"
        elif individuo == "onivoro":
            print "minhoca"