"""
RS2
Zadatak 5
Moduli i paketi
2024.

"""

from shop import proizvodi as p

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
    p.proizvodi.append(pro)


def main() -> None:
    """glavna funkcija programa"""
    print([proizvod.ispis() for proizvod in p.proizvodi])


if __name__ == "__main__":
    main()
