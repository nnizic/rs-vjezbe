"""
RS 5
Mikroservisi
Zadatak 1
Lista proizvoda u JSON formatu
2024.
"""

from aiohttp import web


async def get_products(request):
    """korutina za dohvat"""
    proizvodi: list = [
        {"naziv": "lopata", "cijena": 250, "kolicina": 100},
        {"naziv": "motika", "cijena": 200, "kolicina": 120},
        {"naziv": "metla", "cijena": 150, "kolicina": 180},
    ]
    return web.json_response(proizvodi)


app = web.Application()

app.router.add_routes([web.get("/proizvodi", get_products)])

web.run_app(app, port=8081)
