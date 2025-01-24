""" pydantic modeli """

from pydantic import BaseModel

# uz zadatak22


class Film(BaseModel):
    """osnovni model filma"""

    id: int
    naziv: str
    genre: str
    godina: int


class CreateFilm(BaseModel):
    """osnovni model dodavanja filma (bez id)"""

    naziv: str
    genre: str
    godina: int


# uz zadatak 32


class BaseCar(BaseModel):
    """osnovni model automobila:
    marka, model, godina_proizvodnje, cijena,boja"""

    marka: str
    model: str
    godina_proizvodnje: int
    cijena: int
    boja: str


class RequestCar(BaseCar):
    """potražni model automobila:
    marka, model, godina_proizvodnje, cijena,boja"""

    pass


class ResponseCar(BaseCar):
    """povratni model automobila:
    id, marka, model, godina_proizvodnje, cijenai, cijna_pdv,boja"""

    id: int
    cijena_pdv: float
