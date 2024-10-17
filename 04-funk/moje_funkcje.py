#!/usr/bin/env python3

IMIE = "Mat" + "eusz"

def funkcja_1(x):
    return 100 * x

def xyz(a, b):
    print("Witaj")
    return 2 * a + b

def main():
    n1 = float(input("Podaj liczbę: "))
    n2 = float(input("Podaj drugą liczbę: "))
    print(xyz(n1, n2))

if __name__ == "__main__":
    main()

