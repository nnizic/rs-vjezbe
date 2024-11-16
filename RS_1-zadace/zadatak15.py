"""
RS1
Zadatak15
Brojanje samoglasnika i suglasnika
2024.

"""


def prebroj_samoglasnike_suglasnike(tekst: str) -> dict:
    """prebrojavanje otvornika i zatvornika"""
    samoglasnici: str = "aeiouAEIOU"
    suglasnici: str = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    rezultat: dict = {"samoglasnici": 0, "suglasnici": 0}
    for slovo in tekst:
        if slovo in samoglasnici:
            rezultat["samoglasnici"] += 1
        if slovo in suglasnici:
            rezultat["suglasnici"] += 1
    return rezultat


def main() -> None:
    """glavna funkcija programa"""
    tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
    print(prebroj_samoglasnike_suglasnike(tekst))


if __name__ == "__main__":
    main()
