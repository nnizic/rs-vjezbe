""" definicija složenih pydantic modela """

from typing import TypedDict, Optional, Literal
from datetime import datetime
from pydantic import BaseModel


# zadatak 1
class Izdavac(TypedDict):
    """izdavač: naziv, adresa"""

    naziv: str
    adresa: str


TRENUTAK = datetime.now()


class Knjiga(BaseModel):
    """knjiga: naslov, ime_autor, prezime_autor, god_izdavanja, br_stranica, izdavac"""

    naslov: str
    ime_autor: str
    prezime_autor: str
    god_izdavanja: Optional[int] = int(TRENUTAK.year)
    br_stranica: int
    izdavac: Izdavac


# test zadatka 1
knjiga: Knjiga = Knjiga(
    naslov="Soneti",
    ime_autor="William",
    prezime_autor="Shakespeare",
    br_stranica=130,
    izdavac={"naziv": "penguin publishing ltd", "adresa": "London, London, UK"},
)
print(knjiga)


# zadatak 2
class Admin(BaseModel):
    """admin:ime, prezime, email, ovlasti(dodavanje, brisanje, ažuriranje, čitanje)"""

    ime: str
    prezime: str
    email: str
    ovlasti: Literal["dodavanje", "brisanje", "azuriranje", "citanje"] = []


# test zadtka 2
superkorisnik: Admin = Admin(
    ime="Pero", prezime="Perić", email="peroper@orjtsag.it", ovlasti="citanje"
)

print(superkorisnik)


# zadatak 3
class Jelo(TypedDict):
    """jelo: id, naziv, cijena"""

    id: int
    naziv: str
    cijena: float


class Stol(TypedDict):
    """stol: broj, lokacija"""

    broj: int
    lokacija: str


class RestaurantOrder(BaseModel):
    """restoranska narudžba: id,ime_kupca, stol_info, lista_jela, ukupna_cijena"""

    id: int
    ime_kupca: str
    stol_info: Stol
    lista_jela: list[Jelo]


# test zadatka 3
narudzba: RestaurantOrder = RestaurantOrder(
    id=1,
    ime_kupca="Ivo pl Ivich",
    stol_info={"broj": 2, "lokacija": "podrum"},
    lista_jela=[
        {"id": 1, "naziv": "zubatac na lešo", "cijena": 200},
        {"id": 2, "naziv": "zečji bubreg u umaku od zelenog papra", "cijena": 160},
    ],
)


print(narudzba)


# Zadatak 4
class CCTV_frame(BaseModel):
    """CCTV: id, vrijeme_snimanja, koordinate(x,y)"""

    id: int
    vrijeme_snimanja: datetime
    koordinate: tuple[float, float] = (0, 0)


# test zadatka 4
cctv_frame: CCTV_frame = CCTV_frame(
    id=1, vrijeme_snimanja=TRENUTAK, koordinate=(16.15, 45.01)
)
print(cctv_frame)
