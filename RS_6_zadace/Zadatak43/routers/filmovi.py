""" rute za dohvat filmova """

import re
import json
from fastapi import APIRouter, HTTPException
from models import FilmResponse


def pretvori_brojeve(data, numeric_keys: list, non_numeric_keys: list):
    """Rekurzivna funkcija, prolazi kor JSON i
    konvertira str u int ili float gdje je potrebno
    miče ' min' sa kraja Runtime, i '-' ili '-YYYY' iz Year
    Zamjena N/A u 0 kod ključeva koji trebaju biti int ili float
    blokiranje zamjene kod ključeva koji se ne smiju zamijeniti (naziv i sl)"""

    if isinstance(data, dict):  # ako je dict
        return {
            key: (
                (
                    data[key]
                    if key in non_numeric_keys
                    else pretvori_brojeve(value, numeric_keys, non_numeric_keys)
                )
                if key not in numeric_keys
                else (
                    0
                    if value == "N/A"
                    else pretvori_brojeve(value, numeric_keys, non_numeric_keys)
                )
            )
            for key, value in data.items()
        }
    elif isinstance(data, list):  # ako je list
        return [pretvori_brojeve(item, numeric_keys, non_numeric_keys) for item in data]
    elif isinstance(
        data, str
    ):  # ako je str, provjeri posebne slučajeve provjeri jel broj
        data = data.replace("–", "-")

        if "min" in data:
            try:
                return int(data.replace("min", "").strip())
            except ValueError:
                return data  # ako promijena ne uspije vrati orginal

        if re.match(r"^\d{4}-\d{0,4}$", data):  # provjera godina YYYY- ili YYYY-YYYY
            try:
                return int(data.split("-")[0])  # uzmi YYYY ispred -
            except ValueError:
                return data  # ako ne uspije vrati orginal
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


@router.get("/", response_model=list[FilmResponse])
def get_filmovi():
    """dohvat svih filmova"""
    numericki_kljucevi: list = ["Year", "Runtime", "Metascore", "imdbRating"]
    ne_numericki_kljucevi: list = ["Title"]
    parsani_filmovi = pretvori_brojeve(
        filmovi, numericki_kljucevi, ne_numericki_kljucevi
    )
    return parsani_filmovi


@router.get("/{naziv}")
def get_film(naziv: str):
    """dohvat jednog filma"""
    for film in filmovi:
        if film["Title"] == naziv:
            return film
    raise HTTPException(status_code=404, detail="Film nije pronađen.")
