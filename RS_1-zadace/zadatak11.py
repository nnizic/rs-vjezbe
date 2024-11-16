"""
RS1
Zadatak 11
Elementi po paritetu
2024.

"""


def grupiraj_po_paritetu(lista: list) -> dict:
    """grupiranje parnih i neparnih brojeva"""
    rezultat: dict = {"parni": [], "neparni": []}
    for broj in lista:
        if broj % 2 == 0:
            rezultat["parni"].append(broj)
        else:
            rezultat["neparni"].append(broj)
    return rezultat


def main() -> None:
    """glavna funkcija programa"""
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(grupiraj_po_paritetu(lista))


if __name__ == "__main__":
    main()
