""" glavni pokretač"""

from aiohttp import web
from operacije import operacije as op


# print(op.operacija["*"](7, 8))


async def izracunaj_post(request) -> dict:
    """post podataka"""
    podaci_za_izracun: dict = await request.json()
    return web.json_response(
        round(
            op.operacija[podaci_za_izracun["akcija"]](
                podaci_za_izracun["prvi_broj"], podaci_za_izracun["drugi_broj"]
            ),
            2,
        )
    )


app = web.Application()

app.router.add_routes([web.post("/kalkulator", izracunaj_post)])

web.run_app(app, port=8080)
