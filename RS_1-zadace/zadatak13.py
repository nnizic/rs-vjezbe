"""
RS1
Zadatak 12
Obrnuti riječnik
2024.

"""


def obrnuti_rijecnik(rijecnik: dict) -> dict:
    """zamjena ključeva i vrijednosti"""
    unosi: list = []
    kljucevi: list = []
    for unos, vrijednost in rijecnik.items():
        unosi.append(unos)
        kljucevi.append(vrijednost)
        rezultat: dict = dict(zip(kljucevi, unosi))
    return rezultat


def main() -> None:
    """glavna funkcija programa"""
    rijecnik: dict = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}
    print(obrnuti_rijecnik(rijecnik))


if __name__ == "__main__":
    main()
