# Model regular numbers
from pydantic import BaseModel

class Number(BaseModel):
    id: int
    proximo: int
    anterior: int
    impar: bool
    primo: bool
    raiz: float
    binario: str
    octal: str

# Model const numbers
class Const(BaseModel):
    id: int
    number: float
    oficial_name: str
    other_name: str
    symbol: str
