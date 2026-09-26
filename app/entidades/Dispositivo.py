from dataclasses import dataclass
from typing import Optional

@dataclass
class Dispositivo:
    placa:str
    nombre_chofer:str
    estado:str="Activo"
    id_dispositivo:Optional[int]=None