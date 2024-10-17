#!/usr/bin/env python3

"""
Zadanie 1

Napisać program podający uptime systemu w godzinach, z dokładnością do dziesiątej części.

Użyć danych z /proc/uptime
"""

plik = open("/proc/uptime")

zawartosc = plik.read()

a, b = zawartosc.split(" ")

czas_w_sek = int(float(a))

czas_w_godz = float(a) / 3600

godz, minu, sek = czas_w_sek // 3600, (czas_w_sek % 3600) // 60, czas_w_sek % 60

print(f"{czas_w_godz:.1f}")

print(f"{godz}:{minu}:{sek}")
