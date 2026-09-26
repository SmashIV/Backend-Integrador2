from app.dto.TelemetriaDTO import TelemetriaLoteEntradaDTO
from app.entidades.Telemetria import Telemetria
from app.repositorios.TelemetriaRepositorio import TelemetriaRepositorio
from app.entidades.Alerta import Alerta
from app.repositorios.AlertaRepositorio import AlertaRepositorio

class TelemetriaService:
    def __init__(self):
        self.telemetria_repositorio = TelemetriaRepositorio()
        self.alerta_repositorio = AlertaRepositorio()

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
        entidad_telemetria = Telemetria(
            temperatura = temperatura,
            humedad = humedad,
            gases = gases,
            latitud = latitud,
            longitud = longitud,
            id_dispositivo = lote.device_id,
        )

        #Guardar en bd
        telemetria_guardado = self.telemetria_repositorio.guardar(entidad_telemetria)

        #Configuración de alertas
        tipo_alerta = None
        alerta_guardada = None
        if temperatura > 32.0:
            tipo_alerta = f"Alerta: Calor crítico ({temperatura}°C)"
        elif temperatura < 12.0:
            tipo_alerta = f"Alerta: Temperatura baja ({temperatura}°C)"
        elif gases > 300:
            tipo_alerta = f"Concentracion alta de gases ({gases} ppm)"

        if tipo_alerta:
            nueva_alerta = Alerta(
                tipo_alerta = tipo_alerta,
                id_lectura = telemetria_guardado.id_lectura,
            )
            alerta_guardada = self.alerta_repositorio.guardar(nueva_alerta)

        return{
            "mensaje":"Lote procesado exitosamente",
            "id_lectura":telemetria_guardado.id_lectura,
            "dispositivo":telemetria_guardado.id_dispositivo,
            "fecha_registro":telemetria_guardado.fecha_hora,
            "alerta_generada":{
                "id_alerta":(
                    alerta_guardada.id_alerta if alerta_guardada else None
                ),
                "tipo":tipo_alerta,
            },  
        }

    def obtener_historial_reciente (self, limite: int=10):
        "Consulta el repositorio para traer las ultimas lecturas registradas."
        return self.telemetria_repositorio.obtener_ultimas_lecturas(limite)