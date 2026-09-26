from typing import List
from fastapi import APIRouter, HTTPException, status
from app.dto.AlertaDTO import AlertaRespuestaDTO, AtenderAlertaDTO
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

@router.put(
    "/{id_alerta}/atender",
    response_model=AlertaRespuestaDTO,
    summary="Marcar alerta como atendida",
)
def atender_alerta(id_alerta:int, datos:AtenderAlertaDTO):
    alerta_atendida = servicio.atender_alerta(id_alerta, datos.id_usuario)
    if not alerta_atendida:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La alerta con ID {id_alerta} no existe",
        )
    return alerta_atendida