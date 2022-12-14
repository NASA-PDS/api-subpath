# encoding: utf-8

from typing import Union
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def read_root() -> str:
    return {'Hello': '🌎'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None) -> str:
    return {'item_id': item_id, 'q': q}

