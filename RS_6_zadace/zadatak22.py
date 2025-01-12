""" Zadatak 2.2
    osnovne definicije ruta i Pydantic modela
    RS 2024/25 """

from fastapi import FastAPI

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
    return {"message": "Hello, World!"}
