""" pydantic modeli """

from pydantic import BaseModel


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
