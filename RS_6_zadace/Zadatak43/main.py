""" glavna datoteka mikroservisa za filmove """

from fastapi import FastAPI
from routers.filmovi import router as filmovi_router

app = FastAPI()

app.include_router(filmovi_router)


@app.get("/")
def home():
    """osnovni odgovor servisa"""
    return {"poruka": "Microservis za filmove" "Microservis za filmove"}
