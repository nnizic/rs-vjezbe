import asyncio
from aiohttp import web
from fastapi import FastAPI
from korisnici import korisnici
from korisnici import hash_data


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
                return web.json_response(korisnik)
            return web.json_response(korisnik)
        return web.json_response(korisnik)


app.router.add_get("/", handler_function)
app.router.add_post("/register", register_function)
app.router.add_post("/login", login_function)

web.run_app(app, host="localhost", port=9000)
