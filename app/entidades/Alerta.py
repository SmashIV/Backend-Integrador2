from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Alerta:
    tipo_alerta:str
    id_lectura:int
    id_alerta:Optional[int]=None
    fecha_hora:Optional[datetime]=None
    fecha_vista:Optional[datetime]=None
    id_usuario:Optional[int]=None