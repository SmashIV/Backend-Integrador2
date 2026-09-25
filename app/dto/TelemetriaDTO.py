from pydantic import BaseModel, Field
from typing import List, Optional

class LecturaSensorDTO(BaseModel):
    sensor:str
    t:int
    v:float

class CoordenadasDTO(BaseModel):
    t:int
    lat:float
    lon:float
    speed:Optional[float] = 0.0
    alt:Optional[float] = 0.0
    fix:int

class AlertasDTO(BaseModel):
    sensor:str
    type:str
    threshold:float
    value:float
    t:int

class TelemetriaLoteEntradaDTO(BaseModel):
    device_id: Optional[int] = Field(default=1, description="Camion 1")
    schema_version:int
    batch_id:int
    sent_at:int
    readings:List[LecturaSensorDTO]
    gps:List[CoordenadasDTO]
    alerts:Optional[List[AlertasDTO]] = []