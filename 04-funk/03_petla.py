#!/usr/bin/env python3

import time

x = 1.0

while True:
    print("#" * int(x))
    x *= 1.2 # x = x * 1.2
    time.sleep(1)
