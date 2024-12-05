""" RS 4
Zadatak 1.
Dohvat korisnika 
"""

import asyncio
import time
import aiohttp


async def fetch_users(session) -> list:
    "poziv apiju"
    response = await session.get("https://jsonplaceholder.typicode.com/users")
    fact_dict = await response.json()
    return fact_dict


async def main() -> None:
    """glavna funkcija programa"""
    start: float = time.time()
    async with aiohttp.ClientSession() as session:
        fetch_korutine = [fetch_users(session) for i in range(5)]
        lista_rezultata = await asyncio.gather(*fetch_korutine)

    end: float = time.time()
    for i in range(5):
        imena: list = list(map(lambda korisnik: korisnik["name"], lista_rezultata[i]))
        uimena: list = list(
            map(lambda korisnik: korisnik["username"], lista_rezultata[i])
        )
        email: list = list(map(lambda korisnik: korisnik["email"], lista_rezultata[i]))
        print(f"IMENA:\n{imena}")
        print(f"KORISNIČKA IMENA:\n{uimena}")
        print(f"EMAIL ADRESE:\n{email}")

    print(f"\nIzvodenje programa je {end-start:.2f} sekundi.")


asyncio.run(main())
