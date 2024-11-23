"""
RS2
Zadatak 4
Klase i objekti
2024.

"""

import datetime

# 1. Klasa Automobil, atributi marka, model, godina_proizvodnje i kilometraza, metoda ispis, starost


class Automobil:
    """klasa Automobil"""

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
    """klasa Kalkulator"""

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
    """klasa Student"""

    def __init__(self, ime: str, prezime: str, godine: int, ocjene: list):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self) -> float:
        """računanje prosjeka"""
        return sum(self.ocjene) / len(self.ocjene)


# 4. klasa Krug, atribut r metode opseg, povrsina
class Krug:
    """Klasa krug"""

    def __init__(self, r: float) -> None:
        self.r = r

    def opseg(self) -> float:
        """izračun opsega"""
        return 2 * self.r * 3.14

    def povrsina(self) -> float:
        """izračun površine"""
        return self.r**2 * 3.14


# 5. Klasa RAdnik, atributi ime, pozicija, placa, metoda work
class Radnik:
    """klasa radnik"""

    def __init__(self, ime: str, pozicija: str, placa: int):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self) -> str:
        """ispis pozicije"""
        return f"Radim na poziciji {self.pozicija}"


# 5.1 Klasa Manager nasljeđuje klasu Radnik uz atribut department, metode work i give_raise
class Manager(Radnik):
    """Klasa Manager"""

    def __init__(self, ime: str, pozicija: str, placa: int, department: str):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self) -> str:
        """ispis pozicije i departmenta"""
        return f"Radim na poziciji {self.pozicija} u odjelu {self.department}"

    def give_raise(self, radnik: Radnik, povecanje: int) -> str:
        """dodavanje povišice radnicima"""
        radnik.placa += povecanje
        return f"Radniku {radnik.ime} plaća je povećana za {povecanje} €."


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
    studenti_objekt = [
        Student(
            student["ime"], student["prezime"], student["godine"], student["ocjene"]
        )
        for student in studenti
    ]
    for student in studenti_objekt:
        print(f"{student.ime} ima prosjek:{student.prosjek()}")

    najbolji_student: list = list(
        filter(lambda student: student.prosjek() == 5.0, studenti_objekt)
    )
    print([[student.ime, student.prosjek()] for student in najbolji_student])

    # rad sa klasom Krug
    moj_krug: Krug = Krug(5)
    print(
        f"Opseg kruga polumjera {moj_krug.r} je {moj_krug.opseg()} a površina {moj_krug.povrsina()}"
    )

    # rad sa klasom Radnik
    radnik_Ive: Radnik = Radnik("Ive Ivić", "vratar", 2500)
    print(f"{radnik_Ive.ime} radi za plaću od {radnik_Ive.placa} € mjesečno. ")
    print(radnik_Ive.work())
    admin_Anka: Manager = Manager(
        "Anka Ankić", "financijski direktor", 3900, "gornja uprava"
    )
    print(f"{admin_Anka.ime}")
    print(admin_Anka.work())
    print(admin_Anka.give_raise(radnik_Ive, 200))

    print(f"{radnik_Ive.ime} radi za plaću od {radnik_Ive.placa} € mjesečno. ")


if __name__ == "__main__":
    main()
