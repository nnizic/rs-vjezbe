"""
RS 3
Zadatak 5.
- simulacija enkripcije podataka (hashlib modul) -
2024.

"""

import asyncio
import hashlib


def hash(value):
    """funkcija za hashiranje"""
    return hashlib.sha256(value.encode()).hexdigest()


async def secure_data(osjetljivi_podaci: dict) -> dict:
    """simulacija enkriptiranja"""
    print("Pokrećem enkripciju ...")
    await asyncio.sleep(3)
    return {
        "prezime": osjetljivi_podaci["prezime"],
        "broj_kartice": hash(osjetljivi_podaci["broj_kartice"]),
        "CVV": hash(osjetljivi_podaci["CVV"]),
    }


lista_osjetljivi_podaci: list = [
    {"prezime": "Ivic", "broj_kartice": "123456789", "CVV": "123"},
    {"prezime": "Matic", "broj_kartice": "987654321", "CVV": "111"},
    {"prezime": "Peric", "broj_kartice": "123443211", "CVV": "321"},
]


async def main() -> None:
    """glavn funkcija programa"""
    zadaci = [asyncio.create_task(secure_data(i)) for i in lista_osjetljivi_podaci]
    enkriptirano: dict = await asyncio.gather(*zadaci)
    print(enkriptirano)


if __name__ == "__main__":
    asyncio.run(main())
