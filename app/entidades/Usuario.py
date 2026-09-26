from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    nombre:str
    email:str
    contrasena:str
    rol:str
    id_usuario:Optional[int]=None