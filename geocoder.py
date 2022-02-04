import requests


def geocode(address):
    toponym_to_find = address
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}
    response = requests.get(geocoder_api_server, params=geocoder_params).json()
    ll = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
    return ll


def get_ll_coord(addsress):
    ll = geocode(addsress)['Point']['pos']
    return float(ll.split(' ')[0]), float(ll.split(' ')[1])

def get_ll_span(address):
    toponym = geocode(address)
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    envelope = toponym["boundedBy"]["Envelope"]
    l, b = envelope["lowerCorner"].split(" ")
    r, t = envelope["upperCorner"].split(" ")
    dx = abs(float(l) - float(r)) / 2.0
    dy = abs(float(t) - float(b)) / 2.0

    return dx, dy
