"""servis1 - slanje i primanje liste brojeva"""

import aiohttp
import requests
from fastapi import FastAPI

app = FastAPI()

SERVIS_2_URL = "http://servis2:8000/dodaj"
SERVIS_3_URL = "http://servis3:8000/dodaj"


@app.post("/start")
async def start_game():
    """funkcija šalje i prima listu brojeva sa i na određeni servis"""
    lista_brojeva = {"lista_brojeva": [0]}
    while len(lista_brojeva["lista_brojeva"]) <= 10:
        servis_url = (
            SERVIS_2_URL
            if len(lista_brojeva["lista_brojeva"]) % 2 == 1
            else SERVIS_3_URL
        )
        async with aiohttp.ClientSession() as session:
            response = await session.post(servis_url, json=lista_brojeva)

            lista_brojeva = await response.json()

    return {"poruka": "Igra gotova", "lista_brojeva": lista_brojeva["lista_brojeva"]}
