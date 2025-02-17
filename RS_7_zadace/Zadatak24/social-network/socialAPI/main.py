"""fastapi mikroservis za blogove"""

import aiohttp
from fastapi import FastAPI, HTTPException

from models import BlogRequest, BlogRespond, User

app = FastAPI()
blogovi: list = [
    {
        "korisnik": "Kuglo Kuglić",
        "tekst": "Bio je lijep okrugli dan",
        "vrijeme": 1739636103.134426,
        "id": 1,
    },
    {
        "korisnik": "Krafno Marelić",
        "tekst": "Sve je plivalo u ulju.",
        "vrijeme": 1739636103.135555,
        "id": 2,
    },
    {
        "korisnik": "Krafno Marelić",
        "tekst": "Bilo je postuo finim prahom, kao šećerom u prahu.",
        "vrijeme": 1739636103.135765,
        "id": 3,
    },
]


# komunikacija između servisa:
@app.post("/login")
async def login(data: User):

    async with aiohttp.ClientSession() as session:
        async with session.post(
            "http://authapi:9000/login", json=data.dict()
        ) as response:
            if response.status != 200:
                raise HTTPException(
                    status_code=response.status,
                    detail=f"Login failed {response.status}: {await response.json()}",
                )
            response_data = await response.json()
            return {"poruka": "Login OK", "odgovor": response_data}


@app.get("/users")
async def getu_sers():
    async with aiohttp.ClientSession() as session:
        response = await session.get("http://authapi:9000")
        korisnici = await response.json()
        return korisnici


@app.get("/objava", response_model=list[BlogRespond])
def get_blogs():
    return blogovi


@app.post("/objava", response_model=BlogRespond)
def post_blog(blog: BlogRequest):
    new_id = len(blogovi) + 1
    blogs_id = BlogRespond(id=new_id, **blog.model_dump())
    blogovi.append(blogs_id)
    return blogs_id


@app.get("/objava/{id}", response_model=BlogRespond)
def get_blog_by_id(id: int):
    pronadjeni_blog = next((blog for blog in blogovi if blog["id"] == id), None)
    if pronadjeni_blog is None:
        raise HTTPException(status_code=404, detail="Blog nije pronađen.")
    return pronadjeni_blog


@app.get("/korisnici/{korisnik}/objave", response_model=list[BlogRespond])
def get_blogs_by_name(name: str):
    pronadjeni_blogovi = [blog for blog in blogovi if blog["korisnik"] == name]
    if len(pronadjeni_blogovi) == 0:
        raise HTTPException(status_code=404, detail="Korisnik nije pronađen.")
    return pronadjeni_blogovi
