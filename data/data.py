import math
from models.model import Const

# Date base math consts
def get_const_data():
    return [
        Const(
            id=1,
            number=math.pi,
            oficial_name="Pi",
            other_name="constante de Arquimedes ou número de Ludoph",
            symbol="π"
        ),
        Const(
            id=2,
            number=math.e,
            oficial_name="número de Euler",
            other_name="constante de Napier, base do Logaritmo natural",
            symbol="e"
        )
    ]
