#!/usr/bin/env python3

EARTH_RADIUS_KM = 6371.0

from math import radians, sin, cos, asin, sqrt

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
