""" glavna datoteka mikroservisa za filmove """

import json

filmovi = open("filmovi_json/Film.JSON")

filmovi = json.load(filmovi)


for film in filmovi:
    print(f"NAziv: {film["Title"]} , godina: {film["Year"]}")
