import json
from extractor import *

with open('codes.json') as json_file:
    airports = json.load(json_file)


def extract(index):
    login()
    reach_page()
    for airport in airports:
        if airports[index] is airport:
            continue

        price = getPrice(airports[index],airport)
        print(airports[index] , ' --> ', airport,' ', price)