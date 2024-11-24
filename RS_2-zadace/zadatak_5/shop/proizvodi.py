# proizvodi.py
""" skladište proizvoda """


class Proizvod:
    """klasa Proizvod"""

    def __init__(self, naziv: str, cijena: int, kolicina: int):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self) -> str:
        """ispis atributa proizvoda"""
        return f"Proizvod {self.naziv}, cijena {self.cijena}, količina {self.kolicina}"


skladiste: list = [Proizvod("Slušalice", 100, 25), Proizvod("Zvučnici", 250, 10)]


def dodaj_proizvod(naziv: str, cijena: int, kolicina: int) -> None:
    """dodaje proizvod u listu proizvodi"""
    skladiste.append(Proizvod(naziv, cijena, kolicina))
