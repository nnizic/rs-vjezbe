"""

RS2
Zadatak 2
Funkcije višeg reda
2024.

"""

# 1. funkcijom map kvadriaj duljine
nizovi = ["jabuka", "kruška", "banana", "naranča"]
kvadrirane_duljine: list = list(map(lambda x: len(x) ** 2, nizovi))

# 2. funkcijom filter filtriraj brojeve veće od 5
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
veci_od_5: list = list(filter(lambda x: x > 5, brojevi))

# 3. kvadriranje u riječnik: ključ=org broj, vrijednost=kvadrirani broj
brojevi2 = [10, 5, 12, 15, 20]
brojevi3: list = list(map(lambda x: x**2, brojevi2))
transform: dict = dict(zip(brojevi2, brojevi3))

# 4. provjera punoljetnosti svih studenata True/False
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18},
]
svi_punoljetni: bool = all(list(map(lambda student: student["godine"] > 17, studenti)))

# 5. sve riječi iz liste dulje od minimalne duljine (7)
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
min_duljina: int = 7
duge_rijeci = list(filter(lambda rijec: len(rijec) >= min_duljina, rijeci))


def main() -> None:
    """glavna funkcija programa"""
    print(kvadrirane_duljine)
    print(veci_od_5)
    print(transform)
    print(svi_punoljetni)
    print(duge_rijeci)


if __name__ == "__main__":
    main()
