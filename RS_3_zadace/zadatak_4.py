"""
RS 3
Zadatak 4
- provjeravanje parnosti -
2024.
"""

import asyncio
import random


async def provjeri_parnost(broj: int) -> str:
    """provjera parnosti broja"""
    await asyncio.sleep(2)
    paran_neparan: str = lambda broj: (
        f"Broj {broj} je paran." if broj % 2 == 0 else f"Broj {broj} je neparan."
    )
    return paran_neparan(broj)


async def main() -> None:
    """glavna funkcija programa"""
    lista_brojeva: list = random.sample(range(1, 101), 10)
    zadaci: list = [asyncio.create_task(provjeri_parnost(i)) for i in lista_brojeva]
    rezultati: list = await asyncio.gather(*zadaci)

    print(rezultati)


if __name__ == "__main__":
    asyncio.run(main())
