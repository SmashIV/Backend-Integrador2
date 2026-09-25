from fastapi import APIRouter, status
from app.dto.TelemetriaDTO import TelemetriaLoteEntradaDTO
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

