""" Obrada grešaka - automobili """

from fastapi import FastAPI, HTTPException, status, Query
from models import ResponseCar, RequestCar

app = FastAPI()


automobili = [
    {
        "id": 1,
        "marka": "Honda",
        "model": "civic",
        "godina_proizvodnje": 1982,
        "cijena": 2100,
        "cijena_pdv": 2100 * 1.25,
        "boja": "plava",
    },
    {
        "id": 2,
        "marka": "Alfa Romeo",
        "model": "33",
        "godina_proizvodnje": 1990,
        "cijena": 2500,
        "cijena_pdv": 2500 * 1.25,
        "boja": "zelena",
    },
]


@app.get("/automobili", response_model=list)
def dohvati_automobile():
    """dohvat svih automobila"""
    return automobili


@app.get("/automobili/{id}", response_model=ResponseCar)
def dohvati_automobil(id: int):
    """dohvat jednog automobila"""
    for auto in automobili:
        if auto["id"] == id:
            return auto
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Automobil sa id-em {id} nije pronađen.",
    )


@app.post("/automobili", response_model=ResponseCar)
def dodaj_automobil(automobil: RequestCar):
    """dodavanje automobila"""
    PDV: float = 1.25
    new_id = automobili[-1]["id"] + 1
    cijena_pdv: float = automobil.cijena * PDV
    automobil_za_pohranu: ResponseCar = {
        **automobil.model_dump(),
        "id": new_id,
        "cijena_pdv": cijena_pdv,
    }
    automobili.append(automobil_za_pohranu)
    return automobil_za_pohranu


@app.get("/automobili/pretraga/", response_model=list[ResponseCar])
def dohvati_birane_automobile(
    min_cijena: int = Query(0, ge=1),
    max_cijena: int = Query(0, ge=1),
    min_godina: int = Query(1960, ge=1961, le=2024),
    max_godina: int = Query(1960, ge=1961, le=2025),
):
    """dohvat automobila prema paramterima query-a"""
    if min_cijena > max_cijena:
        raise HTTPException(
            status_code=400, detail="minimalna cijena mora biti manja od maksimalne"
        )
    if min_godina > max_godina:
        raise HTTPException(
            status_code=400,
            detail="Minimalni broj godina mora biti manji od maksimalnog.",
        )
    filtrirana_vozila: list = []
    for auto in automobili:
        if (
            auto["godina_proizvodnje"] >= min_godina
            and auto["godina_proizvodnje"] <= max_godina
            and auto["cijena"] >= min_cijena
            and auto["cijena"] <= max_cijena
        ):
            filtrirana_vozila.append(auto)

    return filtrirana_vozila
