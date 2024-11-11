"""
Zadatak 2.
Prijestupna godina
2024

"""


def main() -> None:
    """glavna funkcija programa"""
    godina = int(input("Upiši godinu:"))
    if (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0:
        print(f"Godina {godina} je prijestupna.")
    else:
        print(f"Godina {godina} nije prijestupna.")


if __name__ == "__main__":
    main()
