from app.entidades.Telemetria import Telemetria
from app.repositorios.TelemetriaRepositorio import TelemetriaRepositorio

# 1. Preparamos el repositorio
repo = TelemetriaRepositorio()

# 2. Simulamos una lectura que mandaría el camión 1
datos_simulados = Telemetria(
    temperatura=24.5,
    humedad=60.0,
    gases=120.0,
    latitud=-13.41,
    longitud=-76.13,
    id_dispositivo=1
)

# 3. Guardamos en la base de datos usando el repositorio
lectura_guardada = repo.guardar(datos_simulados)

# 4. Mostramos el resultado
print("¡Lectura guardada con éxito en PostgreSQL!")
print(f"ID asignado por la base de datos: {lectura_guardada.id_lectura}")
print(f"Fecha y hora registrada: {lectura_guardada.fecha_hora}")