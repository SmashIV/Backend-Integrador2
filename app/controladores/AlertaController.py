from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from app.dto.AlertaDTO import AlertaRespuestaDTO
from app.servicios.AlertaService import AlertaService

from app.core.auth import obtener_usuario_actual

router = APIRouter(prefix="/alertas", tags=["Alertas"])
servicio = AlertaService()

@router.get("/", response_model=List[AlertaRespuestaDTO])
def listar_alertas(limite:int=10, _: dict = Depends(obtener_usuario_actual)):
    """
        Endpoint para que el front obtenga las alertas registradas
        validadas con el DTO de respuesta
    """
    if limite < 0 :
        # TODO: Decidir despues si para este caso emitir una excepcion o solo ignorar. Por ahora se ignora.
        # raise HTTPException(
        #    status_code=status.HTTP_400_BAD_REQUEST,
        #    detail=f"No existe un limite negativo"
        #)
        limite = 10
    return servicio.listar_alertas_recientes(limite)

@router.put(
    "/{id_alerta}/atender",
    response_model=AlertaRespuestaDTO,
    summary="Marcar alerta como atendida",
)
def atender_alerta(id_alerta:int,
                   usuario: dict = Depends(obtener_usuario_actual)):
    alerta_atendida = servicio.atender_alerta(id_alerta, usuario["id_usuario"])
    if not alerta_atendida:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"La alerta con ID {id_alerta} no existe",
        )
    return alerta_atendida