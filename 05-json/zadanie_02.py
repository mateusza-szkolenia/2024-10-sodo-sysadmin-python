#!/usr/bin/env python3

DANE = "duze.json"

EARTH_RADIUS_KM = 6371.0

import json
from math import radians, sin, cos, asin, sqrt

class LotniskoNotFound(Exception):
    """Nie znaleziono lotniska"""


def haversine(coords1: tuple[float, float], coords2: tuple[float, float]) -> float:
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    lon1, lat1 = coords1
    lon2, lat2 = coords2
    
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = EARTH_RADIUS_KM
    return c * r

def odleglosc_miedzy_lotniskami(lotnisko1: dict, lotnisko2: dict) -> float:
    """Odległość między lotniskami"""

    return haversine(lotnisko1['gps'], lotnisko2['gps'])

def odleglosc_miedzy_lotniskami_wg_nazwy(lot1: str, lot2: str) -> float:
    """Odległość między lotniskami wg nazw"""

    lotnisko1 = znajdz_lotnisko(lot1)
    lotnisko2 = znajdz_lotnisko(lot2)

    return odleglosc_miedzy_lotniskami(lotnisko1, lotnisko2)

def znajdz_lotnisko(nazwa: str) -> dict:
    """Znajdź w "bazie danych" lotnisko o danym kodzie"""

    for lotnisko in LOTNISKA:
        if nazwa in [lotnisko['iata_code'], lotnisko['icao_code']]:
            return lotnisko
    raise LotniskoNotFound

def lotniska_w_promieniu(lotnisko: dict, promien: float) -> list[dict]:
    """Znajdź lotniska w danym promieniu"""

    wynik = []

    for spr_lot in LOTNISKA:
        odleglosc = odleglosc_miedzy_lotniskami(lotnisko, spr_lot)
        if odleglosc <= promien:
            wynik.append(spr_lot)
    return wynik

LOTNISKA = json.load(open(DANE, 'r', encoding='utf-8'))
