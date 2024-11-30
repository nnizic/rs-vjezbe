""" 
RS 3
Zadatak 2
-2 apija, vraćaju dict, korištenje gather-
2024.
"""

import asyncio


async def fetch_api1() -> list:
    """api 1"""
    print("Dohvaćam podatke sa APIja 1...")
    await asyncio.sleep(3)
    print("Podatci sa APIja 1 dohvaćeni.")
    return [
        {"Ivan Ivic": "nije platio"},
        {"Mate Matic": "platio"},
        {"Vid Vidic": "platio"},
        {"Pere Peric": "nije platio"},
    ]


async def fetch_api2() -> list:
    """api 2"""
    print("Dohvaćam podatke sa APIja 2...")
    await asyncio.sleep(5)
    print("Podatci sa APIja 2 dohvaćeni.")
    return [
        {"monitor": "na stanju"},
        {"tipkovnica": "na stanju"},
        {"mis": "nema na stanju"},
    ]


async def main() -> None:
    """glavna funkcija programa"""
    podaci_1, podaci_2 = await asyncio.gather(fetch_api1(), fetch_api2())

    print(f"Podaci s API-ja 1: {podaci_1}")
    print(f"Podaci s API-ja 2: {podaci_2}")


asyncio.run(main())
