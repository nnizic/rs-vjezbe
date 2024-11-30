""" RS 3
Zadatak 1
-simuliranje dohvaćanje podataka sa weba-
2024."""

import asyncio


async def dohvati_podatke() -> dict:
    """korutina 1"""
    print("Dohvaćam podatke...")
    await asyncio.sleep(3)
    podaci = {"podaci": [i for i in range(1, 11)], "status": "ok"}
    print("Podaci su dohvaćeni...")
    return podaci


async def main() -> None:
    """glavna funkcija programa"""
    rezultati: dict = await dohvati_podatke()
    print(f"Rezultati su: {rezultati}")


asyncio.run(main())
