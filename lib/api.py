# -*- coding: utf-8 -*-

import requests


GOOGLE_GEOCODE_API_URL = "https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyBflv1wp3O6qIB9ZL3x88bWTjiOeZnI5Kw"


def convert_address_to_latlng(address):
    url = GOOGLE_GEOCODE_API_URL + "&address=" + address
    res = requests.get(url)
    
    lat = res.json()["results"][0]["geometry"]["location"]["lat"]
    lng = res.json()["results"][0]["geometry"]["location"]["lng"]
    return [lat, lng]
