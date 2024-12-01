"""
RS 3
Zadatak 3
- autentifikacija / autorizacija -
2024.
"""

import asyncio

baza_korisnika: list = [
    {"korisnicko_ime": "mirko123", "email": "mirko123@gmail.com"},
    {"korisnicko_ime": "ana_anic", "email": "aanic@gmail.com"},
    {"korisnicko_ime": "maja_0x", "email": "majaaaaa@gmail.com"},
    {"korisnicko_ime": "zdeslav032", "email": "deso032@gmail.com"},
]

baza_lozinka: list = [
    {"korisnicko_ime": "mirko123", "lozinka": "lozinka123"},
    {"korisnicko_ime": "ana_anic", "lozinka": "super_teska_lozinka"},
    {"korisnicko_ime": "maja_0x", "lozinka": "s324SDFfdsj234"},
    {"korisnicko_ime": "zdeslav032", "lozinka": "deso123"},
]


async def autentifikacija(korisnik: dict) -> str:
    """korutina 1: simulacija autentifikacije"""
    print("Pokrećem autentifikaciju ....")
    await asyncio.sleep(3)
    for kor in baza_korisnika:
        if (
            kor["korisnicko_ime"] == korisnik["korisnicko_ime"]
            and kor["email"] == korisnik["email"]
        ):
            autoriziranje: str = await autorizacija(kor, korisnik["lozinka"])
            return autoriziranje
    return f"Korisnik {korisnik} nije pronađen."


async def autorizacija(korisnik, lozinka) -> str:
    """korutina 2: simulacija autorizacije"""
    print("pokrećem autorizaciju ...")
    await asyncio.sleep(2)
    for kor in baza_lozinka:
        if kor["korisnicko_ime"] == korisnik["korisnicko_ime"]:
            if kor["lozinka"] == lozinka:
                return f"korisnik {korisnik}: Autorizacija uspješna."
            return f"korisnik {korisnik}: Autorizacija neuspješna."


async def main() -> None:
    """glavna funkcija programa"""
    proizvoljni_korisnik: dict = {
        "korisnicko_ime": "ana_anic",
        "email": "aanic@gmail.com",
        "lozinka": "super_teska_lozinka",
    }

    autentificiranje_korisnika = await autentifikacija(proizvoljni_korisnik)
    print(autentificiranje_korisnika)


if __name__ == "__main__":
    asyncio.run(main())
