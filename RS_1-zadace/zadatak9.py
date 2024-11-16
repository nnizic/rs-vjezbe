"""
RS1
Zadatak 9
jedinsktvena lista
2024.

"""


def ukloni_duplikate(lista: list) -> list:
    """jedinstveni elementi idu u skup"""
    pomocni_skup: set = set()
    for broj in lista:
        pomocni_skup.add(broj)
    rezultat: list = pomocni_skup
    return rezultat


def main() -> None:
    """glavna funkcija programa"""
    lista: list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    print(ukloni_duplikate(lista))


if __name__ == "__main__":
    main()
