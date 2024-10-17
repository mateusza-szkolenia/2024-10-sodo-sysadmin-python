#!/usr/bin/env python3

plik = open("imie.txt", encoding='utf8')

zawartosc = plik.read()
imie = zawartosc.strip()

print(f"{plik = } {zawartosc = } {imie = }")
print(f"{len(imie)}")
