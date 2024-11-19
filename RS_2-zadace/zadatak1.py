"""
RS2
Zadatak 1
Lambda izrazi
2024.

"""

# 1. kvadriranje broja
kvadriraj: int = lambda x: x**2
# 2. zbroji pa kvadriraj
zbroji_pakvadriraj: int = lambda x, y: (x + y) ** 2
# 3. kvadriraj duljinu niza
kvadriraj_duljinu: int = lambda x: len(x) ** 2
# pomnoži i potenciraj
pomnozi_i_potenciraj: int = lambda x, y: (y * 5) ** x
# True ako je paran, inače None
paran_broj: bool = lambda x: True if x % 2 == 0 else None


def main() -> None:
    """glavna funkcija programa"""
    print(kvadriraj(7))
    print(zbroji_pakvadriraj(2, 3))
    niz: list = [1, 2, 3, 4]
    print(kvadriraj_duljinu(niz))
    print(pomnozi_i_potenciraj(2, 2))
    print(paran_broj(2))
    print(paran_broj(3))


if __name__ == "__main__":
    main()
