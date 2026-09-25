from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Telemetria:
    temperatura:float
    humedad:float
    gases:float
    latitud:float
    longitud:float
    id_dispositivo:int
    fecha_hora: Optional[datetime] = None
    id_lectura: Optional[int] = None
