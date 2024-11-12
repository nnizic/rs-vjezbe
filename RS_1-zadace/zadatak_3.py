"""
RS1_Zadatak3
Igra pogađanja brojeva
2024.
"""

from random import randint


def main() -> None:
    """glavna funkcija programa"""
    trazeni_broj = randint(1, 100)
    broj_je_pogodjen = False
    counter = int(0)

    while broj_je_pogodjen == False:
        korisnikov_broj = int(input("Upiši broj: "))
        counter += 1
        if korisnikov_broj > trazeni_broj:
            print("Traženi broj je manji !")
        elif korisnikov_broj < trazeni_broj:
            print("Traženi broj je veći! ")
        else:
            print(f"Bravo, broj je pogođen u { counter } puta !")
            broj_je_pogodjen = True


if __name__ == "__main__":
    main()
