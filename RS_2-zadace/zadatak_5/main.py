"""
RS2
Zadatak 5
Moduli i paketi
2024.

"""

from shop import proizvodi as p
from shop import narudzbe as n

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100},
]

pproizvodi = [
    p.Proizvod(proizvod["naziv"], proizvod["cijena"], proizvod["kolicina"])
    for proizvod in proizvodi
]
for pro in pproizvodi:
    p.skladiste.append(pro)


def main() -> None:
    """glavna funkcija programa"""
    print([proizvod.ispis() for proizvod in p.skladiste])

    proizvodi_zanarudzbu: list = [
        {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 10},
        {"naziv": "Miš", "cijena": 100, "kolicina": 15},
    ]
    naruceni_proizvodi: n.Narudzba = n.napravi_narudzbu(proizvodi_zanarudzbu)
    if isinstance(naruceni_proizvodi, n.Narudzba):
        naruceni_proizvodi.ispis_narudzbe()
    else:
        print("Narudžba nije uspjela.")


if __name__ == "__main__":
    main()
