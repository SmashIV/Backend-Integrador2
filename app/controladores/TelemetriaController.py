from fastapi import APIRouter, status, Query, HTTPException
from typing import List
from app.dto.TelemetriaDTO import TelemetriaLoteEntradaDTO, TelemetriaRespuestaDTO
from app.servicios.TelemetriaService import TelemetriaService

router = APIRouter(prefix="/telemetria", tags = ["Telemetria"])
servicio = TelemetriaService()

@router.post("/",status_code=status.HTTP_201_CREATED)
def recibir_telemetria(datos: TelemetriaLoteEntradaDTO):
    """
        Endpoint que recibe el paquete JSON desde el ESP32,
        lo valida mediante el DTO y lo manda a procesar al
        servicio
    """
    respuesta = servicio.procesar_lote_telemetria(datos)
    return respuesta

@router.get("/")
def consultar_telemetria(limite: int=10):
    """Endpoint para que el front reciba las últimas lecturas de los camiones"""
    return servicio.obtener_ultimas_lecturas(limite)

@router.get(
    "/dispositivo/{id_dispositivo}",
    response_model=List[TelemetriaRespuestaDTO],
    summary="Historial de telemetría del camión"
)
def obtener_historial_camion(id_dispositivo, limite):
    return servicio.obtener_ultimas_lecturas_byunidad(id_dispositivo, limite)

@router.get(
    "/dispositivo/{id_dispositivo}/ultima",
    response_model=TelemetriaRespuestaDTO,
    summary="Ultima lectura y ubicacion del camión"
)
def obtener_ultima_lectura_byunidad(id_dispositivo):
    lectura = servicio.obtener_ultima_lectura_byunidad(id_dispositivo)
    if not lectura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encontraron lecturas para el dispositivo {id_dispositivo}"
        )
    return lectura

@router.get(
    "/recientes",
    response_model=List[TelemetriaRespuestaDTO],
    summary="Historial general"
)
def obtener_historial_general(limite):
    return servicio.obtener_ultimas_lecturas(limite)