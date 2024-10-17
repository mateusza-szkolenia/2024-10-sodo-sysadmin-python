#!/usr/bin/env python3

"""Funkcje i lambdy"""

def o_trzy_wiecej(n):
    return n + 3

def dlugosc_imienia(imie):
    return len(imie)

def ostatnia_litera(imie):
    return imie[-1]

o_piec_wiecej = lambda n: n + 5

imiona = ['Mateusz', 'Aleksander', 'Zygmunt', 'Kuba']

print(imiona)

imiona.sort(key=ostatnia_litera)

print(imiona)

imiona.sort(key=lambda i: i[1])

print(imiona)

funkcje: list = [
    lambda x: x + 3,
    lambda x: 10 * x,
    lambda x: 100 - x,
    o_trzy_wiecej,
]

print(funkcje[3](100))
