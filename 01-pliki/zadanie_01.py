#!/usr/bin/env python3

"""
Zadanie 1

Napisać program podający uptime systemu w godzinach, z dokładnością do dziesiątej części.

Użyć danych z /proc/uptime
"""

plik = open("/proc/uptime")

zawartosc = plik.read()

a, b = zawartosc.split(" ")

czas_w_godz = float(a) / 3600

print(czas_w_godz)

