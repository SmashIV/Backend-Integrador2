from app.dto.TelemetriaDTO import TelemetriaLoteEntradaDTO
from app.entidades.Telemetria import Telemetria
from app.repositorios.TelemetriaRepositorio import TelemetriaRepositorio

class TelemetriaService:
    def __init__(self):
        self.repositorio = TelemetriaRepositorio()

    def procesar_lote_telemetria(self, lote:TelemetriaLoteEntradaDTO):
        temperatura = 0.0
        humedad = 0.0
        gases = 0.0

        #Datos de la lista de sensores
        for lectura in lote.readings:
            if lectura.sensor == "dht22_temp":
                temperatura = lectura.v
            elif lectura.sensor == "dht22_hum":
                humedad = lectura.v
            elif lectura.sensor == "mq135_raw":
                gases = lectura.v

        #Coordenadas gps       
        latitud = 0.0
        longitud = 0.0
        if lote.gps:
            ultima_coordenada = lote.gps[-1]
            latitud = ultima_coordenada.lat
            longitud = ultima_coordenada.lon

        #Modelo para insertar en bd
        entidad = Telemetria(
            temperatura = temperatura,
            humedad = humedad,
            gases = gases,
            latitud = latitud,
            longitud = longitud,
            id_dispositivo = lote.device_id,
        )

        #Guardar en bd
        guardado = self.repositorio.guardar(entidad)

        #Configuración de alertas
        alerta = None
        if temperatura > 32.0:
            alerta = (
                f"Alerta: Temperatura crítica ({temperatura}°C) - Riesgo de estrés térmico"
            )
        elif temperatura < 12.0:
            alerta = (
                f"Alerta: Temperatura baja ({temperatura}°C - Riesgo de hipotermia)"
            )
        return{
            "mensaje":"Lote procesado exitosamente",
            "id_lectura":guardado.id_lectura,
            "dispositivo":guardado.id_dispositivo,
            "fecha_registro":guardado.fecha_hora,
            "alerta_microclima":alerta,
        }
        