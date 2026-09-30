from sqlalchemy import select

from app.core.database import obtener_sesion
from app.entidades.Telemetria import Telemetria


class TelemetriaRepositorio:
    def guardar(self, lectura):
        with obtener_sesion() as sesion:
            sesion.add(lectura)
            sesion.flush()
        return lectura

    def obtener_ultimas_lecturas(self, limite=10):
        with obtener_sesion() as sesion:
            resultado = sesion.execute(
                select(Telemetria).order_by(Telemetria.fecha_hora.desc()).limit(limite)
            )
            return resultado.scalars().all()

    def obtener_ultimas_lecturas_byunidad(self, id_dispositivo, limite):
        with obtener_sesion() as sesion:
            subconsulta = (
                select(Telemetria.id_lectura)
                .where(Telemetria.id_dispositivo == id_dispositivo)
                .order_by(Telemetria.fecha_hora.desc())
                .limit(limite)
            )
            resultado = sesion.execute(
                select(Telemetria)
                .where(Telemetria.id_lectura.in_(subconsulta))
                .order_by(Telemetria.fecha_hora.asc())
            )
            return resultado.scalars().all()

    def obtener_ultima_lectura_byunidad(self, id_dispositivo):
        with obtener_sesion() as sesion:
            resultado = sesion.execute(
                select(Telemetria)
                .where(Telemetria.id_dispositivo == id_dispositivo)
                .order_by(Telemetria.fecha_hora.desc())
                .limit(1)
            )
            return resultado.scalar_one_or_none()
