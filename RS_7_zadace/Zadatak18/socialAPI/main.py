""" fastapi mikroservis za blogove """

from fastapi import FastAPI
from models import BlogRequest, BlogRespond

app = FastAPI()
blogovi: list = []


@app.get("/objava", response_model=BlogRespond)
def get_blogs():
    return blogovi
