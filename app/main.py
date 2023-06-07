from typing import Optional
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI, Body


def init_bd():
    diccionario = {"name": ["Nepo"], "description": ["Humano"], "price": [0], "tax": [5]}
    base_datos = pd.DataFrame.from_dict(diccionario)
    return base_datos


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()  # pragma: no mutate

PATH_DATABASE = "/tmp/data_base.csv"


@app.post("/items/", status_code=201)
async def create_item(item: Item = Body(...)):
    base_datos = init_bd()
    base_datos = base_datos.append(item.__dict__, ignore_index=True)
    base_datos.to_csv(PATH_DATABASE, index_label="id")
    return item


@app.get("/")
def read_root():
    return {"msg": "Hello World from GECI - Ciencia de Datos!"}


@app.get("/make_add")
def make_add():
    return {"add": 4 + 6}


@app.get("/all_bd")
def get_all_items():
    base_datos = pd.read_csv(PATH_DATABASE)
    return base_datos.to_dict()
