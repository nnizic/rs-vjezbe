# narudzbe.py
""" narudžba proizvoda iz skladišta u proizvodi.py """
from shop import proizvodi as p


class Narudzba:
    """klasa Narudzbe"""

    def __init__(self, proizvodi: list, ukupna_cijena: float):
        self.proizvodi = proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self) -> None:
        """ispis svakog naručenog proizvoda i ukupne cijene"""
        naziv: list = [[pro["naziv"], pro["kolicina"]] for pro in self.proizvodi]

        print(f"{naziv} ukupno {self.ukupna_cijena}")


def napravi_narudzbu(proizvodi: list) -> Narudzba:
    """stvaranje narudžbi"""

    nazivi_nar: list = [pro["naziv"] for pro in proizvodi]
    nazivi_skla: list = [pro.naziv for pro in p.skladiste]
    nema_me: list = [pro for pro in nazivi_nar if pro not in nazivi_skla]

    if len(nema_me) > 0:
        print(f"Proizvoda {', '.join(nema_me)} nema na skladištu.")
        return
    if len(proizvodi) > 0:
        if isinstance(proizvodi, list) and all(
            map(lambda x: isinstance(x, dict), proizvodi)
        ):
            ukupna_cijena: float = 0
            ukupna_cijena = sum(
                proizvod["cijena"] * proizvod["kolicina"] for proizvod in proizvodi
            )
            nova_narudzba: Narudzba = Narudzba(proizvodi, ukupna_cijena)
            return nova_narudzba
        return
    return
