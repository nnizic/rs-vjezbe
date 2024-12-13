"""
RS 5
Mikroservisi
Zadatak 3
punoljetni
2024.
"""

from aiohttp import web

korisnici: list = [
    {"ime": "Ivo", "godine": 25},
    {"ime": "Ana", "godine": 17},
    {"ime": "Marko", "godine": 19},
    {"ime": "Maja", "godine": 16},
    {"ime": "Iva", "godine": 22},
]


async def get_punoljetni(request):
    """korutina za punoljetne"""
    punoljetni_korisnici: list = [
        korisnik for korisnik in korisnici if korisnik["godine"] > 17
    ]
    return web.json_response(punoljetni_korisnici)


app = web.Application()

app.router.add_routes([web.get("/punoljetni", get_punoljetni)])

web.run_app(app, port=8082)
