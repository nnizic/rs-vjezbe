"""
RS1
Zadatak 8
Parna lista
2024.

"""


def filtriraj_parne(brojevi: list) -> list:
    """filtriranje samo parnih brojeva"""
    parna_lista = []
    for broj in brojevi:
        if broj % 2 == 0:
            parna_lista.append(broj)
    return parna_lista


def main() -> None:
    """glavna funkcija programa"""
    lista = list(range(1, 11))
    print(filtriraj_parne(lista))


if __name__ == "__main__":
    main()
