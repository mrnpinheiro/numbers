from data.data import *
from fastapi import FastAPI
from logic import *
from models.model import Number
from pydantic import BaseModel

app = FastAPI()

# Main route
@app.get("/")
def index():
    return {
        "title":"numbers",
        "hello, stranger!": "Mariana Pinheiro"
        }

# Route get all consts
@app.get("/numbers/consts")
def get_all_consts():
    return get_const_data()

# Route get one number
@app.get("/numbers/{id_number}")
def get_numero_usando_id(id_number: int):
    return Number(
        id=id_number,
        proximo=next_number(id_number),
        anterior=previous_number(id_number),
        impar=odd_number(id_number),
        primo=prime_number(id_number),
        raiz=square_number(id_number),
        binario=binary_number(id_number),
        octal=oct_number(id_number)
    )
