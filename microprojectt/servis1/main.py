"""servis1 - slanje i primanje liste brojeva"""

import asyncio

import aiohttp
from fastapi import FastAPI
from fastapi.responses import StreamingResponse

app = FastAPI()

SERVIS_2_URL = "http://servis2:8000/dodaj"
SERVIS_3_URL = "http://servis3:8000/dodaj"


async def stream_game():
    """Asinkroni generator koji šalje i prima listu brojeva"""
    lista_brojeva = {"lista_brojeva": [0]}
    while len(lista_brojeva["lista_brojeva"]) <= 10:
        servis_url = (
            SERVIS_2_URL
            if len(lista_brojeva["lista_brojeva"]) % 2 == 1
            else SERVIS_3_URL
        )
        servis_naziv = "Servis 2" if servis_url == SERVIS_2_URL else "Servis 3"
        async with aiohttp.ClientSession() as session:
            response = await session.post(servis_url, json=lista_brojeva)
            lista_brojeva = await response.json()
            yield f'data: {{"poruka": "Broj dodani od {servis_naziv}", "lista_brojeva": {lista_brojeva["lista_brojeva"]}}}\n\n'
        await asyncio.sleep(1)

    yield f'data: {{"poruka": "Igra gotova", "lista_brojeva": {lista_brojeva["lista_brojeva"]}}}\n\n'


@app.post("/start")
async def start_game():
    """Pokretanje strimanja igre"""
    return StreamingResponse(stream_game(), media_type="text/event-stream")
