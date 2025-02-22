from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/dodaj")
async def dodaj_broj(request: Request):
    """dodaje broj u listu_brojeva"""
    data = await request.json()
    data["lista_brojeva"].append(len(data["lista_brojeva"]))
    return data
