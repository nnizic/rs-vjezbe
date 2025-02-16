"""login i registracija"""

import asyncio

from aiohttp import web

from korisnici import hash_data, korisnici

app = web.Application()


def handler_function(request):
    """funkcija za povrat"""
    return web.json_response(korisnici)


async def register_function(request):
    """funkcija za registraciju"""
    data = await request.json()
    korisnici.append(
        {
            "korisnicko_ime": data["korisnicko_ime"],
            "lozinka_hash": hash_data(data["lozinka"]),
        }
    )
    return web.json_response(data)


async def login_function(request):
    """funkcija za login"""
    data = await request.json()
    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == data["korisnicko_ime"]:
            if korisnik["lozinka_hash"] == hash_data(data["lozinka"]):
                return web.Response(
                    status=200,
                    reason="OK",
                    text=f"Korisnik {korisnik["korisnicko_ime"]} pronađen.",
                )
            return web.Response(
                status=404, reason="Not Found", text="Neispravna lozinka."
            )
    return web.Response(
        status=404,
        reason="Not Found",
        text=f"Korisnik {data["korisnicko_ime"]} nije pronađen.",
    )


app.router.add_get("/", handler_function)
app.router.add_post("/register", register_function)
app.router.add_post("/login", login_function)

web.run_app(app, host="0.0.0.0", port=9000)
