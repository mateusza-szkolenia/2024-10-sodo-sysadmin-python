#!/usr/bin/env python3

DANE = 'dane.yaml'

import yaml

dane = yaml.safe_load(open(DANE))

txt = yaml.dump(dane, allow_unicode=True)

print(txt)
