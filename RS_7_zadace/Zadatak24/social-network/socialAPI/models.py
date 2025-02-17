"""osnovni modeli za socialAPI"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

ct = datetime.now()


class User(BaseModel):
    korisnicko_ime: str
    lozinka: str


class BlogRequest(BaseModel):
    """Blog: korisnik, tekst, vrijeme"""

    korisnik: str
    tekst: str
    vrijeme: Optional[float] = float(ct.timestamp())


class BlogRespond(BlogRequest):
    """dodan id"""

    id: int
