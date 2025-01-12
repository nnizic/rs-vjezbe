""" Zadatak 2.2
    osnovne definicije ruta i Pydantic modela
    RS 2024/25 """

from fastapi import FastAPI
from models import Film, CreateFilm

app = FastAPI()

filmovi = [
    {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
    {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
    {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
    {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008},
]


@app.get("/")
def read_root():
    """osnovna ruta"""
    return {"message": "Baza filmova"}


@app.get("/filmovi")
def get_films():
    """dohvat svih filmova"""
    return filmovi


@app.get("/filmovi/{id}", response_model=Film)
def get_film(id: int):
    """pretraga filma prema poziciji u bazi"""
    pronadjeni_film = next((film for film in filmovi if film["id"] == id), None)
    return pronadjeni_film


@app.get("/filmovi/")
def get_film_by_query(genre: str = None, min_year: int = 2000):
    """dohvat filma prema žanru i starosti"""
    pronadjeni_filmovi = [
        film
        for film in filmovi
        if film["genre"] == genre and film["godina"] >= min_year
    ]
    return pronadjeni_filmovi


@app.post("/filmovi")
def add_film(film: CreateFilm):
    """dodavanje filma u bazu"""
    new_id = len(filmovi) + 1
    film_s_id = Film(id=new_id, **film.model_dump())
    filmovi.append(film_s_id.model_dump())
    return film_s_id
