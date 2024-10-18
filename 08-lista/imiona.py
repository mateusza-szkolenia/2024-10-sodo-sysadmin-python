

imiona = ["Mateusz", "Michał", "Marek", "Olek"]

for n, imie in enumerate(imiona, start=1):
    print(f'{n}. {imie}')


zadania = ["x", "yy", "zz", "aaaaa", "zzzzzzz"]

for zadanie, imie in zip(zadania, imiona):
    print(imie, zadanie)

for n, (zadanie, imie) in enumerate(zip(zadania, imiona)):
    print(f"{n}: {imie} {zadanie}")
