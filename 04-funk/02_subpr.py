#!/usr/bin/env python3

import subprocess

p = subprocess.run(["ip", "address"], capture_output=True)

interfaces = []

for linia in p.stdout.decode().split("\n"):
    if linia == "":
        continue
    if linia[0].isdigit():
        interfaces.append(linia)
    # print(f"{linia}")

print(interfaces)
