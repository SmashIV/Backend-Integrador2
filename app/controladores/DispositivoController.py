from typing import List
from fastapi import APIRouter, HTTPException, status
from app.dto.DispositivoDTO import DispositivoCrearDTO, DispositivoRespuestaDTO
from app.servicios.DispositivoService import DispositivoService

router = APIRouter(prefix="/dispositivos", tags=["Dispositivos"])
servicio = DispositivoService()

@router.post(
    "/",
    response_model=DispositivoRespuestaDTO,
    status_code=status.HTTP_201_CREATED,
    summary="Registrar nuevo dispositivo",
    )
def registrar_dispositivo(datos:DispositivoCrearDTO):
    try:
        dispositivo = servicio.registrar_dispositivo(datos)
        return dispositivo
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        )

@router.get(
    "/",
    response_model=List[DispositivoRespuestaDTO],
    summary="Listar dispositivos registrados"
)
def listar_dispositivos():
    return servicio.listar_dispositivos()

@router.get(
    "/{id_dispositivo}",
    response_model=DispositivoRespuestaDTO,
    summary="Buscar por id",
)
def obtener_byid(id_dispositivo):
    dispositivo = servicio.obtener_byid(id_dispositivo)
    if not dispositivo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Dispositivo con ID {id_dispositivo} no encontrado"
        )
    return dispositivo