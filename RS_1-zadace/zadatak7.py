""" 
RS1
Zadatak 7
Provjera lozinke
2024.

"""


def duljina_lozinke(lozinka: str) -> bool:
    """provjera dužine lozinke"""
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
        return False
    return True


def zabranjene_rijeci(lozinka: str) -> bool:
    """provjera zabranjenih riječi"""
    lozinka = lozinka.lower()
    if lozinka in ("password", "lozinka"):
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        return False
    return True


def slova_i_brojke(lozinka: str) -> bool:
    """provjera malih-velikih slova i brojki"""
    set_lozinka = set(lozinka)
    ima_malo_slovo: bool = False
    ima_veliko_slovo: bool = False
    ima_broj: bool = False
    for slovo in set_lozinka:
        if slovo.islower():
            ima_malo_slovo = True
        if slovo.isupper():
            ima_veliko_slovo = True
        if slovo.isdigit():
            ima_broj = True
    if ima_malo_slovo and ima_veliko_slovo and ima_broj:
        return True
    print("Lozinka mora sadržavati barem jedno malo slovo, veliko slovo i broj")
    return False


def provjera_lozinke(lozinka: str) -> None:
    """glavna provjera lozinke"""
    if (
        duljina_lozinke(lozinka)
        and zabranjene_rijeci(lozinka)
        and slova_i_brojke(lozinka)
    ):
        print("Lozinka je jaka")


def main() -> None:
    """glavna funkcija programa"""
    korisnicka_lozinka: str = input("Upiši lozinku: ")
    provjera_lozinke(korisnicka_lozinka)


if __name__ == "__main__":
    main()
