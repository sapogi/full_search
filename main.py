import sys
from io import BytesIO

import requests
from PIL import Image
from geocoder import get_ll_coord, get_ll_span

toponym_to_find = 'Добринка, улица воронского'

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

delta = get_ll_span(toponym_to_find)

map_params = {
    "ll": f'{toponym_longitude},{toponym_lattitude}',
    "spn": f'{delta[0]},{delta[1]}',
    "l": "map"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)
print(get_ll_coord(toponym_to_find))
print(get_ll_span(toponym_to_find))
Image.open(BytesIO(response.content)).show()
