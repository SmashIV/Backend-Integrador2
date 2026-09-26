from app.entidades.Alerta import Alerta
from app.repositorios.AlertaRepositorio import AlertaRepositorio

repo = AlertaRepositorio()

# 1. Creamos una alerta asociada a la lectura 3 (que ya existe en tu BD)
nueva_alerta = Alerta(
    tipo_alerta="Estrés Térmico (Prueba Manual)",
    id_lectura=3
)

# 2. Guardamos en PostgreSQL
alerta_guardada = repo.guardar(nueva_alerta)

print("¡Alerta guardada exitosamente en PostgreSQL!")
print(f"ID Alerta generado: {alerta_guardada.id_alerta}")
print(f"Fecha y hora: {alerta_guardada.fecha_hora}")

# 3. Consultamos las alertas registradas
lista = repo.obtener_alertas_recientes(5)
print(f"Total de alertas obtenidas: {len(lista)}")
print("Primera alerta del historial:", lista[0]["tipo_alerta"])