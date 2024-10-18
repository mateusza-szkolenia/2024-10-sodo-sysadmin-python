#!/usr/bin/env python3

import json

WYNIK = "wynik.json"

dane = {
    "cokolwiek": [1,2,3,True,None,"qwe",45.4]
}

with open(WYNIK, "w", encoding='utf8') as plik:
    # json.dump(dane, plik, indent=2)
    json.dump(dane, plik)
