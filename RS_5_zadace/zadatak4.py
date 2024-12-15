"""
RS5
Zadatak4.
aiohttp
/proizvodi
/proizvodi/{id}
2024.
"""

import asyncio, aiohttp
from aiohttp import web
from aiohttp.web import AppRunner

proizvodi: list = [
    {"id": 1, "naziv": "Laptop", "cijena": 2500},
    {"id": 2, "naziv": "Mis", "cijena": 22},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 59},
    {"id": 4, "naziv": "Monitor", "cijena": 210},
    {"id": 5, "naziv": "Slusalice", "cijena": 40},
]

app = web.Application()


async def get_proizvodi(request) -> dict:
    """dohvat svih proizvoda"""
    return web.json_response(proizvodi)


async def get_proizvod(request) -> dict:
    """dohvat proizvoda"""
    user_id = request.match_info["id"]

    for proizvod in proizvodi:
        if proizvod["id"] == int(user_id):
            return web.json_response(proizvod, status=200)

    return web.json_response(
        {"error": "Proizvod s trazenim ID-em ne postoji"}, status=404
    )


app.router.add_get("/proizvodi/{id}", get_proizvod)
app.router.add_get("/proizvodi", get_proizvodi)


async def start_server() -> None:
    """startanje simulacije servera"""
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8080)
    await site.start()
    print("Poslužitelj sluša na 8080")


async def main() -> None:
    """glavna funkcija programa"""
    await start_server()
    async with aiohttp.ClientSession() as session:
        print("Klijent otvoren")
        rezultati = await session.get("http://localhost:8080/proizvodi")
        rezultat_jedan = await session.get("http://localhost:8080/proizvodi/6")
        print(await rezultati.text())
        print(await rezultat_jedan.text())


asyncio.run(main())
