#!/usr/bin/env python3

def przelicz_C_na_F(temp: float) -> float:
    """Funkcja przelicza temperaturę ze st. C na F"""
    return 1.8 * temp + 32

x = float(input("Podaj temp w C: "))

x2 = przelicz_C_na_F(x)

print(f"Temp w F {x2}")

x3 = przelicz_C_na_F(10.0)

x4 = przelicz_C_na_F()

print(x3, x4)
