"""

RS2
Zadatak 3
Comprehension sintaksa
2024.

"""

# 1. lista parnih kvadrata brojeva od 20 do 50
parni_kvadrati: list = [broj**2 for broj in range(20, 51) if broj % 2 == 0]

# 2. lista duljina u listi rijeci koje sadrze slovo a
rijeci = [
    "jabuka",
    "pas",
    "knjiga",
    "zvijezda",
    "prijatelj",
    "zvuk",
    "čokolada",
    "ples",
    "pjesma",
    "otorinolaringolog",
]
duljine_sa_slovom_a: list = [len(rijec) for rijec in rijeci if "a" in rijec]

# 3.  lista riječnika ključeva 1-10, vrijednsoti kubovi za neparne, ključ za parne
kubovi: list = [{broj: broj**3 if broj % 2 != 0 else broj} for broj in range(1, 11)]

# 4. riječnik iteriranjem liste brojeva od 50 do 500 s korakom 50, ključevi brojevi, vrijednosti korijeni na 2 decimale
korijeni: dict = {broj: round(broj**0.5, 2) for broj in range(50, 501, 50)}

# 5. lista riječnika ključevi prezimena vrijednosti zbrojeni bodovi
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]},
]
zbrojeni_bodovi: list = [
    {student["prezime"]: sum(student["bodovi"])} for student in studenti
]


def main() -> None:
    """glavna funkcija programa"""
    print(parni_kvadrati)
    print(duljine_sa_slovom_a)
    print(kubovi)
    print(korijeni)
    print(zbrojeni_bodovi)


if __name__ == "__main__":
    main()
