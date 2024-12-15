"""
RS5
Zadatak5.
aiohttp
GET:
/proizvodi
/proizvodi/{id}
POST:
/narudzbe
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

narudzbe: list = []
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


async def post_narudzbe(request) -> dict:
    """stvaranje narudzbi"""
    podatci_za_narudzbu: dict = await request.json()
    for pro in proizvodi:
        if podatci_za_narudzbu["proizvod_id"] == pro["id"]:
            narudzbe.append(podatci_za_narudzbu)
            return web.json_response(narudzbe, status=200)
        return web.json_response(
            {"error": "Proizvod s traznim ID-em ne postoji"}, status=404
        )


# dodavanje ruta sve u jednom
app.router.add_routes(
    [
        web.get("/proizvodi/{id}", get_proizvod),
        web.get("/proizvodi", get_proizvodi),
        web.post("/narudzbe", post_narudzbe),
    ]
)


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
        rezultat_jedan = await session.get("http://localhost:8080/proizvodi/3")
        rezultati_dva = await session.post(
            "http://localhost:8080/narudzbe", json={"proizvod_id": 1, "kolicina": 2}
        )
        print(await rezultati.text())
        print(await rezultat_jedan.text())
        print(await rezultati_dva.text())


asyncio.run(main())
