""" Obrada grešaka - automobili """

from fastapi import FastAPI, HTTPException, status
from models import BaseCar

app = FastAPI()


automobili = [
    {
        "id": 1,
        "marka": "Honda",
        "model": "civic",
        "godina_proizvodnje": 1982,
        "cijena": 2100,
        "boja": "plava",
    },
    {
        "id": 2,
        "marka": "Alfa Romeo",
        "model": "33",
        "godina_proizvodnje": 1990,
        "cijena": 2500,
        "boja": "zelena",
    },
]


@app.get("/automobili", response_model=list)
def dohvati_automobile():
    """dohvat svih automobila"""
    return automobili


@app.get("/automobili/{id}", response_model=BaseCar)
def dohvati_automobil(id: int):
    """dohvat jednog automobila"""
    for auto in automobili:
        if auto["id"] == id:
            return auto
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Automobil sa id-em {id} nije pronađen.",
    )
