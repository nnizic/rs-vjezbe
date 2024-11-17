"""
RS1
Zadatak 10
Brojanje riječi u tekstu
2024.

"""


def brojanje_rijeci(tekst: str) -> dict:
    """funkcija za brojanje"""
    lista_tekst: list = tekst.split()
    lista_tekse_set: set = set(lista_tekst)
    duzina_liste: list = [0 for x in range(0, len(lista_tekse_set))]

    rezultat: dict = dict(zip(lista_tekse_set, duzina_liste))
    for rijec in lista_tekst:
        rezultat[rijec] += 1
    return rezultat


def main() -> None:
    """glavna funkcija programa"""
    tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
    print(brojanje_rijeci(tekst))


if __name__ == "__main__":
    main()
