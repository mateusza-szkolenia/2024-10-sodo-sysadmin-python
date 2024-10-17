#!/usr/bin/env python3

import os
from datetime import datetime

s = os.stat("pliczek.txt")

d = datetime.fromtimestamp(s.st_mtime)

print(s)
print(d)
