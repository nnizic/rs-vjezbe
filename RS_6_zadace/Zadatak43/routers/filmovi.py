""" rute za dohvat filmova """

import json
from fastapi import APIRouter


def pretvori_brojeve(data):
    """Rekurzivna funkcija, prolazi kor JSON i
    konvertira str u int ili float gdje je potrebno"""
    if isinstance(data, dict):  # ako je dict
        return {key: pretvori_brojeve(value) for key, value in data.items()}
    elif isinstance(data, list):  # ako je list
        return [pretvori_brojeve(item) for item in data]
    elif isinstance(data, str):  # ako je str, provjeri jel broj
        if data.isdigit():
            return int(data)
        try:
            return float(data)
        except ValueError:
            return data  # ako nije broj, ostavi str
    else:
        return data  # ostalo se ne mijenja


try:
    with open("filmovi_json/Film.JSON", "r", encoding="utf-8") as filmovi:
        filmovi = json.load(filmovi)
except FileNotFoundError:
    print("DAtoteka nije nađena.")

router = APIRouter(prefix="/filmovi")


@router.get("/")
def get_filmovi():
    """dohvat svih filmova"""
    parsani_filmovi = pretvori_brojeve(filmovi)
    return parsani_filmovi
