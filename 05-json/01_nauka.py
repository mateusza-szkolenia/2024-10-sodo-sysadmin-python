#!/usr/bin/env python3

import json
import pprint

FILENAME = "dane.json"

with open(FILENAME, 'r', encoding='utf8') as src:
    dane = json.load(src)

for pomiar in dane['pomiary']:
    if pomiar.get('skip', False) is True:
        continue
    print(pomiar['data'])
