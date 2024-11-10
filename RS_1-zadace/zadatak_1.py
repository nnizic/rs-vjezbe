""" 
Zadatak 1.
Jednostavni kalkulator
2024.

"""


def main() -> None:
    "glavna funkcija programa"
    print("Jednostavni kalkulator(dva broja i operacija):")
    prvi_broj = float(input("Upiši prvi broj: "))
    drugi_broj = float(input("Upiši drugi broj: "))
    operacija = str(input("Izaberi operaciju(+,-,*,/)"))
    rezultat = float(0)
    printaj_me = True

    if operacija == "+":
        rezultat = prvi_broj + drugi_broj
    elif operacija == "-":
        rezultat = prvi_broj - drugi_broj
    elif operacija == "*":
        rezultat = prvi_broj * drugi_broj
    elif operacija == "/":
        if drugi_broj != 0:
            rezultat = prvi_broj / drugi_broj
        else:
            print("Dijeljenje sa nulom nije dozvoljeno!")
            printaj_me = False
    else:
        print("Nepodržani operator!")
        printaj_me = False

    if printaj_me:
        print(f"Rezultat operacije {prvi_broj} {operacija} {drugi_broj} je {rezultat}")


if __name__ == "__main__":
    main()
