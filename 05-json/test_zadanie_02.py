#!/usr/bin/env python3

import pytest
import zadanie_02

def test_haversine_Warszawa_to_Gdansk():
    warszawa = (52.0, 21.0)
    gdansk = (54.0, 18.0)

    odleglosc = zadanie_02.haversine(warszawa, gdansk)

    assert 350.0 < odleglosc < 450.0, "Zła odległość"

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
