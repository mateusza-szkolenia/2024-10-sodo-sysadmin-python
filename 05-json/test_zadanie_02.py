#!/usr/bin/env python3

import pytest
import zadanie_02

ODLEGLOSCI = [
    ((52.0, 21.0), (54.0, 18.0), 340.0),
    ((52.5, 13.5), (52.0, 21.0), 800.0),
]

def test_haversine_Warszawa_to_Gdansk():
    warszawa = (52.0, 21.0)
    gdansk = (54.0, 18.0)

    odleglosc = zadanie_02.haversine(warszawa, gdansk)

    assert 350.0 < odleglosc < 450.0, "Zła odległość"

@pytest.mark.parametrize("a,b,est_dist", ODLEGLOSCI)
def test_haversine_A_to_B(a: tuple[float, float], b: tuple[float, float], est_dist: float):

    odleglosc = zadanie_02.haversine(a, b)

    assert est_dist * 0.8 < odleglosc < est_dist * 1.2

def test_haversine_return_type():
    warszawa = (52.0, 21.0)
    gdansk = (54.0, 18.0)

    wynik = zadanie_02.haversine(warszawa, gdansk)

    assert isinstance(wynik, float), "Zły typ zwracany"

def test_haversine_wrong_args():

    with pytest.raises(ValueError):
        wynik = zadanie_02.haversine("warszawa", "gdansk")

def test_haversine_wrong_args2():

    with pytest.raises(TypeError):
        wynik = zadanie_02.haversine("XX", "YY")

def test_odleglosc_miedzy_lotniskami_WAW_GDN():
    lot1 = {
        "name": "Warsaw Chopin Airport",
        "continent": "EU",
        "iso_country": "PL",
        "municipality": "Warsaw",
        "iata_code": "WAW",
        "icao_code": "EPWA",
        "gps": [
        52.165699,
        20.9671
        ]
    }

    lot2 =   {
        "name": "Gdansk airport",
        "continent": "EU",
        "iso_country": "PL",
        "municipality": "Gdańsk",
        "iata_code": "GDN",
        "icao_code": "EPGD",
        "gps": [
        54.377602,
        18.4662
        ]
    }

    odleglosc = zadanie_02.odleglosc_miedzy_lotniskami(lot1, lot2)

    assert 300.0 < odleglosc < 500.0

def test_znajdz_lotnisko_WAW():
    lotnisko = zadanie_02.znajdz_lotnisko("WAW")

    assert isinstance(lotnisko, dict)
    assert lotnisko['iata_code'] == "WAW"

def test_znajdz_lotnisko_EPWA():
    lotnisko = zadanie_02.znajdz_lotnisko("EPWA")

    assert isinstance(lotnisko, dict)
    assert lotnisko['iata_code'] == "WAW"

def test_znajdz_nieistniejace_lotnisko():
    with pytest.raises(zadanie_02.LotniskoNotFound):
        zadanie_02.znajdz_lotnisko("XYZ")

def test_odleglosc_miedzy_lotniskami_wg_nazwy_WAW_GDN():

    odleglosc = zadanie_02.odleglosc_miedzy_lotniskami_wg_nazwy("WAW", "GDN")

    assert 300.0 < odleglosc < 500.0

def test_lotniska_w_promieniu_1000_od_WAW():
    lotnisko = zadanie_02.znajdz_lotnisko("WAW")
    lotniska = zadanie_02.lotniska_w_promieniu(lotnisko, 1000.0)

    assert len(lotniska) > 1, "Za mało"
    assert len(lotniska) < len(zadanie_02.LOTNISKA), "Wszystkie"

def test_lotniska_w_promieniu_100_od_WAW():
    lotnisko = zadanie_02.znajdz_lotnisko("WAW")
    lotniska = zadanie_02.lotniska_w_promieniu(lotnisko, 100.0)

    assert len(lotniska) == 4, "Zła liczba"
