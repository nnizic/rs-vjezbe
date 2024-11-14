""" 
RS1
Zadatak 5
Računanje faktorijela
"""


def fakt_for(broj: int) -> int:
    """izračun faktorijela petljom for"""
    rezultat: int = 1
    for i in range(1, broj + 1):
        rezultat *= i
    return rezultat


def fakt_while(broj: int) -> int:
    """Izračun faktorijela petljom while"""
    rezultat: int = broj
    while broj > 1:
        broj -= 1
        rezultat *= broj
    return rezultat


def main() -> None:
    """glavna funkcija progrma"""
    broj: int = int(input("Upiši broj do kojeg računam: "))
    print("Za izračun petljom for birajte 1 ")
    print("Za izračun petljom while birajte 2 ")
    odabir: int = int(input("Vaš odabir je: "))
    if odabir == 1:
        print(f"Faktorijel broja {broj} je {fakt_for(broj)}")
    elif odabir == 2:
        print(f"Faktorijel broja {broj} je {fakt_while(broj)}")
    else:
        print("Krivi odabir")


if __name__ == "__main__":
    main()
