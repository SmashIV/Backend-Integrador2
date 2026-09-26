from typing import List
from fastapi import APIRouter
from app.dto.AlertaDTO import AlertaRespuestaDTO
from app.servicios.AlertaService import AlertaService

router = APIRouter(prefix="/alertas", tags=["Alertas"])
servicio = AlertaService()

@router.get("/", response_model=List[AlertaRespuestaDTO])
def listar_alertas(limite:int=10):
    """
        Endpoint para que el front obtenga las alertas registradas
        validadas con el DTO de respuesta
    """
    return servicio.listar_alertas_recientes(limite)