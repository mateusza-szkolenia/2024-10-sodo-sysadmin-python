#!/usr/bin/env python3

def przelicz_C_na_F(temp):
    return 1.8 * temp + 32

x = float(input("Podaj temp w C: "))

x2 = przelicz_C_na_F(x)

print(f"Temp w F {x2}")
