""" osnovni modeli za socialAPI """

from datetime import datetime
from typing import Optional
from pydantic import BaseModel

ct = datetime.now()


class BlogRequest(BaseModel):
    """Blog: korisnik, tekst, vrijeme"""

    korisnik: str
    tekst: str
    vrijeme: Optional[float] = float(ct.timestamp())


class BlogRespond(BlogRequest):
    """dodan id"""

    id: int
