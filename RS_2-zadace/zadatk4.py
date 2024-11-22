"""
RS2
Zadatak 4
Klase i objekti
2024.

"""

import datetime

# 1. Klasa Automobil, atributi marka, model, godina_proizvodnje i kilometraza, metoda ispis, starost


class Automobil:
    def __init__(
        self, marka: str, model: str, godina_proizvodnje: int, kilometraza: int
    ):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self) -> str:
        """ispis svih atributa klase"""
        return f"Vozilo marke {self.marka}, model {self.model}, proizvedeno je {self.godina_proizvodnje} i ima {self.kilometraza} kilometara."

    def starost(self) -> str:
        """Ispis starosti vozila"""
        trenutna_godina: int = (datetime.date.today()).year
        return f"Starost vozila je {trenutna_godina - self.godina_proizvodnje} godine"


# 2. KLasa Kalkulator, atributi a i b, metode zbroj, oduzimanje, mnozenje, dijeljenje, potenciranje i korijen


class Kalkulator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def zbroj(self) -> str:
        """a+b"""
        return f" Rezultat je: {self.a+self.b}"

    def oduzimanje(self) -> str:
        """a-b"""
        return f" Rezultat je: {self.a-self.b}"

    def mnozenje(self) -> str:
        """a*b"""
        return f" Rezultat je: {self.a*self.b}"

    def dijeljenje(self) -> str:
        """a/b"""
        if self.b == 0:
            return "NEMA DIJELJENJA SA NULOM"
        return f" Rezultat je: {self.a/self.b}"

    def potenciranje(self) -> str:
        """a**2 b**2"""
        return f" Rezultat je: {self.a**2} i  {self.b**2}"

    def korijen(self) -> str:
        """a**0.5 b**0.5"""
        return f" Rezultat je: {self.a**0.5} i  {self.b**0.5}"


# 3. klasa Student, atributi ime, prezime, godine, ocjene, metoda prosjek
class Student:
    def __init__(self, ime: str, prezime: str, godine: int, ocjene: list):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self) -> float:
        zbroj_ocjena: int = 0
        for ocjena in self.ocjene:
            zbroj_ocjena += ocjena
        return zbroj_ocjena / len(self.ocjene)


def main() -> None:
    """glavna funkcija programa"""
    # rad sa klasom Automobil
    moj_auto = Automobil("honda", "civic 1.3", 1982, 123000)
    print(moj_auto.starost())
    print(moj_auto.ispis())

    # rad sa klasom Kalkulator
    mojkalkulator = Kalkulator(3, 2)
    print(mojkalkulator.zbroj())
    print(mojkalkulator.oduzimanje())
    print(mojkalkulator.mnozenje())
    print(mojkalkulator.dijeljenje())
    print(mojkalkulator.potenciranje())
    print(mojkalkulator.korijen())

    moj_los_kalkulator = Kalkulator(4, 0)
    print(moj_los_kalkulator.dijeljenje())

    # Rad sa klasom Student
    studenti = [
        {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
        {
            "ime": "Marko",
            "prezime": "Marković",
            "godine": 22,
            "ocjene": [3, 4, 5, 2, 3],
        },
        {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
        {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
        {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
        {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]},
    ]
    studenti_objekt = []
    for student in studenti:
        studenti_objekt.append(
            Student(
                student["ime"], student["prezime"], student["godine"], student["ocjene"]
            )
        )
    for student in studenti_objekt:
        print(f"{student.ime} ima prosjek:{student.prosjek()}")

    najbolji_student: list = list(
        filter(lambda student: student.prosjek() == 5.0, studenti_objekt)
    )
    for student in najbolji_student:
        print(student.ime)


if __name__ == "__main__":
    main()
