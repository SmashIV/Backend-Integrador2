from app.dto.TelemetriaDTO import TelemetriaLoteEntradaDTO
from app.servicios.TelemetriaService import TelemetriaService

# Simulamos la llegada del paquete del ESP32
payload = {
    "schema_version": 1,
    "batch_id": 105,
    "sent_at": 1756132800000,
    "readings": [
        {"sensor": "dht22_temp", "t": 1756132799000, "v": 33.5},
        {"sensor": "dht22_hum", "t": 1756132799000, "v": 65.0},
        {"sensor": "mq135_raw", "t": 1756132799000, "v": 210.0},
    ],
    "gps": [{"t": 1756132795000, "lat": -13.4152, "lon": -76.1348, "fix": 1}],
    "alerts": [],
}

# 1. El DTO valida el formato
datos_validados = TelemetriaLoteEntradaDTO(**payload)

# 2. El servicio procesa la información y la manda a la base de datos
servicio = TelemetriaService()
resultado = servicio.procesar_lote_telemetria(datos_validados)

# 3. Vemos el resultado
print("Estado:", resultado["mensaje"])
print("ID generado en BD:", resultado["id_lectura"])
print("Fecha:", resultado["fecha_registro"])
print("Diagnóstico:", resultado["alerta_microclima"])