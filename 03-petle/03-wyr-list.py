#!/usr/bin/env python3

from pprint import pprint

linie_pliku = """Pierwsza linia
druga linia
trzecia linia

piąta linia

siódma linia
ósma linia""".split("\n")

pprint(linie_pliku)

linie = [ f"treść: [[ {x} ]]" for x in linie_pliku]

pprint(linie)

linie = [len(x)
         for x in linie_pliku
         if x != ""]

pprint(linie)

linie = []
for x in linie_pliku:
    if x != "":
        linie.append(len(x))
pprint(linie)


