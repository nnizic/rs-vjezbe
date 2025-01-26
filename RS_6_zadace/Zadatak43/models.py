""" pydantic scheme za filmove  """

from typing import Literal, Optional
from pydantic import BaseModel, Field


class Person(BaseModel):
    """osnova za osobe koje rade na filmu (name, surname)"""

    name: str
    surname: str


class Actor(Person):
    """glumac: name, surname"""

    pass


class Director(Person):
    """redatelj: name, surname"""

    pass


class Writer(Person):
    """pisac: name, surname"""

    pass


class Film(BaseModel):
    """osnovi model za film"""

    Title: str
    Rated: str
    Genre: str
    Language: str
    Country: str
    Actors: str
    Plot: str
    Writer: str
    Images: list[str]
    Type: Literal["movie", "series"]
    # neobavezni - zadanih vrijednosti
    Released: str = Field(default="undefined")
    Awards: str = Field(default="0 wins & 0 nominations.")
    Poster: str = Field(default="undefined")
    imdbVotes: str = Field(default="undefined")
    imdbID: str = Field(default="undefined")
    Response: str = Field(default="undefined")


class FilmResponse(Film):
    """schema za dohvat filma"""

    ComingSoon: Optional[bool] = False
    totalSeasons: Optional[int] = 0
    Year: int
    imdbRating: float
    Metascore: float
    Runtime: int
