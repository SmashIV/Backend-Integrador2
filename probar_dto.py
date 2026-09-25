from app.dto.TelemetriaDTO import TelemetriaLoteEntradaDTO

# Simulamos exactamente el JSON que enviará el ESP32
payload_simulado = {
    "schema_version": 1,
    "batch_id": 4821,
    "sent_at": 1756132800000,
    "readings": [
        {"sensor": "dht22_temp", "t": 1756132799000, "v": 25.4},
        {"sensor": "dht22_hum", "t": 1756132799000, "v": 62.1},
        {"sensor": "mq135_raw", "t": 1756132799000, "v": 115.0}
    ],
    "gps": [
        {"t": 1756132795000, "lat": -13.4152, "lon": -76.1348, "fix": 1}
    ],
    "alerts": []
}

# Pasamos los datos por el DTO
paquete_validado = TelemetriaLoteEntradaDTO(**payload_simulado)

print("¡Validación exitosa!")
print(f"Camión asignado automáticamente: {paquete_validado.device_id}")
print(f"Total de lecturas de sensores recibidas: {len(paquete_validado.readings)}")
print(f"Primer sensor: {paquete_validado.readings[0].sensor} = {paquete_validado.readings[0].v}")