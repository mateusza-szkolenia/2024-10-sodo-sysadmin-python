#!/usr/bin/env python3

import json

LOTNISKA = 'lotniska.json'

def wspolrzedne(napis: str) -> tuple[float, float]:
    lat, lon = map(float, napis.split(", "))
    return lat, lon

def czy_duze(lotnisko: dict) -> bool:
    return lotnisko.get('type') in ['large_airport', 'medium_airport']

def moje_lotnisko(lotnisko: dict) -> dict:
    return {
            "name": lotnisko['name'],
            "continent": lotnisko['continent'],
            "iso_country": lotnisko['iso_country'],
            "municipality": lotnisko['municipality'],
            "iata_code": lotnisko['iata_code'],
            "icao_code": lotnisko['ident'],
            "gps": wspolrzedne(lotnisko['coordinates'])
            }

if __name__ == "__main__":
    with open(LOTNISKA, 'r', encoding='utf-8') as plik:
        lotniska = json.load(plik)

    duze_lotniska = [moje_lotnisko(lotnisko)
                     for lotnisko in lotniska
                     if czy_duze(lotnisko)]

    with open("duze.json", "w") as plik:
        json.dump(duze_lotniska, plik, indent=2)
    print("Zapisano.")
